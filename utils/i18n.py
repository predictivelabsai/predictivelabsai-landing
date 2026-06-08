"""Internationalisation — session-based language with IP detection.

Same 12 languages as plai/kanvas:
en (English), et (Estonian), de (German), fr (French), sv (Swedish),
lv (Latvian), no (Norwegian), da (Danish), pl (Polish),
nl (Dutch), fi (Finnish), lt (Lithuanian).
"""

from __future__ import annotations

from typing import Any

DEFAULT_LANG = "en"

LANGUAGES: dict[str, dict] = {
    "en": {"name": "English",    "native": "English",    "flag": "\U0001f1ec\U0001f1e7"},
    "et": {"name": "Estonian",   "native": "Eesti",      "flag": "\U0001f1ea\U0001f1ea"},
    "de": {"name": "German",     "native": "Deutsch",    "flag": "\U0001f1e9\U0001f1ea"},
    "fr": {"name": "French",     "native": "Français", "flag": "\U0001f1eb\U0001f1f7"},
    "sv": {"name": "Swedish",    "native": "Svenska",    "flag": "\U0001f1f8\U0001f1ea"},
    "lv": {"name": "Latvian",    "native": "Latviešu", "flag": "\U0001f1f1\U0001f1fb"},
    "no": {"name": "Norwegian",  "native": "Norsk",      "flag": "\U0001f1f3\U0001f1f4"},
    "da": {"name": "Danish",     "native": "Dansk",      "flag": "\U0001f1e9\U0001f1f0"},
    "pl": {"name": "Polish",     "native": "Polski",     "flag": "\U0001f1f5\U0001f1f1"},
    "nl": {"name": "Dutch",      "native": "Nederlands", "flag": "\U0001f1f3\U0001f1f1"},
    "fi": {"name": "Finnish",    "native": "Suomi",      "flag": "\U0001f1eb\U0001f1ee"},
    "lt": {"name": "Lithuanian", "native": "Lietuvių",  "flag": "\U0001f1f1\U0001f1f9"},
}

SUPPORTED_LANGS = set(LANGUAGES.keys())

_ESTONIAN_IP_PREFIXES = (
    "85.253.", "90.190.", "84.50.", "213.168.", "195.50.",
    "62.65.", "88.196.", "86.43.", "193.40.", "194.126.",
)
_LATVIAN_IP_PREFIXES = (
    "195.13.", "213.175.", "195.122.", "80.233.", "78.84.",
)
_LITHUANIAN_IP_PREFIXES = (
    "82.135.", "78.56.", "78.57.", "78.58.", "78.60.",
    "78.61.", "78.62.", "78.63.", "213.252.",
)


