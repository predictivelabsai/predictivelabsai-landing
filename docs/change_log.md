# Change log

## 2026-10-11 — All target languages (phase 2)
- Published languages (geo + hreflang): en, lt, et, lv, fi, sv, no (hreflang nb), da, de, fr, pt, es, pl.
  UK/US/IE/CA/AU/NZ stay English; nl remains switcher-only.
- ccTLDs: predictivelabs.lt -> lt, predictivelabs.ee -> et (Predictive Labs OÜ shown first).
  EE visitors on .ai get the same one-time, human-only redirect to .ee as LT -> .lt.
- Countries without a live ccTLD are served on predictivelabs.ai in their language
  (geo for humans) with crawlable locale URLs `?lang=xx` used as hreflang alternates/canonical.
- New Portuguese (pt-PT) and Spanish catalogs; repo/app-suite/partner/market-name
  translations for all languages (`utils/locales/`). Language menu lists .ai/.lt/.ee domain links.

## 2026-10-11 — Lithuanian site on predictivelabs.lt (geo + domain i18n)
- New `utils/domains.py` (ccTLD -> language, hreflang/canonical, geo-redirect map) and
  `utils/geo.py` (country from CF-IPCountry/X-Country-Code headers, else cached ipapi.co /
  ip-api.com lookup, else Baltic IP-prefix fallback) — same pattern as CityTicker.
- Language precedence: `?lang=` > manual choice (session, per host) > ccTLD > visitor country > en.
- Human LT visitors on predictivelabs.ai get one 302 to predictivelabs.lt (same path/query).
  Never for bots, ccTLDs, POSTs/static, `?stay=1`, `?lang=`, or after a manual choice
  (`pl_stay` cookie) — no loops. `PL_GEO_REDIRECT=off` disables.
- Canonical + hreflang (en -> .ai, lt -> .lt, x-default -> .ai) injected on every page;
  .eu / .co.uk canonicalise to .ai.
- Full Lithuanian copy: editorial revision of the LT catalog, plus translations for repo,
  app-suite, partner and legal-entity text (`utils/content_i18n.py`). LT site lists
  UAB „Predictive Labs“ (įmonės kodas 307863496) first and in the copyright line.
- Language menu gains an explicit predictivelabs.ai / predictivelabs.lt domain switch.
- Tests: `tests/test_geo_i18n.py` (simulated country header, bots, loops, hreflang).

