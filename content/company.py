"""Public legal entities and registered addresses."""

LEGAL_REGIONS = ("EMEA", "Americas", "APAC")

LEGAL_ENTITIES = (
    {
        "region": "EMEA",
        "market": "United Kingdom",
        "entity": "Predictive Labs Ltd · Co. 14857334 · D-U-N-S© Number: 230619730",
        "address": "155 Minories Street, Suite 275, London EC3N 1AD",
    },
    {
        "region": "EMEA",
        "market": "Lithuania",
        "entity": "Predictive Labs, UAB · Reg. 307863496",
        "address": "Medeinos g. 35-70, Vilnius LT-06137",
    },
    {
        "region": "EMEA",
        "market": "Estonia",
        "entity": "Predictive Labs OÜ · Registry 12061679",
        "address": "Ravala 6, Tallinn",
    },
    {
        "region": "Americas",
        "market": "Canada",
        "entity": "Predictive Labs Inc. · OCN 1001679945",
        "address": "155 East Beaver Creek Road, Suite 24-147, Richmond Hill, Ontario L4B 2N1",
    },
    {
        "region": "Americas",
        "market": "United States",
        "entity": "Predictive Labs LLC · ID 2025-001721250",
        "address": "1331 Grand Street, Suite 607, Hoboken, NJ 07030",
    },
    {
        "region": "APAC",
        "market": "New Zealand",
        "entity": "Predictive Labs Limited · Co. 9448513 · NZBN 9429053855695",
        "address": "19E Lomond Street, Takapuna, Auckland 0622",
    },
)


# Local entity shown first and named in the copyright on that language's site.
LOCAL_ENTITY = {"lt": "Lithuania", "et": "Estonia"}
COPYRIGHT = {"lt": "UAB „Predictive Labs“ (įmonės kodas 307863496)", "et": "Predictive Labs OÜ"}


def entities_for(lang: str = "en"):
    market = LOCAL_ENTITY.get(lang)
    if not market:
        return LEGAL_ENTITIES
    return tuple(sorted(LEGAL_ENTITIES, key=lambda e: e["market"] != market))


def copyright_holder(lang: str = "en") -> str:
    return COPYRIGHT.get(lang, "Predictive Labs Ltd.")