def _get_client_ip(request) -> str:
    forwarded = (getattr(request, "headers", {}) or {}).get("x-forwarded-for", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    client = getattr(request, "client", None)
    return client.host if client else ""


def detect_language(request) -> str:
    ip = _get_client_ip(request)
    if any(ip.startswith(p) for p in _ESTONIAN_IP_PREFIXES):
        return "et"
    if any(ip.startswith(p) for p in _LATVIAN_IP_PREFIXES):
        return "lv"
    if any(ip.startswith(p) for p in _LITHUANIAN_IP_PREFIXES):
        return "lt"
    return DEFAULT_LANG


def get_lang(sess: dict[str, Any], request=None) -> str:
    lang = (sess.get("lang") or "").lower()
    if lang in SUPPORTED_LANGS:
        return lang
    if request:
        detected = detect_language(request)
        sess["lang"] = detected
        return detected
    return DEFAULT_LANG


def set_lang(sess: dict[str, Any], lang: str) -> str:
    code = (lang or "").lower()
    if code in SUPPORTED_LANGS:
        sess["lang"] = code
    return get_lang(sess)


def t(key: str, lang: str = DEFAULT_LANG) -> str:
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key
    return entry.get(lang, entry.get("en", key))


# ---------------------------------------------------------------------------
# Translation catalog
# ---------------------------------------------------------------------------

TRANSLATIONS: dict[str, dict[str, str]] = {

    # ── Navigation ────────────────────────────────────────────
    "nav_platform": {
        "en": "Platform", "et": "Platvorm", "de": "Plattform",
        "fr": "Plateforme", "sv": "Plattform", "lv": "Platforma",
        "no": "Plattform", "da": "Platform", "pl": "Platforma",
        "nl": "Platform", "fi": "Alusta", "lt": "Platforma",
    },
    "nav_solutions": {
        "en": "Solutions", "et": "Lahendused", "de": "Lösungen",
        "fr": "Solutions", "sv": "Lösningar", "lv": "Risinājumi",
        "no": "Løsninger", "da": "Løsninger", "pl": "Rozwiązania",
        "nl": "Oplossingen", "fi": "Ratkaisut", "lt": "Sprendimai",
    },
    "nav_case_studies": {
        "en": "Case studies", "et": "Juhtumiuuringud", "de": "Fallstudien",
        "fr": "Études de cas", "sv": "Fallstudier", "lv": "Gadījumu izpētes",
        "no": "Casestudier", "da": "Casestudier", "pl": "Studia przypadków",
        "nl": "Casestudies", "fi": "Tapaustutkimukset", "lt": "Atvejų analizės",
    },
    "nav_signal": {
        "en": "Signal", "et": "Signaal", "de": "Signal",
        "fr": "Signal", "sv": "Signal", "lv": "Signāls",
        "no": "Signal", "da": "Signal", "pl": "Sygnał",
        "nl": "Signaal", "fi": "Signaali", "lt": "Signalas",
    },
    "nav_research": {
        "en": "Research", "et": "Teadus", "de": "Forschung",
        "fr": "Recherche", "sv": "Forskning", "lv": "Pētniecība",
        "no": "Forskning", "da": "Forskning", "pl": "Badania",
        "nl": "Onderzoek", "fi": "Tutkimus", "lt": "Tyrimai",
    },
    "nav_thesis": {
        "en": "Thesis", "et": "Tees", "de": "These",
        "fr": "Thèse", "sv": "Tes", "lv": "Tēze",
        "no": "Tese", "da": "Tese", "pl": "Teza",
        "nl": "These", "fi": "Teesi", "lt": "Tezė",
    },
    "nav_team": {
        "en": "Team", "et": "Meeskond", "de": "Team",
        "fr": "Équipe", "sv": "Team", "lv": "Komanda",
        "no": "Team", "da": "Team", "pl": "Zespół",
        "nl": "Team", "fi": "Tiimi", "lt": "Komanda",
    },
    "nav_contact": {
        "en": "Contact", "et": "Kontakt", "de": "Kontakt",
        "fr": "Contact", "sv": "Kontakt", "lv": "Kontakti",
        "no": "Kontakt", "da": "Kontakt", "pl": "Kontakt",
        "nl": "Contact", "fi": "Yhteystiedot", "lt": "Kontaktai",
    },
    "nav_talk_to_us": {
        "en": "Talk to us", "et": "Räägi meiega", "de": "Kontaktieren Sie uns",
        "fr": "Contactez-nous", "sv": "Prata med oss", "lv": "Sazināties ar mums",
        "no": "Snakk med oss", "da": "Tal med os", "pl": "Porozmawiaj z nami",
        "nl": "Praat met ons", "fi": "Ota yhteyttä", "lt": "Susisiekite",
    },

    # ── Solutions sub-nav ────────────────────────────────────
    "nav_sol_defense": {
        "en": "Defense & public security", "et": "Riigikaitse ja avalik julgeolek",
        "de": "Verteidigung & öffentliche Sicherheit", "fr": "Défense & sécurité publique",
        "sv": "Försvar & allmän säkerhet", "lv": "Aizsardzība un sabiedriskā drošība",
        "no": "Forsvar og offentlig sikkerhet", "da": "Forsvar og offentlig sikkerhed",
        "pl": "Obronność i bezpieczeństwo publiczne", "nl": "Defensie & openbare veiligheid",
        "fi": "Puolustus ja yleinen turvallisuus", "lt": "Gynyba ir viešasis saugumas",
    },
    "nav_sol_health": {
        "en": "Health & life sciences", "et": "Tervishoid ja bioteadused",
        "de": "Gesundheit & Biowissenschaften", "fr": "Santé & sciences de la vie",
        "sv": "Hälsa & livsvetenskap", "lv": "Veselība un dzīvības zinātnes",
        "no": "Helse og biovitenskap", "da": "Sundhed og biovidenskab",
        "pl": "Zdrowie i nauki przyrodnicze", "nl": "Gezondheid & levenswetenschappen",
        "fi": "Terveys ja biotieteet", "lt": "Sveikata ir gyvybės mokslai",
    },
    "nav_sol_public": {
        "en": "Public management & mobility", "et": "Avalik haldus ja liikuvus",
        "de": "Öffentliche Verwaltung & Mobilität", "fr": "Gestion publique & mobilité",
        "sv": "Offentlig förvaltning & mobilitet", "lv": "Publiskā pārvalde un mobilitāte",
        "no": "Offentlig forvaltning og mobilitet", "da": "Offentlig forvaltning og mobilitet",
        "pl": "Zarządzanie publiczne i mobilność", "nl": "Publiek beheer & mobiliteit",
        "fi": "Julkishallinto ja liikkuvuus", "lt": "Viešasis valdymas ir mobilumas",
    },
    "nav_sol_financial": {
        "en": "Financial services", "et": "Finantsteenused", "de": "Finanzdienstleistungen",
        "fr": "Services financiers", "sv": "Finansiella tjänster", "lv": "Finanšu pakalpojumi",
        "no": "Finansielle tjenester", "da": "Finansielle tjenester", "pl": "Usługi finansowe",
        "nl": "Financiële diensten", "fi": "Rahoituspalvelut", "lt": "Finansinės paslaugos",
    },

    # ── Footer ────────────────────────────────────────────────
    "footer_platform": {
        "en": "Platform", "et": "Platvorm", "de": "Plattform",
        "fr": "Plateforme", "sv": "Plattform", "lv": "Platforma",
        "no": "Plattform", "da": "Platform", "pl": "Platforma",
        "nl": "Platform", "fi": "Alusta", "lt": "Platforma",
    },
    "footer_solutions": {
        "en": "Solutions", "et": "Lahendused", "de": "Lösungen",
        "fr": "Solutions", "sv": "Lösningar", "lv": "Risinājumi",
        "no": "Løsninger", "da": "Løsninger", "pl": "Rozwiązania",
        "nl": "Oplossingen", "fi": "Ratkaisut", "lt": "Sprendimai",
    },
    "footer_company": {
        "en": "Company", "et": "Ettevõte", "de": "Unternehmen",
        "fr": "Entreprise", "sv": "Företag", "lv": "Uzņēmums",
        "no": "Selskap", "da": "Virksomhed", "pl": "Firma",
        "nl": "Bedrijf", "fi": "Yritys", "lt": "Įmonė",
    },
    "footer_overview": {
        "en": "Overview", "et": "Ülevaade", "de": "Übersicht",
        "fr": "Aperçu", "sv": "Översikt", "lv": "Pārskats",
        "no": "Oversikt", "da": "Oversigt", "pl": "Przegląd",
        "nl": "Overzicht", "fi": "Yleiskatsaus", "lt": "Apžvalga",
    },

    # ── CTA Section ───────────────────────────────────────────
    "cta_engage": {
        "en": "Engage", "et": "Kaasa", "de": "Kontaktieren",
        "fr": "Engager", "sv": "Engagera", "lv": "Iesaistīties",
        "no": "Engasjer", "da": "Engager", "pl": "Zaangażuj",
        "nl": "Contact", "fi": "Ota yhteyttä", "lt": "Įsitraukite",
    },
    "cta_headline": {
        "en": "Brief us on your programme.", "et": "Tutvustage meile oma programmi.",
        "de": "Briefen Sie uns zu Ihrem Programm.", "fr": "Présentez-nous votre programme.",
        "sv": "Berätta om ert program.", "lv": "Pastāstiet mums par savu programmu.",
        "no": "Fortell oss om programmet ditt.", "da": "Fortæl os om jeres program.",
        "pl": "Przedstaw nam swój program.", "nl": "Vertel ons over uw programma.",
        "fi": "Kerro meille ohjelmastasi.", "lt": "Papasakokite apie savo programą.",
    },
    "cta_body": {
        "en": "We work with public-sector buyers in the UK, the Nordics, the Benelux and the Baltics. Tell us the problem — we'll tell you if we can help.",
        "et": "Töötame avaliku sektori tellijatega Ühendkuningriigis, Põhjamaades, Beneluxi riikides ja Baltikumis. Kirjeldage probleemi — me ütleme, kas saame aidata.",
        "de": "Wir arbeiten mit öffentlichen Auftraggebern in Großbritannien, Skandinavien, den Benelux-Staaten und dem Baltikum. Schildern Sie das Problem — wir sagen Ihnen, ob wir helfen können.",
        "fr": "Nous travaillons avec des acheteurs du secteur public au Royaume-Uni, dans les pays nordiques, au Benelux et dans les pays baltes. Décrivez le problème — nous vous dirons si nous pouvons aider.",
        "sv": "Vi arbetar med offentliga beställare i Storbritannien, Norden, Benelux och Baltikum. Beskriv problemet — vi säger om vi kan hjälpa.",
        "lv": "Mēs strādājam ar publiskā sektora pasūtītājiem Lielbritānijā, Ziemeļvalstīs, Beniluksa valstīs un Baltijā. Pastāstiet par problēmu — mēs pateiksim, vai varam palīdzēt.",
        "no": "Vi jobber med offentlige oppdragsgivere i Storbritannia, Norden, Benelux og Baltikum. Fortell oss problemet — vi sier fra om vi kan hjelpe.",
        "da": "Vi arbejder med offentlige indkøbere i Storbritannien, Norden, Benelux og Baltikum. Fortæl os problemet — vi siger, om vi kan hjælpe.",
        "pl": "Współpracujemy z zamawiającymi z sektora publicznego w Wielkiej Brytanii, krajach nordyckich, Beneluksie i krajach bałtyckich. Opisz problem — powiemy, czy możemy pomóc.",
        "nl": "Wij werken met publieke opdrachtgevers in het VK, Scandinavië, de Benelux en het Balticum. Beschrijf het probleem — wij vertellen of we kunnen helpen.",
        "fi": "Työskentelemme julkisen sektorin tilaajien kanssa Isossa-Britanniassa, Pohjoismaissa, Benelux-maissa ja Baltiassa. Kerro ongelma — me kerromme, voimmeko auttaa.",
        "lt": "Dirbame su viešojo sektoriaus pirkėjais JK, Šiaurės šalyse, Beneliukse ir Baltijos šalyse. Apibūdinkite problemą — pasakysime, ar galime padėti.",
    },
    "cta_start": {
        "en": "Start the conversation", "et": "Alusta vestlust", "de": "Gespräch beginnen",
        "fr": "Engager la conversation", "sv": "Starta samtalet", "lv": "Sākt sarunu",
        "no": "Start samtalen", "da": "Start samtalen", "pl": "Rozpocznij rozmowę",
        "nl": "Start het gesprek", "fi": "Aloita keskustelu", "lt": "Pradėkite pokalbį",
    },
    "cta_see_cases": {
        "en": "See case studies", "et": "Vaata juhtumiuuringuid", "de": "Fallstudien ansehen",
        "fr": "Voir les études de cas", "sv": "Se fallstudier", "lv": "Skatīt gadījumu izpētes",
        "no": "Se casestudier", "da": "Se casestudier", "pl": "Zobacz studia przypadków",
        "nl": "Bekijk casestudies", "fi": "Katso tapaustutkimukset", "lt": "Žiūrėti atvejų analizes",
    },

    # ── Home page ─────────────────────────────────────────────
    "home_eyebrow": {
        "en": "AI for public outcomes", "et": "Tehisintellekt avalike tulemuste nimel",
        "de": "KI für öffentliche Ergebnisse", "fr": "IA pour les résultats publics",
        "sv": "AI för offentliga resultat", "lv": "MI publiskiem rezultātiem",
        "no": "KI for offentlige resultater", "da": "AI for offentlige resultater",
        "pl": "AI dla wyników publicznych", "nl": "AI voor publieke resultaten",
        "fi": "Tekoäly julkisten tulosten hyväksi", "lt": "DI viešiesiems rezultatams",
    },
    "home_headline_1": {
        "en": "Decisions made ", "et": "Otsused, mis põhinevad ",
        "de": "Entscheidungen auf ", "fr": "Des décisions fondées sur ",
        "sv": "Beslut grundade på ", "lv": "Lēmumi, kas balstīti uz ",
        "no": "Beslutninger basert på ", "da": "Beslutninger baseret på ",
        "pl": "Decyzje oparte na ", "nl": "Beslissingen op basis van ",
        "fi": "Päätökset perustuen ", "lt": "Sprendimai, priimti ",
    },
    "home_headline_2": {
        "en": "with evidence,", "et": "tõenditel,",
        "de": "Grundlage von Evidenz,", "fr": "des preuves,",
        "sv": "evidens,", "lv": "pierādījumiem,",
        "no": "evidens,", "da": "evidens,",
        "pl": "dowodach,", "nl": "bewijs,",
        "fi": "näyttöön,", "lt": "įrodymų pagrindu,",
    },
    "home_headline_3": {
        "en": " at the scale of the public good.", "et": " ühiskondliku hüve ulatuses.",
        "de": " im Maßstab des Gemeinwohls.", "fr": " à l'échelle de l'intérêt public.",
        "sv": " i samhällsnyttans skala.", "lv": " sabiedriskā labuma mērogā.",
        "no": " i offentlighetens interesse.", "da": " i den offentlige interesses skala.",
        "pl": " w skali dobra publicznego.", "nl": " op de schaal van het publieke belang.",
        "fi": " julkisen edun mittakaavassa.", "lt": " viešosios gerovės mastu.",
    },
    "home_lede": {
        "en": "Predictive Labs builds AI systems for European public services — in health, defense, public management and mobility — that are auditable by design and open where they can be.",
        "et": "Predictive Labs ehitab tehisintellekti süsteeme Euroopa avalike teenuste jaoks — tervishoius, riigikaitses, avalikus halduses ja liikuvuses — mis on kavandatud auditeeritavatena ja avatud seal, kus võimalik.",
        "de": "Predictive Labs entwickelt KI-Systeme für europäische öffentliche Dienste — in Gesundheit, Verteidigung, öffentlicher Verwaltung und Mobilität — die von Grund auf prüfbar und offen sind, wo es möglich ist.",
        "fr": "Predictive Labs construit des systèmes d'IA pour les services publics européens — santé, défense, gestion publique et mobilité — auditables par conception et ouverts dans la mesure du possible.",
        "sv": "Predictive Labs bygger AI-system för europeiska offentliga tjänster — inom hälsa, försvar, offentlig förvaltning och mobilitet — som är granskningsbara genom design och öppna där det är möjligt.",
        "lv": "Predictive Labs veido MI sistēmas Eiropas sabiedriskajiem pakalpojumiem — veselībā, aizsardzībā, publiskajā pārvaldē un mobilitātē — kas ir pārbaudāmas pēc būtības un atvērtas, kur iespējams.",
        "no": "Predictive Labs bygger KI-systemer for europeiske offentlige tjenester — innen helse, forsvar, offentlig forvaltning og mobilitet — som er reviderbare fra utformingen og åpne der det er mulig.",
        "da": "Predictive Labs bygger AI-systemer til europæiske offentlige tjenester — inden for sundhed, forsvar, offentlig forvaltning og mobilitet — der er reviderbare fra design og åbne, hvor det er muligt.",
        "pl": "Predictive Labs buduje systemy AI dla europejskich usług publicznych — w zdrowiu, obronności, zarządzaniu publicznym i mobilności — które są audytowalne z założenia i otwarte tam, gdzie to możliwe.",
        "nl": "Predictive Labs bouwt AI-systemen voor Europese overheidsdiensten — in gezondheid, defensie, openbaar bestuur en mobiliteit — die controleerbaar zijn door ontwerp en open waar mogelijk.",
        "fi": "Predictive Labs rakentaa tekoälyjärjestelmiä eurooppalaisille julkisille palveluille — terveydenhuollossa, puolustuksessa, julkishallinnossa ja liikkuvuudessa — jotka ovat suunnitelmallisesti tarkastettavia ja avoimia mahdollisuuksien mukaan.",
        "lt": "Predictive Labs kuria DI sistemas Europos viešosioms paslaugoms — sveikatos, gynybos, viešojo valdymo ir mobilumo srityse — kurios yra audituojamos pagal dizainą ir atviros ten, kur įmanoma.",
    },
    "home_cta_see": {
        "en": "See what we build", "et": "Vaata, mida ehitame", "de": "Sehen Sie, was wir bauen",
        "fr": "Voir ce que nous construisons", "sv": "Se vad vi bygger", "lv": "Skatīt, ko mēs veidojam",
        "no": "Se hva vi bygger", "da": "Se, hvad vi bygger", "pl": "Zobacz, co budujemy",
        "nl": "Zie wat we bouwen", "fi": "Katso mitä rakennamme", "lt": "Žiūrėkite, ką kuriame",
    },
    "home_precedent": {
        "en": "Precedent", "et": "Kogemus", "de": "Referenz",
        "fr": "Références", "sv": "Referens", "lv": "Pieredze",
        "no": "Referanse", "da": "Reference", "pl": "Doświadczenie",
        "nl": "Referentie", "fi": "Kokemus", "lt": "Patirtis",
    },
    "home_precedent_heading": {
        "en": "Delivered inside institutions that take correctness seriously.",
        "et": "Tarnitud asutustes, mis suhtuvad korrektsusesse tõsiselt.",
        "de": "Geliefert in Institutionen, die Korrektheit ernst nehmen.",
        "fr": "Livré au sein d'institutions qui prennent la rigueur au sérieux.",
        "sv": "Levererat inom institutioner som tar korrekthet på allvar.",
        "lv": "Piegādāts iestādēs, kas nopietni izturas pret precizitāti.",
        "no": "Levert i institusjoner som tar korrekthet på alvor.",
        "da": "Leveret i institutioner, der tager korrekthed alvorligt.",
        "pl": "Dostarczone instytucjom, które traktują poprawność poważnie.",
        "nl": "Geleverd bij instellingen die correctheid serieus nemen.",
        "fi": "Toimitettu organisaatioille, jotka suhtautuvat oikeellisuuteen vakavasti.",
        "lt": "Pristatyta institucijoms, kurios rimtai žiūri į tikslumą.",
    },
    "home_capabilities": {
        "en": "Capabilities", "et": "Võimekused", "de": "Fähigkeiten",
        "fr": "Capacités", "sv": "Kapabiliteter", "lv": "Spējas",
        "no": "Kapabiliteter", "da": "Kapabiliteter", "pl": "Możliwości",
        "nl": "Capaciteiten", "fi": "Kyvykkyydet", "lt": "Gebėjimai",
    },
    "home_cap_heading": {
        "en": "Four capabilities, composed to fit the programme.",
        "et": "Neli võimekust, mis kohandatakse programmi järgi.",
        "de": "Vier Fähigkeiten, zusammengestellt passend zum Programm.",
        "fr": "Quatre capacités, composées pour s'adapter au programme.",
        "sv": "Fyra kapabiliteter, komponerade efter programmet.",
        "lv": "Četras spējas, sakārtotas atbilstoši programmai.",
        "no": "Fire kapabiliteter, satt sammen for programmet.",
        "da": "Fire kapabiliteter, sammensat til programmet.",
        "pl": "Cztery możliwości, dopasowane do programu.",
        "nl": "Vier capaciteiten, samengesteld passend bij het programma.",
        "fi": "Neljä kyvykkyyttä, suunniteltu ohjelman mukaan.",
        "lt": "Keturi gebėjimai, sukomponuoti pagal programą.",
    },
    "home_cap_body": {
        "en": "We don't ship a platform. We ship a team that brings a platform's discipline to every engagement — reproducible pipelines, versioned models, inspectable prompts, open code where the law and the contract allow.",
        "et": "Me ei tarni platvormi. Me tarnime meeskonna, mis toob platvormi distsipliini igasse projekti — reprodutseeritavad torujuhtmed, versioonitud mudelid, kontrollitavad vihjed, avatud kood seal, kus seadus ja leping lubavad.",
        "de": "Wir liefern keine Plattform. Wir liefern ein Team, das die Disziplin einer Plattform in jedes Projekt bringt — reproduzierbare Pipelines, versionierte Modelle, überprüfbare Prompts, offener Code, wo Gesetz und Vertrag es erlauben.",
        "fr": "Nous ne fournissons pas une plateforme. Nous fournissons une équipe qui apporte la discipline d'une plateforme à chaque engagement — pipelines reproductibles, modèles versionnés, prompts inspectables, code ouvert là où la loi et le contrat le permettent.",
        "sv": "Vi levererar inte en plattform. Vi levererar ett team som medför en plattforms disciplin till varje uppdrag — reproducerbara pipelines, versionshanterade modeller, inspekterbara prompts, öppen kod där lag och avtal tillåter.",
        "lv": "Mēs nepiegādājam platformu. Mēs piegādājam komandu, kas nodrošina platformas disciplīnu katrā projektā — reproducējamas cauruļvadus, versiju pārvaldītus modeļus, pārbaudāmus norādījumus, atvērtu kodu, kur likums un līgums to atļauj.",
        "no": "Vi leverer ikke en plattform. Vi leverer et team som bringer en plattforms disiplin til hvert oppdrag — reproduserbare pipelines, versjonerte modeller, inspiserbare prompts, åpen kode der lov og kontrakt tillater det.",
        "da": "Vi leverer ikke en platform. Vi leverer et team, der bringer en platforms disciplin til hvert engagement — reproducerbare pipelines, versionerede modeller, inspicerbare prompts, åben kode, hvor lov og kontrakt tillader det.",
        "pl": "Nie dostarczamy platformy. Dostarczamy zespół, który wnosi dyscyplinę platformy do każdego projektu — powtarzalne potoki, wersjonowane modele, kontrolowalne prompty, otwarty kod tam, gdzie prawo i umowa na to pozwalają.",
        "nl": "Wij leveren geen platform. Wij leveren een team dat de discipline van een platform meebrengt naar elk project — reproduceerbare pipelines, geversioneerde modellen, controleerbare prompts, open code waar wet en contract het toestaan.",
        "fi": "Emme toimita alustaa. Toimitamme tiimin, joka tuo alustan kurinalaisuuden jokaiseen projektiin — toistettavat putkilinjat, versioidut mallit, tarkastettavat kehotteet, avoin koodi lain ja sopimuksen sallimissa rajoissa.",
        "lt": "Mes netiekiame platformos. Tiekiame komandą, kuri atneša platformos discipliną į kiekvieną projektą — atkuriamus vamzdynus, versijuotus modelius, tikrinamus raginimus, atvirą kodą ten, kur leidžia įstatymas ir sutartis.",
    },
    "home_where": {
        "en": "Where we work", "et": "Kus me töötame", "de": "Wo wir arbeiten",
        "fr": "Où nous travaillons", "sv": "Där vi arbetar", "lv": "Kur mēs strādājam",
        "no": "Hvor vi jobber", "da": "Hvor vi arbejder", "pl": "Gdzie pracujemy",
        "nl": "Waar we werken", "fi": "Missä työskentelemme", "lt": "Kur dirbame",
    },
    "home_where_heading": {
        "en": "Built around four public-sector programmes — and one commercial root.",
        "et": "Üles ehitatud nelja avaliku sektori programmi ümber — ja ühe ärilise juurega.",
        "de": "Aufgebaut um vier Programme des öffentlichen Sektors — und eine kommerzielle Wurzel.",
        "fr": "Construit autour de quatre programmes du secteur public — et une racine commerciale.",
        "sv": "Byggt kring fyra offentliga sektorprogram — och en kommersiell rot.",
        "lv": "Veidots ap četrām publiskā sektora programmām — un vienu komerciālu sakni.",
        "no": "Bygget rundt fire offentlige sektorprogrammer — og én kommersiell rot.",
        "da": "Bygget omkring fire offentlige sektorprogrammer — og én kommerciel rod.",
        "pl": "Zbudowane wokół czterech programów sektora publicznego — i jednego korzenia komercyjnego.",
        "nl": "Opgebouwd rond vier programma's voor de publieke sector — en één commerciële wortel.",
        "fi": "Rakennettu neljän julkisen sektorin ohjelman ympärille — ja yksi kaupallinen juuri.",
        "lt": "Sukurta aplink keturias viešojo sektoriaus programas — ir vieną komercinę šaknį.",
    },
    "home_selected_work": {
        "en": "Selected work", "et": "Valitud tööd", "de": "Ausgewählte Arbeiten",
        "fr": "Travaux sélectionnés", "sv": "Utvalda arbeten", "lv": "Atlasītie darbi",
        "no": "Utvalgte arbeider", "da": "Udvalgte arbejder", "pl": "Wybrane prace",
        "nl": "Geselecteerd werk", "fi": "Valitut työt", "lt": "Pasirinkti darbai",
    },
    "home_selected_heading": {
        "en": "What the programmes look like.", "et": "Kuidas programmid välja näevad.",
        "de": "Wie die Programme aussehen.", "fr": "À quoi ressemblent les programmes.",
        "sv": "Hur programmen ser ut.", "lv": "Kā izskatās programmas.",
        "no": "Hvordan programmene ser ut.", "da": "Hvordan programmerne ser ud.",
        "pl": "Jak wyglądają programy.", "nl": "Hoe de programma's eruitzien.",
        "fi": "Miltä ohjelmat näyttävät.", "lt": "Kaip atrodo programos.",
    },
    "home_all_cases": {
        "en": "All case studies", "et": "Kõik juhtumiuuringud", "de": "Alle Fallstudien",
        "fr": "Toutes les études de cas", "sv": "Alla fallstudier", "lv": "Visas gadījumu izpētes",
        "no": "Alle casestudier", "da": "Alle casestudier", "pl": "Wszystkie studia przypadków",
        "nl": "Alle casestudies", "fi": "Kaikki tapaustutkimukset", "lt": "Visos atvejų analizės",
    },
    "home_signal_heading": {
        "en": "We read the data our clients work with — every day.",
        "et": "Loeme andmeid, millega meie kliendid töötavad — iga päev.",
        "de": "Wir lesen die Daten, mit denen unsere Kunden arbeiten — jeden Tag.",
        "fr": "Nous lisons les données avec lesquelles nos clients travaillent — chaque jour.",
        "sv": "Vi läser den data våra kunder arbetar med — varje dag.",
        "lv": "Mēs lasām datus, ar kuriem strādā mūsu klienti — katru dienu.",
        "no": "Vi leser dataene kundene våre jobber med — hver dag.",
        "da": "Vi læser de data, vores kunder arbejder med — hver dag.",
        "pl": "Czytamy dane, z którymi pracują nasi klienci — każdego dnia.",
        "nl": "Wij lezen de data waarmee onze klanten werken — elke dag.",
        "fi": "Luemme dataa, jonka kanssa asiakkaamme työskentelevät — joka päivä.",
        "lt": "Skaitome duomenis, su kuriais dirba mūsų klientai — kiekvieną dieną.",
    },
    "home_open_signal": {
        "en": "Open Signal", "et": "Ava Signaal", "de": "Signal öffnen",
        "fr": "Ouvrir Signal", "sv": "Öppna Signal", "lv": "Atvērt Signālu",
        "no": "Åpne Signal", "da": "Åbn Signal", "pl": "Otwórz Sygnał",
        "nl": "Signaal openen", "fi": "Avaa Signaali", "lt": "Atidaryti Signalą",
    },
    "home_news_title": {
        "en": "What's moving in AI and European public services.",
        "et": "Mis liigub tehisintellektis ja Euroopa avalikes teenustes.",
        "de": "Was sich in KI und europäischen öffentlichen Diensten bewegt.",
        "fr": "Ce qui bouge dans l'IA et les services publics européens.",
        "sv": "Vad som rör sig inom AI och europeiska offentliga tjänster.",
        "lv": "Kas notiek MI un Eiropas sabiedriskos pakalpojumos.",
        "no": "Hva som skjer innen KI og europeiske offentlige tjenester.",
        "da": "Hvad der sker inden for AI og europæiske offentlige tjenester.",
        "pl": "Co się dzieje w AI i europejskich usługach publicznych.",
        "nl": "Wat er beweegt in AI en Europese overheidsdiensten.",
        "fi": "Mitä tapahtuu tekoälyssä ja eurooppalaisissa julkisissa palveluissa.",
        "lt": "Kas vyksta DI ir Europos viešosiose paslaugose.",
    },
    "home_news_subtitle": {
        "en": "A rolling mix from AI, government, health, defence and financial-services feeds. Refreshed hourly; links open in a new tab.",
        "et": "Pidevalt uuenev segu tehisintellekti, valitsemise, tervishoiu, kaitse ja finantsteenuste voogudest. Värskendatakse iga tund; lingid avanevad uuel vahelehel.",
        "de": "Eine rollende Mischung aus KI-, Regierungs-, Gesundheits-, Verteidigungs- und Finanzdienstleistungs-Feeds. Stündlich aktualisiert; Links öffnen in neuem Tab.",
        "fr": "Un mélange continu de flux IA, gouvernement, santé, défense et services financiers. Actualisé toutes les heures ; les liens s'ouvrent dans un nouvel onglet.",
        "sv": "En rullande mix från AI-, regerings-, hälso-, försvars- och finanstjänstflöden. Uppdateras varje timme; länkar öppnas i ny flik.",
        "lv": "Pastāvīga ziņu sajaukums no MI, valdības, veselības, aizsardzības un finanšu pakalpojumu plūsmām. Atjaunināts katru stundu; saites atveras jaunā cilnē.",
        "no": "En rullerende blanding fra KI-, regjerings-, helse-, forsvars- og finanstjenestestrømmer. Oppdateres hver time; lenker åpnes i ny fane.",
        "da": "En rullende blanding fra AI-, regerings-, sundheds-, forsvars- og finanstjenestefeeds. Opdateres hver time; links åbner i ny fane.",
        "pl": "Ciągle aktualizowana mieszanka z kanałów AI, rządowych, zdrowia, obronności i usług finansowych. Odświeżane co godzinę; linki otwierają się w nowej karcie.",
        "nl": "Een doorlopende mix uit AI-, overheids-, gezondheids-, defensie- en financiële dienstverlening feeds. Elk uur vernieuwd; links openen in een nieuw tabblad.",
        "fi": "Jatkuva sekoitus tekoäly-, hallinto-, terveys-, puolustus- ja rahoituspalvelusyötteistä. Päivitetään tunneittain; linkit avautuvat uudessa välilehdessä.",
        "lt": "Nuolat atnaujinamas mišinys iš DI, vyriausybės, sveikatos, gynybos ir finansinių paslaugų kanalų. Atnaujinama kas valandą; nuorodos atsidaro naujame skirtuke.",
    },

    # ── Thesis page ───────────────────────────────────────────
    "thesis_eyebrow": {
        "en": "Thesis", "et": "Tees", "de": "These",
        "fr": "Thèse", "sv": "Tes", "lv": "Tēze",
        "no": "Tese", "da": "Tese", "pl": "Teza",
        "nl": "These", "fi": "Teesi", "lt": "Tezė",
    },
    "thesis_headline": {
        "en": "EU Open Source Strategy: key proposals for tech sovereignty.",
        "et": "EL-i avatud lähtekoodiga strateegia: peamised ettepanekud tehnoloogilise suveräänsuse tagamiseks.",
        "de": "EU-Open-Source-Strategie: Kernvorschläge für technologische Souveränität.",
        "fr": "Stratégie open source de l'UE : propositions clés pour la souveraineté technologique.",
        "sv": "EU:s strategi för öppen källkod: nyckelförslag för teknisk suveränitet.",
        "lv": "ES atvērtā pirmkoda stratēģija: galvenie priekšlikumi tehnoloģiskajai suverenitātei.",
        "no": "EUs åpen kildekode-strategi: nøkkelforslag for teknologisk suverenitet.",
        "da": "EU's open source-strategi: nøgleforslag for teknologisk suverænitet.",
        "pl": "Strategia open source UE: kluczowe propozycje dla suwerenności technologicznej.",
        "nl": "EU Open Source Strategie: kernvoorstellen voor technologische soevereiniteit.",
        "fi": "EU:n avoimen lähdekoodin strategia: avainteemat teknologiseen suvereniteetiin.",
        "lt": "ES atvirojo kodo strategija: pagrindiniai pasiūlymai technologiniam suverenitetui.",
    },
    "thesis_lede": {
        "en": "The European Commission has published its EU Open Source Strategy (June 2026) to reduce dependence on non-EU proprietary tech and strengthen control over critical digital infrastructure. The strategy takes a full lifecycle approach — from R&D and procurement to deployment and maintenance — to build a more resilient and competitive European open source ecosystem.",
        "et": "Euroopa Komisjon on avaldanud EL-i avatud lähtekoodiga strateegia (juuni 2026), et vähendada sõltuvust EL-i-välistest suletud tehnoloogiatest ja tugevdada kontrolli kriitilise digitaristu üle. Strateegia hõlmab kogu elutsüklit — teadus- ja arendustegevusest ning hangetest juurutamise ja hoolduseni — et luua vastupidavam ja konkurentsivõimelisem Euroopa avatud lähtekoodiga ökosüsteem.",
        "de": "Die Europäische Kommission hat ihre EU-Open-Source-Strategie (Juni 2026) veröffentlicht, um die Abhängigkeit von proprietärer Nicht-EU-Technologie zu verringern und die Kontrolle über kritische digitale Infrastruktur zu stärken. Die Strategie verfolgt einen Vollzyklus-Ansatz — von F&E und Beschaffung bis hin zu Bereitstellung und Wartung — um ein widerstandsfähigeres und wettbewerbsfähigeres europäisches Open-Source-Ökosystem aufzubauen.",
        "fr": "La Commission européenne a publié sa stratégie open source de l'UE (juin 2026) pour réduire la dépendance aux technologies propriétaires non européennes et renforcer le contrôle sur les infrastructures numériques critiques. La stratégie adopte une approche sur tout le cycle de vie — de la R&D et des marchés publics au déploiement et à la maintenance — pour construire un écosystème open source européen plus résilient et compétitif.",
        "sv": "Europeiska kommissionen har publicerat sin EU-strategi för öppen källkod (juni 2026) för att minska beroendet av icke-EU-proprietär teknik och stärka kontrollen över kritisk digital infrastruktur. Strategin tar ett helhetsperspektiv — från FoU och upphandling till driftsättning och underhåll — för att bygga ett mer motståndskraftigt och konkurrenskraftigt europeiskt ekosystem för öppen källkod.",
        "lv": "Eiropas Komisija ir publicējusi ES atvērtā pirmkoda stratēģiju (2026. gada jūnijs), lai samazinātu atkarību no ārpus-ES komerciālajām tehnoloģijām un stiprinātu kontroli pār kritisko digitālo infrastruktūru. Stratēģija aptver visu dzīves ciklu — no pētniecības un iepirkumiem līdz ieviešanai un uzturēšanai — lai veidotu noturīgāku un konkurētspējīgāku Eiropas atvērtā pirmkoda ekosistēmu.",
        "no": "Europakommisjonen har publisert sin EU-åpen kildekode-strategi (juni 2026) for å redusere avhengigheten av ikke-EU proprietær teknologi og styrke kontrollen over kritisk digital infrastruktur. Strategien tar en fullsyklustilegange — fra FoU og anskaffelse til utrulling og vedlikehold — for å bygge et mer motstandsdyktig og konkurransedyktig europeisk åpen kildekode-økosystem.",
        "da": "Europa-Kommissionen har offentliggjort sin EU open source-strategi (juni 2026) for at reducere afhængigheden af ikke-EU proprietær teknologi og styrke kontrollen over kritisk digital infrastruktur. Strategien tager en fuld livscyklustilgang — fra F&U og indkøb til implementering og vedligeholdelse — for at opbygge et mere modstandsdygtigt og konkurrencedygtigt europæisk open source-økosystem.",
        "pl": "Komisja Europejska opublikowała Strategię Open Source UE (czerwiec 2026), aby zmniejszyć zależność od pozaunijnych technologii zamkniętych i wzmocnić kontrolę nad krytyczną infrastrukturą cyfrową. Strategia obejmuje pełny cykl życia — od badań i zamówień publicznych po wdrożenie i utrzymanie — aby zbudować bardziej odporny i konkurencyjny europejski ekosystem open source.",
        "nl": "De Europese Commissie heeft haar EU Open Source Strategie (juni 2026) gepubliceerd om de afhankelijkheid van niet-EU propriëtaire technologie te verminderen en de controle over kritieke digitale infrastructuur te versterken. De strategie hanteert een benadering over de gehele levenscyclus — van O&O en inkoop tot implementatie en onderhoud — om een veerkrachtiger en concurrerender Europees open source ecosysteem op te bouwen.",
        "fi": "Euroopan komissio on julkaissut EU:n avoimen lähdekoodin strategian (kesäkuu 2026) vähentääkseen riippuvuutta EU:n ulkopuolisesta suljetusta teknologiasta ja vahvistaakseen hallintaa kriittisestä digitaalisesta infrastruktuurista. Strategia kattaa koko elinkaaren — T&K:sta ja hankinnoista käyttöönottoon ja ylläpitoon — luodakseen kestävämmän ja kilpailukykyisemmän eurooppalaisen avoimen lähdekoodin ekosysteemin.",
        "lt": "Europos Komisija paskelbė ES atvirojo kodo strategiją (2026 m. birželis), siekdama sumažinti priklausomybę nuo ne ES nuosavybinių technologijų ir sustiprinti kontrolę virš kritinės skaitmeninės infrastruktūros. Strategija apima visą gyvavimo ciklą — nuo MTEP ir viešųjų pirkimų iki diegimo ir priežiūros — kad sukurtų atsparesnę ir konkurencingesnę Europos atvirojo kodo ekosistemą.",
    },
    "thesis_pill_sovereignty": {
        "en": "Tech sovereignty", "et": "Tehnoloogiline suveräänsus", "de": "Technologische Souveränität",
        "fr": "Souveraineté technologique", "sv": "Teknisk suveränitet", "lv": "Tehnoloģiskā suverenitāte",
        "no": "Teknologisk suverenitet", "da": "Teknologisk suverænitet", "pl": "Suwerenność technologiczna",
        "nl": "Technologische soevereiniteit", "fi": "Teknologinen suvereniteetti", "lt": "Technologinis suverenitetas",
    },
    "thesis_pill_opensource": {
        "en": "Open source", "et": "Avatud lähtekood", "de": "Open Source",
        "fr": "Open source", "sv": "Öppen källkod", "lv": "Atvērtais pirmkods",
        "no": "Åpen kildekode", "da": "Open source", "pl": "Open source",
        "nl": "Open source", "fi": "Avoin lähdekoodi", "lt": "Atvirasis kodas",
    },
    "thesis_pill_policy": {
        "en": "EU policy", "et": "EL-i poliitika", "de": "EU-Politik",
        "fr": "Politique UE", "sv": "EU-politik", "lv": "ES politika",
        "no": "EU-politikk", "da": "EU-politik", "pl": "Polityka UE",
        "nl": "EU-beleid", "fi": "EU-politiikka", "lt": "ES politika",
    },
    "thesis_proposals_eyebrow": {
        "en": "Key proposals", "et": "Peamised ettepanekud", "de": "Kernvorschläge",
        "fr": "Propositions clés", "sv": "Nyckelförslag", "lv": "Galvenie priekšlikumi",
        "no": "Nøkkelforslag", "da": "Nøgleforslag", "pl": "Kluczowe propozycje",
        "nl": "Kernvoorstellen", "fi": "Avainehdotukset", "lt": "Pagrindiniai pasiūlymai",
    },
    "thesis_proposals_heading": {
        "en": "Six pillars of the strategy.", "et": "Strateegia kuus sammast.",
        "de": "Sechs Säulen der Strategie.", "fr": "Six piliers de la stratégie.",
        "sv": "Sex pelare i strategin.", "lv": "Seši stratēģijas pīlāri.",
        "no": "Seks pilarer i strategien.", "da": "Seks søjler i strategien.",
        "pl": "Sześć filarów strategii.", "nl": "Zes pijlers van de strategie.",
        "fi": "Strategian kuusi pilaria.", "lt": "Šeši strategijos ramsčiai.",
    },
    "thesis_p1_title": {
        "en": "Scale the Open Internet Stack",
        "et": "Avatud interneti virna laiendamine",
        "de": "Den offenen Internet-Stack skalieren",
        "fr": "Mise à l'échelle de la pile Internet ouverte",
        "sv": "Skala upp den öppna internetstacken",
        "lv": "Atvērtā interneta steka mērogošana",
        "no": "Skalere den åpne internetstabelen",
        "da": "Skalering af den åbne internetstabel",
        "pl": "Skalowanie otwartego stosu internetowego",
        "nl": "De open internetstack opschalen",
        "fi": "Avoimen internet-pinon skaalaus",
        "lt": "Atvirojo interneto paketo plėtimas",
    },
    "thesis_p1_body": {
        "en": "A catalogue of EU-aligned open source solutions for cloud, workplace tools, secure email, and decentralised social media.",
        "et": "EL-iga kooskõlas olevate avatud lähtekoodiga lahenduste kataloog pilve, töökoha tööriistade, turvalise e-posti ja detsentraliseeritud sotsiaalmeedia jaoks.",
        "de": "Ein Katalog EU-konformer Open-Source-Lösungen für Cloud, Arbeitsplatztools, sichere E-Mail und dezentrale soziale Medien.",
        "fr": "Un catalogue de solutions open source alignées sur l'UE pour le cloud, les outils de travail, la messagerie sécurisée et les réseaux sociaux décentralisés.",
        "sv": "En katalog med EU-anpassade öppen-källkodslösningar för moln, arbetsplatsverktyg, säker e-post och decentraliserade sociala medier.",
        "lv": "ES prasībām atbilstošu atvērtā pirmkoda risinājumu katalogs mākoņiem, darbavietas rīkiem, drošam e-pastam un decentralizētiem sociālajiem medijiem.",
        "no": "En katalog over EU-tilpassede åpen kildekode-løsninger for sky, arbeidsplassverktøy, sikker e-post og desentraliserte sosiale medier.",
        "da": "Et katalog over EU-tilpassede open source-løsninger til cloud, arbejdspladsværktøjer, sikker e-mail og decentraliserede sociale medier.",
        "pl": "Katalog rozwiązań open source zgodnych z UE dla chmury, narzędzi pracy, bezpiecznej poczty e-mail i zdecentralizowanych mediów społecznościowych.",
        "nl": "Een catalogus van EU-conforme open source oplossingen voor cloud, werkplektools, beveiligde e-mail en gedecentraliseerde sociale media.",
        "fi": "EU-yhteensopivien avoimen lähdekoodin ratkaisujen luettelo pilvelle, työpaikkatyökaluille, turvalliselle sähköpostille ja hajautetulle sosiaaliselle medialle.",
        "lt": "ES suderintų atvirojo kodo sprendimų katalogas debesijoms, darbo vietų įrankiams, saugiam el. paštui ir decentralizuotoms socialinėms medijoms.",
    },
    "thesis_p2_title": {
        "en": "Prioritise public funding for open source",
        "et": "Avatud lähtekoodile avaliku rahastamise eelistamine",
        "de": "Öffentliche Finanzierung für Open Source priorisieren",
        "fr": "Prioriser le financement public de l'open source",
        "sv": "Prioritera offentlig finansiering av öppen källkod",
        "lv": "Prioritizēt publisko finansējumu atvērtajam pirmkodam",
        "no": "Prioritere offentlig finansiering for åpen kildekode",
        "da": "Prioritere offentlig finansiering af open source",
        "pl": "Priorytetowe finansowanie publiczne open source",
        "nl": "Publieke financiering voor open source prioriteren",
        "fi": "Julkisen rahoituksen priorisointi avoimelle lähdekoodille",
        "lt": "Viešojo finansavimo prioritetas atvirajam kodui",
    },
    "thesis_p2_body": {
        "en": "Development funding in semiconductors, operating systems, cloud/edge, AI, cybersecurity, and future internet architectures.",
        "et": "Arendusrahastus pooljuhtides, operatsioonisüsteemides, pilv/serva lahendused, tehisintellektis, küberturvalisuses ja tuleviku interneti arhitektuurides.",
        "de": "Entwicklungsfinanzierung in Halbleitern, Betriebssystemen, Cloud/Edge, KI, Cybersicherheit und zukünftigen Internetarchitekturen.",
        "fr": "Financement du développement dans les semi-conducteurs, les systèmes d'exploitation, cloud/edge, l'IA, la cybersécurité et les architectures internet futures.",
        "sv": "Utvecklingsfinansiering inom halvledare, operativsystem, moln/edge, AI, cybersäkerhet och framtida internetarkitekturer.",
        "lv": "Attīstības finansējums pusvadītājos, operētājsistēmās, mākoņa/malas tehnoloģijās, MI, kiberdrošībā un nākotnes interneta arhitektūrās.",
        "no": "Utviklingsfinansiering innen halvledere, operativsystemer, sky/edge, KI, cybersikkerhet og fremtidige internettarkitekturer.",
        "da": "Udviklingsfinansiering inden for halvledere, operativsystemer, cloud/edge, AI, cybersikkerhed og fremtidige internetarkitekturer.",
        "pl": "Finansowanie rozwoju w obszarze półprzewodników, systemów operacyjnych, cloud/edge, AI, cyberbezpieczeństwa i przyszłych architektur internetowych.",
        "nl": "Ontwikkelingsfinanciering in halfgeleiders, besturingssystemen, cloud/edge, AI, cybersecurity en toekomstige internetarchitecturen.",
        "fi": "Kehitysrahoitus puolijohteissa, käyttöjärjestelmissä, pilvi/reunalaskennassa, tekoälyssä, kyberturvallisuudessa ja tulevaisuuden internet-arkkitehtuureissa.",
        "lt": "Plėtros finansavimas puslaidininkiuose, operacinėse sistemose, debesyje/krašte, DI, kibernetiniame saugume ir ateities interneto architektūrose.",
    },
    "thesis_p3_title": {
        "en": "Open Source Maintenance Instrument",
        "et": "Avatud lähtekoodiga hoolduse instrument",
        "de": "Open-Source-Wartungsinstrument",
        "fr": "Instrument de maintenance open source",
        "sv": "Instrument för underhåll av öppen källkod",
        "lv": "Atvērtā pirmkoda uzturēšanas instruments",
        "no": "Vedlikeholdsinstrument for åpen kildekode",
        "da": "Open source-vedligeholdelsesinstrument",
        "pl": "Instrument utrzymania open source",
        "nl": "Open source onderhoudsinstrument",
        "fi": "Avoimen lähdekoodin ylläpitoinstrumentti",
        "lt": "Atvirojo kodo priežiūros instrumentas",
    },
    "thesis_p3_body": {
        "en": "Critical dependency mapping and a dedicated instrument to ensure long-term security and sustainability of key components.",
        "et": "Kriitiliste sõltuvuste kaardistamine ja spetsiaalne instrument võtmekomponentide pikaajalise turvalisuse ja jätkusuutlikkuse tagamiseks.",
        "de": "Kartierung kritischer Abhängigkeiten und ein spezielles Instrument zur Sicherstellung langfristiger Sicherheit und Nachhaltigkeit von Schlüsselkomponenten.",
        "fr": "Cartographie des dépendances critiques et un instrument dédié pour assurer la sécurité et la durabilité à long terme des composants clés.",
        "sv": "Kartläggning av kritiska beroenden och ett dedikerat instrument för att säkerställa långsiktig säkerhet och hållbarhet för nyckelkomponenter.",
        "lv": "Kritisko atkarību kartēšana un īpašs instruments galveno komponentu ilgtermiņa drošības un ilgtspējības nodrošināšanai.",
        "no": "Kartlegging av kritiske avhengigheter og et dedikert instrument for å sikre langsiktig sikkerhet og bærekraft for nøkkelkomponenter.",
        "da": "Kortlægning af kritiske afhængigheder og et dedikeret instrument til at sikre langsigtet sikkerhed og bæredygtighed af nøglekomponenter.",
        "pl": "Mapowanie krytycznych zależności i dedykowany instrument zapewniający długoterminowe bezpieczeństwo i zrównoważony rozwój kluczowych komponentów.",
        "nl": "Mapping van kritieke afhankelijkheden en een specifiek instrument om langetermijnveiligheid en duurzaamheid van sleutelcomponenten te waarborgen.",
        "fi": "Kriittisten riippuvuuksien kartoitus ja omistettu instrumentti avainkomponenttien pitkäaikaisen turvallisuuden ja kestävyyden varmistamiseksi.",
        "lt": "Kritinių priklausomybių žemėlapiai ir specialus instrumentas ilgalaikiam pagrindinių komponentų saugumui ir tvarumui užtikrinti.",
    },
    "thesis_p4_title": {
        "en": "Open source in procurement",
        "et": "Avatud lähtekood hangetel",
        "de": "Open Source in der Beschaffung",
        "fr": "Open source dans les marchés publics",
        "sv": "Öppen källkod i upphandling",
        "lv": "Atvērtais pirmkods iepirkumos",
        "no": "Åpen kildekode i anskaffelser",
        "da": "Open source i indkøb",
        "pl": "Open source w zamówieniach publicznych",
        "nl": "Open source in aanbestedingen",
        "fi": "Avoin lähdekoodi hankinnoissa",
        "lt": "Atvirasis kodas viešuosiuose pirkimuose",
    },
    "thesis_p4_body": {
        "en": "New guidelines, fair assessment of open bids, and stronger OSPOs (Open Source Programme Offices) in public administrations.",
        "et": "Uued juhised, avatud pakkumiste õiglane hindamine ja tugevamad OSPO-d (avatud lähtekoodiga programmi bürood) avalikes haldusasutustes.",
        "de": "Neue Richtlinien, faire Bewertung offener Angebote und stärkere OSPOs (Open Source Program Offices) in der öffentlichen Verwaltung.",
        "fr": "Nouvelles directives, évaluation équitable des offres ouvertes et renforcement des OSPOs (bureaux de programmes open source) dans les administrations publiques.",
        "sv": "Nya riktlinjer, rättvis bedömning av öppna anbud och starkare OSPO:er (Open Source Programme Offices) i offentliga förvaltningar.",
        "lv": "Jaunas vadlīnijas, godīgs atvērto piedāvājumu novērtējums un stiprāki OSPO (atvērtā pirmkoda programmu biroji) publiskajās administrācijās.",
        "no": "Nye retningslinjer, rettferdig vurdering av åpne tilbud og sterkere OSPOer (Open Source Programme Offices) i offentlige administrasjoner.",
        "da": "Nye retningslinjer, fair vurdering af åbne bud og stærkere OSPO'er (Open Source Programme Offices) i offentlige administrationer.",
        "pl": "Nowe wytyczne, uczciwa ocena otwartych ofert i silniejsze OSPO (biura programów open source) w administracjach publicznych.",
        "nl": "Nieuwe richtlijnen, eerlijke beoordeling van open offertes en sterkere OSPO's (Open Source Programme Offices) in overheidsorganisaties.",
        "fi": "Uudet ohjeet, avoimien tarjousten oikeudenmukainen arviointi ja vahvemmat OSPO:t (Open Source Programme Offices) julkishallinnossa.",
        "lt": "Naujos gairės, sąžiningas atvirų pasiūlymų vertinimas ir stipresni OSPO (atvirojo kodo programų biurai) viešosiose administracijose.",
    },
    "thesis_p5_title": {
        "en": "Embed in major EU initiatives",
        "et": "Lõimimine suurtesse EL-i algatustesse",
        "de": "Einbettung in große EU-Initiativen",
        "fr": "Intégration dans les grandes initiatives de l'UE",
        "sv": "Inbäddning i stora EU-initiativ",
        "lv": "Iekļaušana lielās ES iniciatīvās",
        "no": "Innbygging i store EU-initiativer",
        "da": "Indlejring i store EU-initiativer",
        "pl": "Osadzenie w głównych inicjatywach UE",
        "nl": "Inbedding in grote EU-initiatieven",
        "fi": "Upottaminen suuriin EU-aloitteisiin",
        "lt": "Įterpimas į dideles ES iniciatyvas",
    },
    "thesis_p5_body": {
        "en": "Open source at the heart of the EUDI Wallet, European Business Wallet, and Digital Commons EDIC.",
        "et": "Avatud lähtekood EUDI rahakoti, Euroopa ärirahakoti ja Digital Commons EDIC keskmes.",
        "de": "Open Source im Kern des EUDI-Wallets, des European Business Wallets und des Digital Commons EDIC.",
        "fr": "L'open source au cœur du portefeuille EUDI, du portefeuille d'entreprise européen et du Digital Commons EDIC.",
        "sv": "Öppen källkod i hjärtat av EUDI-plånboken, European Business Wallet och Digital Commons EDIC.",
        "lv": "Atvērtais pirmkods EUDI maka, Eiropas biznesa maka un Digital Commons EDIC centrā.",
        "no": "Åpen kildekode i hjertet av EUDI-lommeboken, European Business Wallet og Digital Commons EDIC.",
        "da": "Open source i hjertet af EUDI-tegnebogen, European Business Wallet og Digital Commons EDIC.",
        "pl": "Open source w sercu portfela EUDI, European Business Wallet i Digital Commons EDIC.",
        "nl": "Open source in het hart van de EUDI-portemonnee, European Business Wallet en Digital Commons EDIC.",
        "fi": "Avoin lähdekoodi EUDI-lompakon, European Business Walletin ja Digital Commons EDIC:n ytimessä.",
        "lt": "Atvirasis kodas EUDI piniginės, Europos verslo piniginės ir Digital Commons EDIC centre.",
    },
    "thesis_p6_title": {
        "en": "Support the ecosystem",
        "et": "Ökosüsteemi toetamine",
        "de": "Ökosystem unterstützen",
        "fr": "Soutenir l'écosystème",
        "sv": "Stödja ekosystemet",
        "lv": "Atbalstīt ekosistēmu",
        "no": "Støtte økosystemet",
        "da": "Støtte økosystemet",
        "pl": "Wspieranie ekosystemu",
        "nl": "Het ecosysteem ondersteunen",
        "fi": "Ekosysteemin tukeminen",
        "lt": "Ekosistemos palaikymas",
    },
    "thesis_p6_body": {
        "en": "Startups, skills development (including via Erasmus+), stewardship models, and international promotion of EU open source solutions.",
        "et": "Iduettevõtted, oskuste arendamine (sealhulgas Erasmus+ kaudu), haldusmudelid ja EL-i avatud lähtekoodiga lahenduste rahvusvaheline edendamine.",
        "de": "Startups, Kompetenzentwicklung (einschließlich über Erasmus+), Stewardship-Modelle und internationale Förderung von EU-Open-Source-Lösungen.",
        "fr": "Startups, développement des compétences (y compris via Erasmus+), modèles de gouvernance et promotion internationale des solutions open source de l'UE.",
        "sv": "Startups, kompetensutveckling (inklusive via Erasmus+), förvaltningsmodeller och internationell marknadsföring av EU:s öppna källkodslösningar.",
        "lv": "Jaunuzņēmumi, prasmju attīstība (tostarp caur Erasmus+), pārvaldības modeļi un ES atvērtā pirmkoda risinājumu starptautiskā popularizēšana.",
        "no": "Oppstarter, kompetanseutvikling (inkludert via Erasmus+), forvaltningsmodeller og internasjonal promotering av EUs åpen kildekode-løsninger.",
        "da": "Startups, kompetenceudvikling (herunder via Erasmus+), forvaltningsmodeller og international promovering af EU's open source-løsninger.",
        "pl": "Startupy, rozwój kompetencji (w tym przez Erasmus+), modele zarządzania i międzynarodowa promocja unijnych rozwiązań open source.",
        "nl": "Startups, vaardigheidsontwikkeling (inclusief via Erasmus+), stewardshipmodellen en internationale promotie van EU open source oplossingen.",
        "fi": "Startup-yritykset, osaamisen kehittäminen (mukaan lukien Erasmus+:n kautta), hallintomallit ja EU:n avoimen lähdekoodin ratkaisujen kansainvälinen edistäminen.",
        "lt": "Startuoliai, įgūdžių ugdymas (įskaitant per Erasmus+), valdymo modeliai ir tarptautinis ES atvirojo kodo sprendimų skatinimas.",
    },
    "thesis_why_eyebrow": {
        "en": "Why this matters", "et": "Miks see oluline on", "de": "Warum das wichtig ist",
        "fr": "Pourquoi c'est important", "sv": "Varför detta är viktigt", "lv": "Kāpēc tas ir svarīgi",
        "no": "Hvorfor dette er viktig", "da": "Hvorfor dette er vigtigt", "pl": "Dlaczego to ważne",
        "nl": "Waarom dit belangrijk is", "fi": "Miksi tämä on tärkeää", "lt": "Kodėl tai svarbu",
    },
    "thesis_why_heading": {
        "en": "A practical step toward reducing vendor lock-in and capturing more value in Europe.",
        "et": "Praktiline samm tarnijast sõltuvuse vähendamise ja Euroopas suurema väärtuse loomise suunas.",
        "de": "Ein praktischer Schritt zur Reduzierung der Anbieterabhängigkeit und zur Wertschöpfung in Europa.",
        "fr": "Une étape pratique vers la réduction de la dépendance fournisseur et la capture de plus de valeur en Europe.",
        "sv": "Ett praktiskt steg mot att minska leverantörsinlåsning och fånga mer värde i Europa.",
        "lv": "Praktisks solis ceļā uz piegādātāju ieslēgšanas samazināšanu un lielākas vērtības radīšanu Eiropā.",
        "no": "Et praktisk skritt mot å redusere leverandørinnlåsing og fange mer verdi i Europa.",
        "da": "Et praktisk skridt mod at reducere leverandørafhængighed og fange mere værdi i Europa.",
        "pl": "Praktyczny krok w kierunku ograniczenia uzależnienia od dostawcy i tworzenia większej wartości w Europie.",
        "nl": "Een praktische stap naar het verminderen van leveranciersafhankelijkheid en het vastleggen van meer waarde in Europa.",
        "fi": "Käytännön askel toimittajalukon vähentämiseen ja lisäarvon kaappaamiseen Euroopassa.",
        "lt": "Praktinis žingsnis mažinant priklausomybę nuo tiekėjų ir kuriant didesnę vertę Europoje.",
    },
    "thesis_why_body1": {
        "en": "This is not an aspirational white paper — it is a practical framework for reducing vendor lock-in across European public infrastructure. By linking procurement, R&D funding, maintenance and deployment into a single strategy, the Commission is building the conditions for a self-sustaining open source ecosystem that Europe controls.",
        "et": "See pole ambitsioonikast valgest raamatust — see on praktiline raamistik tarnijast sõltuvuse vähendamiseks kogu Euroopa avalikus taristus. Sidudes hanked, teadus- ja arendusrahastuse, hoolduse ja juurutamise ühtseks strateegiaks, loob komisjon tingimused isemajandavale avatud lähtekoodiga ökosüsteemile, mida Euroopa kontrollib.",
        "de": "Dies ist kein aspiratives Weißbuch — es ist ein praktischer Rahmen zur Reduzierung der Anbieterabhängigkeit in der europäischen öffentlichen Infrastruktur. Durch die Verknüpfung von Beschaffung, F&E-Finanzierung, Wartung und Bereitstellung in einer einzigen Strategie schafft die Kommission die Bedingungen für ein sich selbst tragendes Open-Source-Ökosystem unter europäischer Kontrolle.",
        "fr": "Ce n'est pas un livre blanc ambitieux — c'est un cadre pratique pour réduire la dépendance fournisseur dans l'infrastructure publique européenne. En reliant marchés publics, financement R&D, maintenance et déploiement dans une stratégie unique, la Commission crée les conditions d'un écosystème open source auto-suffisant contrôlé par l'Europe.",
        "sv": "Detta är inte ett aspirerande vitpapper — det är ett praktiskt ramverk för att minska leverantörsinlåsning i europeisk offentlig infrastruktur. Genom att koppla upphandling, FoU-finansiering, underhåll och driftsättning i en enda strategi skapar kommissionen förutsättningarna för ett självbärande ekosystem för öppen källkod som Europa kontrollerar.",
        "lv": "Šis nav ambiciozs baltais dokuments — tas ir praktisks ietvars piegādātāju ieslēgšanas mazināšanai Eiropas publiskajā infrastruktūrā. Savienojot iepirkumus, pētniecības finansējumu, uzturēšanu un ieviešanu vienotā stratēģijā, Komisija veido apstākļus pašpietiekamam atvērtā pirmkoda ekosistēmai, ko kontrolē Eiropa.",
        "no": "Dette er ikke en ambisiøs hvitbok — det er et praktisk rammeverk for å redusere leverandørinnlåsing i europeisk offentlig infrastruktur. Ved å koble anskaffelse, FoU-finansiering, vedlikehold og utrulling i én strategi bygger Kommisjonen forutsetningene for et selvbærende åpen kildekode-økosystem som Europa kontrollerer.",
        "da": "Dette er ikke et ambitiøst hvidbog — det er en praktisk ramme for at reducere leverandørafhængighed i europæisk offentlig infrastruktur. Ved at forbinde indkøb, F&U-finansiering, vedligeholdelse og implementering i én strategi skaber Kommissionen betingelserne for et selvbærende open source-økosystem, som Europa kontrollerer.",
        "pl": "To nie jest ambitna biała księga — to praktyczne ramy ograniczania uzależnienia od dostawcy w europejskiej infrastrukturze publicznej. Łącząc zamówienia, finansowanie B+R, utrzymanie i wdrożenie w jedną strategię, Komisja tworzy warunki dla samowystarczalnego ekosystemu open source kontrolowanego przez Europę.",
        "nl": "Dit is geen ambitieus witboek — het is een praktisch kader voor het verminderen van leveranciersafhankelijkheid in de Europese publieke infrastructuur. Door inkoop, O&O-financiering, onderhoud en implementatie in één strategie te koppelen, schept de Commissie de voorwaarden voor een zelfvoorzienend open source ecosysteem onder Europese controle.",
        "fi": "Tämä ei ole kunnianhimoinen valkoinen kirja — se on käytännön kehys toimittajalukon vähentämiseksi Euroopan julkisessa infrastruktuurissa. Yhdistämällä hankinnat, T&K-rahoituksen, ylläpidon ja käyttöönoton yhdeksi strategiaksi komissio luo edellytykset omavaraiselle avoimen lähdekoodin ekosysteemille, jota Eurooppa hallitsee.",
        "lt": "Tai nėra ambicinga baltoji knyga — tai praktinis pagrindas tiekėjų priklausomybei mažinti Europos viešojoje infrastruktūroje. Sujungdama viešuosius pirkimus, MTEP finansavimą, priežiūrą ir diegimą į vieną strategiją, Komisija kuria sąlygas savarankiškai atvirojo kodo ekosistemai, kurią kontroliuoja Europa.",
    },
    "thesis_why_body2": {
        "en": "At Predictive Labs, we have operated on this thesis from day one: commoditised capability belongs in the commons, client-specific work stays private, and every pipeline should be auditable by design. The EU Open Source Strategy validates that approach at continental scale.",
        "et": "Predictive Labs on tegutsenud selle teesi alusel esimesest päevast: standardsed võimekused kuuluvad ühisvaramusse, kliendispetsiifiline töö jääb eraviisilistuks ja iga torujuhe peaks olema kavandatud auditeeritavana. EL-i avatud lähtekoodiga strateegia kinnitab seda lähenemist mandrilises mastaabis.",
        "de": "Bei Predictive Labs haben wir von Anfang an nach dieser These gearbeitet: Standardfähigkeiten gehören in die Allgemeingüter, kundenspezifische Arbeit bleibt privat, und jede Pipeline sollte von Grund auf prüfbar sein. Die EU-Open-Source-Strategie bestätigt diesen Ansatz im kontinentalen Maßstab.",
        "fr": "Chez Predictive Labs, nous avons opéré selon cette thèse depuis le premier jour : les capacités banalisées appartiennent aux biens communs, le travail spécifique au client reste privé, et chaque pipeline doit être auditable par conception. La stratégie open source de l'UE valide cette approche à l'échelle continentale.",
        "sv": "På Predictive Labs har vi arbetat efter denna tes sedan dag ett: standardiserade kapabiliteter hör till allmänningen, kundspecifikt arbete förblir privat, och varje pipeline bör vara granskningsbar genom design. EU:s öppen-källkodsstrategi validerar detta tillvägagångssätt i kontinental skala.",
        "lv": "Predictive Labs ir darbojušies pēc šīs tēzes kopš pirmās dienas: standartizētas spējas pieder kopienei, klientam specifiskais darbs paliek privāts, un katram cauruļvadam jābūt pārbaudāmam pēc būtības. ES atvērtā pirmkoda stratēģija apstiprina šo pieeju kontinentālā mērogā.",
        "no": "Hos Predictive Labs har vi operert etter denne tesen fra dag én: standardiserte kapabiliteter hører til fellesskapet, kundespesifikt arbeid forblir privat, og hver pipeline bør være reviderbar fra utformingen. EUs åpen kildekode-strategi validerer denne tilnærmingen i kontinental skala.",
        "da": "Hos Predictive Labs har vi opereret efter denne tese fra dag ét: standardiserede kapabiliteter tilhører fællesskabet, kundespecifikt arbejde forbliver privat, og hver pipeline bør være reviderbar fra design. EU's open source-strategi validerer denne tilgang i kontinental skala.",
        "pl": "W Predictive Labs od pierwszego dnia działamy zgodnie z tą tezą: ustandaryzowane możliwości należą do wspólnoty, praca specyficzna dla klienta pozostaje prywatna, a każdy potok powinien być audytowalny z założenia. Strategia open source UE potwierdza to podejście w skali kontynentalnej.",
        "nl": "Bij Predictive Labs werken we vanaf dag één volgens deze these: gestandaardiseerde capaciteiten behoren tot de commons, klantspecifiek werk blijft privé, en elke pipeline moet controleerbaar zijn door ontwerp. De EU Open Source Strategie valideert deze aanpak op continentale schaal.",
        "fi": "Predictive Labsissa olemme toimineet tämän teesin pohjalta ensimmäisestä päivästä lähtien: standardoidut kyvykkyydet kuuluvat yhteisvarantoon, asiakaskohtainen työ pysyy yksityisenä, ja jokaisen putkilinjan tulee olla suunnitelmallisesti tarkastettava. EU:n avoimen lähdekoodin strategia vahvistaa tämän lähestymistavan mannerlaajuisesti.",
        "lt": "Predictive Labs veikė pagal šią tezę nuo pirmos dienos: standartizuoti gebėjimai priklauso bendruomenei, klientui specifinis darbas lieka privatus, ir kiekvienas vamzdynas turėtų būti audituojamas pagal dizainą. ES atvirojo kodo strategija patvirtina šį požiūrį žemyniniu mastu.",
    },
    "thesis_read_more": {
        "en": "Read more", "et": "Loe lisaks", "de": "Mehr erfahren",
        "fr": "En savoir plus", "sv": "Läs mer", "lv": "Lasīt vairāk",
        "no": "Les mer", "da": "Læs mere", "pl": "Czytaj więcej",
        "nl": "Lees meer", "fi": "Lue lisää", "lt": "Skaityti daugiau",
    },
    "thesis_see_research": {
        "en": "See our open source work", "et": "Vaata meie avatud lähtekoodiga tööd",
        "de": "Unsere Open-Source-Arbeit ansehen", "fr": "Voir nos travaux open source",
        "sv": "Se vårt öppna källkodsarbete", "lv": "Skatīt mūsu atvērtā pirmkoda darbus",
        "no": "Se vårt åpen kildekode-arbeid", "da": "Se vores open source-arbejde",
        "pl": "Zobacz nasze prace open source", "nl": "Bekijk ons open source werk",
        "fi": "Katso avoimen lähdekoodin työmme", "lt": "Žiūrėti mūsų atvirojo kodo darbus",
    },
    "thesis_cta_headline": {
        "en": "Building on open source for European public services?",
        "et": "Ehitate avatud lähtekoodil põhinevaid Euroopa avalikke teenuseid?",
        "de": "Aufbau auf Open Source für europäische öffentliche Dienste?",
        "fr": "Construire sur l'open source pour les services publics européens ?",
        "sv": "Bygger på öppen källkod för europeiska offentliga tjänster?",
        "lv": "Veidojat uz atvērtā pirmkoda bāzes Eiropas sabiedriskajiem pakalpojumiem?",
        "no": "Bygger på åpen kildekode for europeiske offentlige tjenester?",
        "da": "Bygger på open source til europæiske offentlige tjenester?",
        "pl": "Budujesz na open source dla europejskich usług publicznych?",
        "nl": "Bouwen op open source voor Europese overheidsdiensten?",
        "fi": "Rakentamassa avoimen lähdekoodin varaan eurooppalaisille julkisille palveluille?",
        "lt": "Kuriate atvirojo kodo pagrindu Europos viešąsias paslaugas?",
    },
    "thesis_cta_body": {
        "en": "We build AI systems on open, auditable stacks for European public-sector programmes. If your brief aligns with this thesis, talk to us.",
        "et": "Ehitame tehisintellekti süsteeme avatud, auditeeritavatel platvormidel Euroopa avaliku sektori programmidele. Kui teie lähteülesanne ühtib selle teesiga, rääkige meiega.",
        "de": "Wir bauen KI-Systeme auf offenen, prüfbaren Stacks für europäische Programme des öffentlichen Sektors. Wenn Ihr Auftrag mit dieser These übereinstimmt, sprechen Sie mit uns.",
        "fr": "Nous construisons des systèmes d'IA sur des stacks ouverts et auditables pour les programmes du secteur public européen. Si votre brief s'aligne avec cette thèse, parlez-nous.",
        "sv": "Vi bygger AI-system på öppna, granskningsbara stackar för europeiska offentliga sektorprogram. Om ert uppdrag överensstämmer med denna tes, prata med oss.",
        "lv": "Mēs veidojam MI sistēmas uz atvērtiem, pārbaudāmiem steku pamatlīdzekļiem Eiropas publiskā sektora programmām. Ja jūsu uzdevums atbilst šai tēzei, sazinieties ar mums.",
        "no": "Vi bygger KI-systemer på åpne, reviderbare stackar for europeiske offentlige sektorprogrammer. Hvis ditt oppdrag stemmer med denne tesen, snakk med oss.",
        "da": "Vi bygger AI-systemer på åbne, reviderbare stacks til europæiske offentlige sektorprogrammer. Hvis jeres brief stemmer overens med denne tese, tal med os.",
        "pl": "Budujemy systemy AI na otwartych, audytowalnych stosach dla europejskich programów sektora publicznego. Jeśli twój brief jest zgodny z tą tezą, porozmawiaj z nami.",
        "nl": "Wij bouwen AI-systemen op open, controleerbare stacks voor Europese publieke sectorprogramma's. Als uw opdracht aansluit bij deze these, praat met ons.",
        "fi": "Rakennamme tekoälyjärjestelmiä avoimille, tarkastettaville pinoille eurooppalaisille julkisen sektorin ohjelmille. Jos toimeksiantosi on linjassa tämän teesin kanssa, ota yhteyttä.",
        "lt": "Kuriame DI sistemas ant atvirų, audituojamų technologijų paketų Europos viešojo sektoriaus programoms. Jei jūsų užduotis atitinka šią tezę, susisiekite su mumis.",
    },

    # ── News section ──────────────────────────────────────────
    "news": {
        "en": "News", "et": "Uudised", "de": "Nachrichten",
        "fr": "Actualités", "sv": "Nyheter", "lv": "Ziņas",
        "no": "Nyheter", "da": "Nyheder", "pl": "Wiadomości",
        "nl": "Nieuws", "fi": "Uutiset", "lt": "Naujienos",
    },
    "news_refresh": {
        "en": "Refreshed hourly from public RSS + Atom feeds.",
        "et": "Värskendatakse tunni tagant avalikest RSS + Atom voogudest.",
        "de": "Stündlich aus öffentlichen RSS- und Atom-Feeds aktualisiert.",
        "fr": "Actualisé toutes les heures à partir de flux RSS et Atom publics.",
        "sv": "Uppdateras varje timme från offentliga RSS- och Atom-flöden.",
        "lv": "Atjaunināts katru stundu no publiskajiem RSS un Atom plūsmām.",
        "no": "Oppdateres hver time fra offentlige RSS- og Atom-strømmer.",
        "da": "Opdateres hver time fra offentlige RSS- og Atom-feeds.",
        "pl": "Odświeżane co godzinę z publicznych kanałów RSS i Atom.",
        "nl": "Elk uur vernieuwd vanuit openbare RSS- en Atom-feeds.",
        "fi": "Päivitetään tunneittain julkisista RSS- ja Atom-syötteistä.",
        "lt": "Atnaujinama kas valandą iš viešų RSS ir Atom kanalų.",
    },

    # ── Case study card labels ────────────────────────────────
    "case_problem": {
        "en": "Problem", "et": "Probleem", "de": "Problem",
        "fr": "Problème", "sv": "Problem", "lv": "Problēma",
        "no": "Problem", "da": "Problem", "pl": "Problem",
        "nl": "Probleem", "fi": "Ongelma", "lt": "Problema",
    },
    "case_approach": {
        "en": "Approach", "et": "Lähenemine", "de": "Ansatz",
        "fr": "Approche", "sv": "Tillvägagångssätt", "lv": "Pieeja",
        "no": "Tilnærming", "da": "Tilgang", "pl": "Podejście",
        "nl": "Aanpak", "fi": "Lähestymistapa", "lt": "Požiūris",
    },
    "case_capability": {
        "en": "Capability", "et": "Võimekus", "de": "Fähigkeit",
        "fr": "Capacité", "sv": "Kapabilitet", "lv": "Spēja",
        "no": "Kapabilitet", "da": "Kapabilitet", "pl": "Możliwość",
        "nl": "Capaciteit", "fi": "Kyvykkyys", "lt": "Gebėjimas",
    },
}
