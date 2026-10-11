"""Country domains -> default UI language (pattern from CityTicker utils/domains.py).

Language precedence (utils.i18n.get_lang):
    ?lang= URL locale > manual choice (session, per host) > ccTLD > visitor country > en

Geo redirect (app.py middleware): a human visitor on a generic domain
(predictivelabs.ai) whose country has its own live ccTLD in GEO_REDIRECT
(LT -> predictivelabs.lt) gets one 302 to that domain. Never for bots, never
from a ccTLD, never after a manual choice (pl_stay cookie / ?stay=1 / ?lang=),
so it cannot loop.
"""
from __future__ import annotations

import os
from html import escape

BRAND = "predictivelabs"
X_DEFAULT = "predictivelabs.ai"

# suffix after "predictivelabs." -> default lang (None = generic, detect by geo)
DOMAIN_TABLE: dict[str, str | None] = {
    "ai": None, "eu": None, "com": None,
    "lt": "lt", "ee": None,  # et once Estonian is published (phase 2)
    "co.uk": "en", "uk": "en",
    # ready if registered later
    "lv": "lv", "fi": "fi", "se": "sv", "no": "no", "dk": "da", "de": "de",
    "fr": "fr", "pt": "pt", "es": "es", "pl": "pl", "nl": "nl",
}

# Domains that actually resolve to this app today (hreflang + redirect targets).
DEFAULT_LIVE = ("predictivelabs.ai", "predictivelabs.lt", "predictivelabs.ee", "predictivelabs.eu", "predictivelabs.co.uk")

# Country -> ccTLD host for the one-time geo redirect from generic domains.
DEFAULT_GEO_REDIRECT = {"lt": "predictivelabs.lt"}

# Domains that duplicate the English .ai site: canonical points at .ai.
ALIAS_OF_AI = ("predictivelabs.eu", "predictivelabs.co.uk", "predictivelabs.com")


def request_host(request) -> str:
    if request is None:
        return ""
    try:
        h = request.headers.get("x-forwarded-host") or request.headers.get("host") or ""
    except Exception:
        return ""
    h = h.split(",")[0].strip().lower().split(":")[0]
    return h[4:] if h.startswith("www.") else h


def tld_of(host: str) -> str | None:
    host = (host or "").lower()
    host = host[4:] if host.startswith("www.") else host
    if not host.startswith(BRAND + "."):
        return None
    sfx = host[len(BRAND) + 1:]
    return sfx if sfx in DOMAIN_TABLE else None


def domain_lang(request=None, host: str | None = None) -> str | None:
    tld = tld_of(host if host is not None else request_host(request))
    return DOMAIN_TABLE.get(tld) if tld else None


def is_generic(host: str) -> bool:
    tld = tld_of(host)
    return tld is not None and DOMAIN_TABLE.get(tld) is None


def live_domains() -> list[str]:
    raw = os.environ.get("PL_DOMAINS", "")
    return [d.strip().lower() for d in raw.split(",") if d.strip()] or list(DEFAULT_LIVE)


def geo_redirect_map() -> dict[str, str]:
    """PL_GEO_REDIRECT='lt=predictivelabs.lt,ee=predictivelabs.ee' overrides; 'off' disables."""
    raw = os.environ.get("PL_GEO_REDIRECT", "").strip()
    if raw.lower() in ("off", "0", "none", "false"):
        return {}
    if raw:
        out = {}
        for part in raw.split(","):
            if "=" in part:
                k, v = part.split("=", 1)
                out[k.strip().lower()] = v.strip().lower()
        return out
    live = set(live_domains())
    return {cc: d for cc, d in DEFAULT_GEO_REDIRECT.items() if d in live}


# Languages without their own live ccTLD are served on .ai under ?lang=xx.
def lang_href(lang: str, path: str = "/") -> str:
    for d in live_domains():
        if domain_lang(host=d) == lang and d not in ALIAS_OF_AI:
            return f"https://{d}{path}"
    if lang == "en":
        return f"https://{X_DEFAULT}{path}"
    sep = "&" if "?" in path else "?"
    return f"https://{X_DEFAULT}{path}{sep}lang={lang}"


HREFLANG_CODE = {"no": "nb"}


def head_tags(request, path: str, lang: str, langs) -> str:
    host = request_host(request) or X_DEFAULT
    if tld_of(host) is None or host in ALIAS_OF_AI:
        host = X_DEFAULT
    if is_generic(host) and lang != "en":
        canonical = lang_href(lang, path)
    elif is_generic(host) or host == X_DEFAULT:
        canonical = f"https://{X_DEFAULT}{path}"
    else:
        canonical = f"https://{host}{path}"
    tags = [f'<link rel="canonical" href="{escape(canonical)}">']
    for code in langs:
        tags.append(f'<link rel="alternate" hreflang="{HREFLANG_CODE.get(code, code)}" href="{escape(lang_href(code, path))}">')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="https://{X_DEFAULT}{escape(path)}">')
    return "".join(tags)
