"""Domain/geo language routing (no network: GEO_IP_LOOKUP=0, countries simulated via CF-IPCountry)."""
import os

os.environ.setdefault("GEO_IP_LOOKUP", "0")
os.environ.setdefault("OPENROUTER_API_KEY", "")

import pytest
from starlette.testclient import TestClient

import content.news as news
news.start_background_refresh = lambda: None
from app import app  # noqa: E402

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
BOT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"


def client(host):
    return TestClient(app, base_url=f"https://{host}", follow_redirects=False)


def get(host, path="/", country=None, ua=UA, **kw):
    h = {"user-agent": ua}
    if country:
        h["cf-ipcountry"] = country
    return client(host).get(path, headers=h, **kw)


def test_lt_visitor_on_ai_redirects_to_lt():
    r = get("predictivelabs.ai", "/team?x=1", "LT")
    assert r.status_code == 302
    assert r.headers["location"] == "https://predictivelabs.lt/team?x=1"
    assert "no-store" in r.headers["cache-control"]


def test_lt_domain_serves_lithuanian_and_never_redirects():
    for c in ("LT", "US", "GB", None):
        r = get("predictivelabs.lt", "/", c)
        assert r.status_code == 200
        assert '<html lang="lt"' in r.text
        assert "UAB „Predictive Labs“" in r.text


def test_ai_english_for_other_countries():
    for c in ("US", "GB", "DE", None):
        r = get("predictivelabs.ai", "/", c)
        assert r.status_code == 200 and '<html lang="en"' in r.text


def test_bots_not_geo_redirected():
    r = get("predictivelabs.ai", "/", "LT", ua=BOT)
    assert r.status_code == 200 and '<html lang="en"' in r.text


def test_stay_param_and_cookie_stop_redirect():
    c = client("predictivelabs.ai")
    r = c.get("/?stay=1", headers={"user-agent": UA, "cf-ipcountry": "LT"})
    assert r.status_code == 200 and "pl_stay" in r.headers.get("set-cookie", "")
    r = c.get("/", headers={"user-agent": UA, "cf-ipcountry": "LT"})
    assert r.status_code == 200


def test_manual_switch_persists_per_host():
    c = client("predictivelabs.lt")
    c.post("/lang", data={"lang": "en"}, headers={"user-agent": UA})
    r = c.get("/", headers={"user-agent": UA})
    assert '<html lang="en"' in r.text
    # and on .ai a manual choice blocks the geo redirect
    a = client("predictivelabs.ai")
    a.post("/lang", data={"lang": "en"}, headers={"user-agent": UA})
    assert a.get("/", headers={"user-agent": UA, "cf-ipcountry": "LT"}).status_code == 200


def test_lang_query_on_ai():
    r = get("predictivelabs.ai", "/?lang=lt", "US")
    assert '<html lang="lt"' in r.text


def test_hreflang_and_canonical():
    r = get("predictivelabs.lt", "/platform")
    assert '<link rel="canonical" href="https://predictivelabs.lt/platform">' in r.text
    assert 'hreflang="lt" href="https://predictivelabs.lt/platform"' in r.text
    assert 'hreflang="en" href="https://predictivelabs.ai/platform"' in r.text
    assert 'hreflang="x-default" href="https://predictivelabs.ai/platform"' in r.text
    r = get("predictivelabs.eu", "/")
    assert '<link rel="canonical" href="https://predictivelabs.ai/">' in r.text


def test_static_and_post_not_redirected():
    assert get("predictivelabs.ai", "/static/site.css", "LT").status_code == 200
    r = client("predictivelabs.ai").post("/lang", data={"lang": "lt"}, headers={"user-agent": UA, "cf-ipcountry": "LT"})
    assert r.status_code == 200


@pytest.mark.parametrize("path", ["/", "/platform", "/solutions/defense", "/solutions/healthcare", "/solutions/public",
                                  "/solutions/financial", "/case-studies", "/signal", "/open-source", "/partners",
                                  "/team", "/thesis", "/contact"])
def test_all_pages_render_lt(path):
    r = get("predictivelabs.lt", path)
    assert r.status_code == 200 and '<html lang="lt"' in r.text
