"""Visitor country detection (same order as CityTicker's utils/geo.py).

  1. CDN/proxy country headers (CF-IPCountry, X-Country-Code, ...) — also lets
     tests and curl simulate a country.
  2. Cached IP -> country lookup (ipapi.co, then ip-api.com), 24 h in-process cache.
  3. Tiny emergency IP-prefix list (Baltic ISPs).
predictivelabs.* is not behind Cloudflare today (A -> Coolify/Traefik), so (2)
is what resolves real visitors.
"""
from __future__ import annotations

import json
import logging
import os
import re
import time
import urllib.request

logger = logging.getLogger(__name__)

COUNTRY_HEADERS = ("cf-ipcountry", "x-country-code", "x-vercel-ip-country", "cloudfront-viewer-country")

# ISO country -> UI language (only languages the site ships).
COUNTRY_LANG = {
    "lt": "lt", "ee": "et", "lv": "lv", "fi": "fi", "ax": "sv", "se": "sv",
    "no": "no", "dk": "da", "fo": "da", "gl": "da", "is": "en",
    "de": "de", "at": "de", "li": "de", "ch": "de",
    "fr": "fr", "mc": "fr", "lu": "fr",
    "pt": "pt", "es": "es", "ad": "es", "pl": "pl", "nl": "nl",
    "gb": "en", "uk": "en", "ie": "en", "us": "en", "ca": "en", "au": "en", "nz": "en",
}

_EMERGENCY_PREFIXES = {
    "lt": ("82.135.", "78.56.", "78.57.", "78.58.", "78.60.", "78.61.", "78.62.", "78.63.", "213.252."),
    "ee": ("85.253.", "90.190.", "84.50.", "213.168.", "195.50.", "62.65.", "88.196.", "86.43.", "193.40.", "194.126.", "213.35."),
    "lv": ("195.13.", "213.175.", "195.122.", "80.233.", "78.84."),
}

_CACHE: dict[str, tuple[float, str | None]] = {}
_TTL = float(os.environ.get("GEO_IP_CACHE_TTL", "86400"))
_TIMEOUT = float(os.environ.get("GEO_IP_TIMEOUT", "1.5"))


def _api_enabled() -> bool:
    return os.environ.get("GEO_IP_LOOKUP", "1").strip().lower() not in ("0", "false", "no", "off")


BOT_RE = re.compile(
    r"bot|crawl|spider|slurp|bingpreview|mediapartners|facebookexternalhit|embedly|quora link|"
    r"whatsapp|telegram|slack|discord|linkedin|twitter|skype|vkshare|w3c_validator|lighthouse|"
    r"headless|python-requests|curl/|wget|httpx|go-http|axios|semrush|ahrefs|yandex|baidu|duckduck|petal|gptbot|claude|perplexity",
    re.I,
)


def is_bot(request) -> bool:
    try:
        ua = request.headers.get("user-agent", "") or ""
    except Exception:
        return False
    return not ua or bool(BOT_RE.search(ua))


def client_ip(request) -> str | None:
    try:
        fwd = request.headers.get("x-forwarded-for", "")
        if fwd:
            return fwd.split(",")[0].strip()
        real = request.headers.get("x-real-ip", "")
        if real:
            return real.strip()
        return request.client.host if request.client else None
    except Exception:
        return None


def _private(ip: str) -> bool:
    return ip in ("::1", "testclient") or ip.startswith(("127.", "10.", "192.168.", "172.16.", "172.17.", "172.18.", "172.2", "172.3", "fc", "fd"))


def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "PredictiveLabsGeo/1.0 (+https://predictivelabs.ai)"})
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as r:
        return r.read().decode("utf-8", "replace").strip()


def lookup_country(ip: str) -> str | None:
    now = time.time()
    hit = _CACHE.get(ip)
    if hit and now - hit[0] < _TTL:
        return hit[1]
    country = None
    try:
        txt = _get(f"https://ipapi.co/{ip}/country_code/")
        if len(txt) == 2 and txt.isalpha():
            country = txt.lower()
    except Exception as e:  # noqa: BLE001
        logger.debug("ipapi.co failed %s: %s", ip, e)
    if country is None:
        try:
            data = json.loads(_get(f"http://ip-api.com/json/{ip}?fields=status,countryCode"))
            if data.get("status") == "success" and data.get("countryCode"):
                country = str(data["countryCode"]).lower()
        except Exception as e:  # noqa: BLE001
            logger.debug("ip-api.com failed %s: %s", ip, e)
    if country is None:
        for cc, prefixes in _EMERGENCY_PREFIXES.items():
            if ip.startswith(prefixes):
                country = cc
                break
    _CACHE[ip] = (now, country)
    if len(_CACHE) > 4096:
        for k, _ in sorted(_CACHE.items(), key=lambda kv: kv[1][0])[:1024]:
            _CACHE.pop(k, None)
    return country


def detect_country(request) -> str | None:
    """ISO country (lower) or None. Never raises."""
    if request is None:
        return None
    try:
        for key in COUNTRY_HEADERS:
            raw = (request.headers.get(key) or "").strip().lower()
            if len(raw) == 2 and raw not in ("xx", "t1"):
                return raw
        ip = client_ip(request)
        if not ip or _private(ip):
            return None
        if not _api_enabled():
            for cc, prefixes in _EMERGENCY_PREFIXES.items():
                if ip.startswith(prefixes):
                    return cc
            return None
        return lookup_country(ip)
    except Exception:
        return None


def country_lang(code: str | None) -> str | None:
    return COUNTRY_LANG.get((code or "").lower())
