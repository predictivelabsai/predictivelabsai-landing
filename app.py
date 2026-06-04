"""
Predictive Labs — multipage FastHTML landing site (v2).

Dark, palantir-inspired, public-sector first. Content lives in content/*.py;
routes are thin composition layers over components.py primitives.
"""

from fasthtml.common import (
    fast_app, serve, Div, Span, A, P, Ul, Li, Section, Article, Header,
    NotStr, Script, Style, H1, H2, H3, Button,
)

from components import (
    page, Hero, Pillar, MetricTile, CaseStudyCard, CTASection, NewsSection,
    Section_, Heading, Eyebrow, Pill, Button_, SectorLink,
    CONTACT_EMAIL, GITHUB_URL, LINKEDIN_URL,
)
from content.case_studies import ALL as ALL_CASES, BID_DERIVED, NAMED_PRECEDENTS
from content.team import TEAM
from content.repos import REPOS, EXTERNAL_RESEARCH
from content import signal as signal_mod
from content import news as news_mod

# Kick off the background RSS refresher once at import time so page renders
# never block on upstream fetches.
news_mod.start_background_refresh()


app, rt = fast_app(live=False, static_path=".", pico=False)


# ---------- /  Home ----------

@rt("/")
def home():
    pillars = [
        ("01", "Document intelligence", "Extraction and retrieval over regulatory filings, clinical protocols, tender packs and legal corpora — with auditable citation trails."),
        ("02", "Applied forecasting", "Demand, revenue and operational forecasting that fuses internal records with open data, satellite and alternative signals."),
        ("03", "Geospatial & mobility", "Origin-destination matrices, anomaly detection and situation pictures, built on open data and published as reference implementations."),
        ("04", "Agentic workflows", "Multi-step LLM agents that run inside your security boundary, instrumented for evaluation and human review."),
    ]

    logos_row = [
        "Microsoft (ISD)", "ARM Holdings", "DBRS Morningstar", "London Stock Exchange Group",
        "Nando's", "Indurent (Blackstone)",
    ]

    # Pick 3 case studies for the home strip — one public-sector, one Nordic health, one enterprise
    home_cases = [c for c in ALL_CASES if c["id"] in ("uk-traffic-od", "nordic-health-rwd", "microsoft-isd")]

    return page(
        "AI for public outcomes",
        "/",
        Hero(),

        # Logo / precedent bar
        Section_(
            Eyebrow("Precedent"),
            Heading(2, "Delivered inside institutions that take correctness seriously.", cls="mt-4 max-w-3xl"),
            Div(
                *[Div(name, cls="text-ink-muted text-sm md:text-base font-medium border border-line rounded-full px-4 py-2") for name in logos_row],
                cls="mt-10 flex flex-wrap gap-3",
            ),
            cls="border-b border-line",
        ),

        # Capability pillars
        Section_(
            Div(
                Eyebrow("Capabilities"),
                Heading(2, "Four capabilities, composed to fit the programme.", cls="mt-4 max-w-4xl"),
                P("We don't ship a platform. We ship a team that brings a platform's discipline to every engagement — reproducible pipelines, versioned models, inspectable prompts, open code where the law and the contract allow.", cls="mt-5 text-ink-muted text-lg max-w-3xl"),
                cls="mb-14",
            ),
            Div(
                *[Pillar(n, t, b) for n, t, b in pillars],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),

        # Sector focus
        Section_(
            Div(
                Eyebrow("Where we work"),
                Heading(2, "Built around four public-sector programmes — and one commercial root.", cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                _sector_link("Defense & public security", "Decision support inside defence, justice and critical infrastructure — with clear boundaries between AI assistance and human authority.", "/solutions/defense"),
                _sector_link("Health & life sciences", "Real-world evidence, protocol design and hospital operations — on privacy-preserving, regulatory-grade pipelines.", "/solutions/healthcare"),
                _sector_link("Public management & mobility", "Traffic, planning and municipal analytics — built on open data and shipped with reference implementations.", "/solutions/public"),
                _sector_link("Financial services", "Our commercial root — rating, forecasting and document intelligence at enterprise scale. Now ~20% of our work.", "/solutions/financial"),
                cls="grid md:grid-cols-2 gap-5",
            ),
            cls="border-y border-line bg-bg-elevated/40",
        ),

        # Case-study strip
        Section_(
            Div(
                Eyebrow("Selected work"),
                Heading(2, "What the programmes look like.", cls="mt-4 max-w-3xl"),
                cls="mb-14 flex flex-col md:flex-row md:items-end md:justify-between gap-4",
            ),
            Div(
                *[CaseStudyCard(c, compact=True) for c in home_cases],
                cls="grid md:grid-cols-3 gap-5",
            ),
            Div(
                Button_("All case studies", href="/case-studies", primary=False),
                cls="mt-10",
            ),
        ),

        # Signal teaser
        Section_(
            Div(
                Div(
                    Eyebrow("Signal"),
                    Heading(2, "We read the data our clients work with — every day.", cls="mt-4 max-w-3xl"),
                    P(
                        "Public-sector delivery starts with the public data. A live view of NHS waiting lists, European ",
                        SectorLink("defence"), " spend, school ",
                        SectorLink("attainment", sector="education"), " gaps, ",
                        SectorLink("energy"), " mix and AI readiness — the canvases our programmes run against.",
                        cls="mt-5 text-ink-muted text-lg max-w-2xl leading-relaxed",
                    ),
                    Button_("Open Signal", href="/signal", primary=True, cls="mt-8"),
                    cls="md:w-2/5",
                ),
                Div(
                    Div(id="signal-teaser", cls="w-full h-[360px]"),
                    cls="md:w-3/5 p-3 rounded-2xl bg-bg-elevated border border-line",
                ),
                cls="flex flex-col md:flex-row gap-10 items-stretch",
            ),
            cls="border-y border-line",
        ),

        NewsSection(
            category="home",
            title="What's moving in AI and European public services.",
            subtitle="A rolling mix from AI, government, health, defence and financial-services feeds. Refreshed hourly; links open in a new tab.",
        ),

        CTASection(),

        # Load Plotly only when signal teaser present (home page only)
        body_extra=[
            Script(src="https://cdn.plot.ly/plotly-2.35.2.min.js"),
            Script(NotStr(f"window.PLOTLY_TEASER = {_teaser_json()};")),
            Script(src="/static/signal.js"),
            Script(src="/static/three-hero.js", type="module"),
        ],
    )


def _sector_link(title, body, href):
    return A(
        Div(
            Div(
                Span(title, cls="text-ink text-xl font-medium tracking-tight"),
                Span("→", cls="text-accent text-xl ml-auto"),
                cls="flex items-center mb-3",
            ),
            P(body, cls="text-ink-muted text-sm leading-relaxed"),
            cls="p-7 rounded-2xl border border-line bg-bg-elevated hover:border-accent/50 hover:bg-bg-raised transition-all",
        ),
        href=href,
        cls="block",
    )


def _teaser_json():
    import json
    from content import signal as s
    nhs, _ = s.nhs_charts()
    # Simplify layout for teaser
    nhs["layout"]["title"]["text"] = "NHS England waiting list · treemap by specialty"
    nhs["layout"]["margin"] = {"l": 0, "r": 0, "t": 30, "b": 0}
    return json.dumps(nhs)


# ---------- /platform ----------

@rt("/platform")
def platform():
    pillars = [
        ("01", "Document intelligence", "We build ingest-and-reason pipelines over the documents your mission actually runs on — statutes, protocols, ITT packs, rating manuals. Every extraction is citation-anchored and every answer is reproducible from the source."),
        ("02", "Applied forecasting", "From elective-surgery demand to public-sector revenue, we fuse authoritative internal records with open, alternative and satellite data. Models are versioned, backtested and delivered with the evaluation harness that keeps them honest."),
        ("03", "Geospatial and mobility", "Traffic, probe-vehicle data, ANPR and infrastructure telemetry turned into origin-destination matrices, congestion signatures and operational situation pictures. Reference implementations like open-od-toolkit stay in the public domain."),
        ("04", "Agentic workflows", "Multi-step LLM agents that plan, call tools and defer to humans, running inside your security boundary. We instrument every step with evaluations, audit logs and explicit escalation paths."),
    ]

    commitments = [
        ("Auditability by design", "Every pipeline is versioned; every model output can be traced back to a specific input, prompt, and revision."),
        ("Open where it's better open", "Commoditised capabilities go to GitHub. Clients get the specific work; the method stays in the community."),
        ("GDPR-native", "Data-protection impact assessment first, then architecture. No data leaves the territory unless the client and the law both say it can."),
        ("Evaluation before volume", "Before a model handles a case, it has to answer for a hundred held-out ones. Before an agent acts, it has to pass a red-team."),
    ]

    return page(
        "Platform",
        "/platform",
        Section_(
            Eyebrow("Platform"),
            Heading(1, "A way of working that behaves like a platform.", cls="mt-5 max-w-5xl"),
            P(
                "We are a consultancy. We deliver as a team of AI and data engineers, data scientists and domain specialists. What makes us look like a platform is the discipline we bring to every programme: the same pipeline conventions, the same evaluation harness, the same audit posture — whether the brief is a ",
                SectorLink("rating model", sector="financial"), ", a ",
                SectorLink("hospital-operations dashboard", sector="health"), " or a ",
                SectorLink("municipal traffic signal", sector="public management"), ".",
                cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow("Capabilities"),
                Heading(2, "Four composable capabilities.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(*[_platform_row(n, t, b) for n, t, b in pillars], cls="divide-y divide-line border-y border-line"),
        ),
        Section_(
            Div(
                Eyebrow("How we commit"),
                Heading(2, "Four commitments we write into every contract.", cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                *[Div(
                    Heading(3, title, cls="mb-2"),
                    P(body, cls="text-ink-muted text-sm leading-relaxed"),
                    cls="p-7 rounded-2xl bg-bg-elevated border border-line",
                ) for title, body in commitments],
                cls="grid md:grid-cols-2 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        CTASection(),
        body_extra=[Script(src="/static/three-hero.js", type="module")],
    )


def _platform_row(number, title, body):
    return Div(
        Div(
            Div(number, cls="font-mono text-xs tracking-widest text-accent"),
            cls="md:w-24 shrink-0",
        ),
        Div(
            Heading(3, title, cls="mb-3"),
            P(body, cls="text-ink-muted leading-relaxed"),
            cls="flex-1",
        ),
        cls="flex flex-col md:flex-row gap-6 py-10",
    )


# ---------- /solutions/* ----------

SOLUTIONS = {
    "defense": {
        "title": "Defense & public security",
        "eyebrow": "Defense & public security",
        "headline": "Decision support where the stakes are operational.",
        "lede": "Satellite-imagery analytics, situation-picture tooling and document intelligence for defence, justice and critical-infrastructure bodies — with clear separation between AI assistance and human authority.",
        "pillars": [
            ("Satellite & geospatial intelligence", "From Sentinel-2 imagery pipelines to change-detection and OSINT fusion, delivered through reproducible open-source stacks."),
            ("Situation pictures", "Fused operational views for municipal and national operators — sensor feeds, anomaly detection, incident summaries."),
            ("Justice and casework data", "Data-warehouse and dashboarding foundations for probation, regulatory and enforcement agencies, under the strictest access controls."),
        ],
        "case_ids": ["nl-justice-dataplatform", "nordic-city-signal", "uk-traffic-od"],
        "register": ["Operational confidence", "Auditable decision trail", "Human in authority"],
    },
    "healthcare": {
        "title": "Health & life sciences",
        "eyebrow": "Health & life sciences",
        "headline": "Real-world evidence and hospital operations, with patient data treated as such.",
        "lede": "Privacy-preserving analytics over national registries, protocol-design automation for health-technology assessment, and AI-application development across hospital systems — delivered with EU AI Act and clinical-data discipline.",
        "pillars": [
            ("Real-world data and evidence", "Pipelines over inpatient records, dispensing data and civil registries, with protocol templates that compress follow-up cycles."),
            ("Hospital operations", "Elective-recovery forecasting, capacity planning and AI-sovelluskehitys for the panels Europe's largest hospital systems put on frameworks."),
            ("Clinical document intelligence", "Extraction and structured summarisation of clinical and regulatory documents, audited against human adjudication."),
        ],
        "case_ids": ["nordic-health-rwd", "nordic-health-panel", "microsoft-isd"],
        "register": ["GDPR-native", "EU AI Act readiness", "Clinical audit trail"],
    },
    "public": {
        "title": "Public management & mobility",
        "eyebrow": "Public management & mobility",
        "headline": "Open data, open code, operational insight.",
        "lede": "Traffic, mobility, municipal planning and data-quality programmes for European public bodies — built on open data, shipped with reference implementations, and priced honestly against the budget on the notice.",
        "pillars": [
            ("Traffic and origin-destination analytics", "County- and city-scale mobility analytics built on ANPR, Bluetooth and open-data fusion, with methodology published on GitHub."),
            ("Municipal data foundations", "Data-quality frameworks, dynamic purchasing frameworks and continuous analytics call-offs for municipalities."),
            ("Planning and forecasting", "Demand, footfall and service-use forecasting for local and regional public-sector planning teams."),
        ],
        "case_ids": ["uk-traffic-od", "nordic-city-signal", "dk-data-quality"],
        "register": ["Open-source by default", "Reference implementations", "Interoperable"],
    },
    "financial": {
        "title": "Financial services",
        "eyebrow": "Financial services",
        "headline": "Where we came from — and where we still deliver, selectively.",
        "lede": "Rating models, revenue forecasting and document intelligence inside regulated institutions. Financial services is the root of our practice and remains about a fifth of our work today.",
        "pillars": [
            ("Rating and risk models", "Production machine-learning for credit and securitisation ratings, deployed with regulatory auditability."),
            ("Revenue and demand forecasting", "Time-series modelling for enterprise revenue planning, integrating alternative datasets."),
            ("Document intelligence at scale", "Extraction, classification and retrieval over prospectuses, filings and rating manuals."),
        ],
        "case_ids": ["dbrs-rmbs", "arm-forecasting", "microsoft-isd"],
        "register": ["Production ML ops", "Regulatory auditability", "Enterprise scale"],
    },
}


SOLUTION_NEWS = {
    "defense": ("defense", "Defence and public-security signal.", "Latest from MoD announcements, EU defence procurement and the wider defence-AI conversation."),
    "healthcare": ("healthcare", "Health and life-sciences signal.", "NHS digital-health coverage, DHSC announcements, and European health-data developments."),
    "public": ("public", "Public-management and mobility signal.", "UK central and local government digital, procurement and AI deployment news."),
    "financial": ("financial", "Financial-services signal.", "Financial-services AI, regulation and FinTech deployment across the UK and Europe."),
}


def _solution_page(slug):
    s = SOLUTIONS[slug]
    cases = [c for c in ALL_CASES if c["id"] in s["case_ids"]]
    news_key, news_title, news_sub = SOLUTION_NEWS[slug]

    return page(
        s["title"],
        f"/solutions/{slug}",
        Section_(
            Eyebrow(s["eyebrow"]),
            Heading(1, s["headline"], cls="mt-5 max-w-5xl"),
            P(s["lede"], cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            Div(
                *[Pill(r) for r in s["register"]],
                cls="mt-10 flex flex-wrap gap-2",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow("Where we focus"),
                Heading(2, "Three focal points in this vertical.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                *[Pillar(f"0{i+1}", t, b) for i, (t, b) in enumerate(s["pillars"])],
                cls="grid md:grid-cols-3 gap-5",
            ),
        ),
        Section_(
            Div(
                Eyebrow("In practice"),
                Heading(2, "What this looks like on programme.", cls="mt-4 max-w-3xl"),
                cls="mb-14",
            ),
            Div(
                *[CaseStudyCard(c) for c in cases],
                cls="grid md:grid-cols-3 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        NewsSection(category=news_key, title=news_title, subtitle=news_sub),
        CTASection(),
    )


@rt("/solutions/defense")
def sol_defense():
    return _solution_page("defense")


@rt("/solutions/healthcare")
def sol_health():
    return _solution_page("healthcare")


@rt("/solutions/public")
def sol_public():
    return _solution_page("public")


@rt("/solutions/financial")
def sol_financial():
    return _solution_page("financial")


# ---------- /case-studies ----------

@rt("/case-studies")
def case_studies():
    return page(
        "Case studies",
        "/case-studies",
        Section_(
            Eyebrow("Case studies"),
            Heading(1, "Engagements, not endorsements.", cls="mt-5 max-w-4xl"),
            P("We name the clients we are contractually cleared to name and keep the rest anonymised until they are. Here are six current European public-sector engagements and three commercial precedents that established the practice.",
              cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow("Current engagements"),
                Heading(2, "Public-sector programmes in flight.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                *[CaseStudyCard(c) for c in BID_DERIVED],
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
        Section_(
            Div(
                Eyebrow("Named precedents"),
                Heading(2, "Commercial roots.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                *[CaseStudyCard(c) for c in NAMED_PRECEDENTS],
                cls="grid md:grid-cols-3 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        CTASection(),
    )


# ---------- /signal ----------

@rt("/signal")
def signal():
    charts = signal_mod.all_charts()
    tabs = []
    panels = []
    for key, block in charts.items():
        tabs.append(
            Button(
                block["title"],
                type="button",
                cls="signal-tab",
                **{"data-signal-tab": key},
            )
        )
        panels.append(
            Div(
                Div(
                    Eyebrow(block["eyebrow"]),
                    Heading(2, block["title"], cls="mt-4"),
                    P(block["summary"], cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed"),
                    cls="mb-10",
                ),
                Div(
                    Div(
                        Div(id=f"chart-{key}-primary", cls="w-full"),
                        cls="chart-frame md:col-span-2",
                    ),
                    Div(
                        Div(id=f"chart-{key}-secondary", cls="w-full"),
                        cls="chart-frame",
                    ),
                    cls="grid md:grid-cols-3 gap-5",
                ),
                Div(
                    Span("Source: ", cls="text-ink-dim text-xs"),
                    A(block["source"]["label"], href=block["source"]["url"], target="_blank", cls="text-accent text-xs hover:underline"),
                    cls="mt-4",
                ),
                cls="hidden",
                **{"data-signal-panel": key},
            )
        )

    return page(
        "Signal",
        "/signal",
        Section_(
            Eyebrow("Signal"),
            Heading(1, "Public-sector data, visualised with the discipline we bring to programmes.", cls="mt-5 max-w-5xl"),
            P("Five canvases across the sectors we serve. Every figure is sourced from a named public dataset and cited below its chart. Nothing here is a client artefact.",
              cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(*tabs, cls="flex flex-wrap gap-3 mb-10"),
            Div(*panels),
            cls="border-t border-line",
        ),
        CTASection(
            headline="Want this on your data?",
            body="Signal is a public view. Our client engagements operate the same primitives over proprietary and regulated data — with the governance, access control and evaluation harness that regulated work requires.",
        ),
        body_extra=[
            Script(src="https://cdn.plot.ly/plotly-2.35.2.min.js"),
            Script(NotStr(f"window.PLOTLY_DATA = {signal_mod.as_json()};")),
            Script(src="/static/signal.js"),
        ],
    )


# ---------- /research ----------

@rt("/research")
def research():
    return page(
        "Research",
        "/research",
        Section_(
            Eyebrow("Research & open source"),
            Heading(1, "Commoditised capability goes to the commons.", cls="mt-5 max-w-4xl"),
            P("Our reference implementations for public-sector problems live on GitHub. Clients get the specific engagement; the method stays in the community so the next buyer can verify it.",
              cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow("Repositories"),
                Heading(2, "Open-source toolkits.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                *[
                    A(
                        Div(
                            Div(
                                Span(r["name"], cls="font-mono text-ink text-sm"),
                                Span(r["relevance"], cls=f"ml-auto text-[10px] font-mono tracking-widest px-2 py-0.5 rounded-full border {'border-accent text-accent' if r['relevance']=='HIGH' else 'border-line text-ink-muted'}"),
                                cls="flex items-center mb-4",
                            ),
                            P(r["tagline"], cls="text-ink-muted text-sm leading-relaxed mb-4"),
                            Div(*[Pill(t) for t in r["tags"]], cls="flex flex-wrap gap-2"),
                            cls="p-6 rounded-2xl bg-bg-elevated border border-line hover:border-accent/50 transition-colors h-full",
                        ),
                        href=r["url"],
                        target="_blank",
                        cls="block",
                    )
                    for r in REPOS
                ],
                cls="grid md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
        ),
        Section_(
            Div(
                Eyebrow("Research platforms"),
                Heading(2, "Running research on live markets.", cls="mt-4 max-w-3xl"),
                cls="mb-14",
            ),
            Div(
                *[
                    A(
                        Div(
                            Heading(3, r["name"], cls="mb-3"),
                            P(r["tagline"], cls="text-ink-muted text-sm leading-relaxed mb-5"),
                            Div(
                                Span("Visit ", cls="text-accent text-sm"),
                                Span("→", cls="text-accent text-sm"),
                            ),
                            cls="p-6 rounded-2xl bg-bg-elevated border border-line hover:border-accent/50 transition-colors h-full",
                        ),
                        href=r["url"],
                        target="_blank",
                        cls="block",
                    )
                    for r in EXTERNAL_RESEARCH
                ],
                cls="grid md:grid-cols-2 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        CTASection(),
    )


# ---------- /team ----------

@rt("/team")
def team():
    return page(
        "Team",
        "/team",
        Section_(
            Eyebrow("Team"),
            Heading(1, "A small group, bound by the discipline the work demands.", cls="mt-5 max-w-4xl"),
            P("We are deliberately small — senior engineers and scientists who own delivery end-to-end. We extend through a vetted partner network when a programme needs specialist clearance, language or capacity.",
              cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                *[_member_card(m) for m in TEAM],
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
        CTASection(headline="Looking to join us?", body="We work with hand-picked partners and occasional specialist contractors. If your background fits the capabilities on this site, tell us.", cta_label="Write to us"),
    )


def _member_card(m):
    return Article(
        Div(
            Div(m["initials"], cls="w-14 h-14 rounded-full bg-bg-raised border border-line flex items-center justify-center text-ink font-mono text-sm"),
            Div(
                Heading(3, m["name"], cls="mb-1"),
                P(m["role"], cls="text-accent text-sm font-mono"),
            ),
            cls="flex items-center gap-4 mb-5",
        ),
        P(m["bio"], cls="text-ink-muted leading-relaxed mb-6"),
        A(
            Span("LinkedIn", cls="text-sm"),
            Span("→", cls="text-sm"),
            href=m["linkedin"],
            target="_blank",
            cls="inline-flex items-center gap-2 text-ink hover:text-accent transition-colors",
        ),
        cls="p-8 rounded-2xl bg-bg-elevated border border-line",
    )


# ---------- /contact ----------

@rt("/contact")
def contact():
    return page(
        "Contact",
        "/contact",
        Section_(
            Eyebrow("Contact"),
            Heading(1, "Brief us on the programme.", cls="mt-5 max-w-4xl"),
            P("We work with public-sector buyers across the UK, the Nordics, the Benelux and the Baltics, and selectively with regulated enterprise clients. Tell us the problem — we'll tell you if we can help.",
              cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                Div(
                    Eyebrow("Write to us"),
                    Heading(2, CONTACT_EMAIL, cls="mt-4 break-all"),
                    P("We read every brief personally. A short note on the buyer, the problem and the deadline is enough to start.",
                      cls="mt-5 text-ink-muted leading-relaxed"),
                    Div(
                        Button_("Email " + CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", primary=True),
                        cls="mt-8",
                    ),
                    cls="p-10 rounded-2xl bg-bg-elevated border border-line",
                ),
                Div(
                    Div(
                        H3("Estonian entity", cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        P("Manmouna OÜ", cls="text-ink"),
                        P("Teelise tn 10, Nõmme linnaosa", cls="text-ink-muted"),
                        P("Tallinn, 10916", cls="text-ink-muted"),
                        P("Estonia", cls="text-ink-muted"),
                        P("Registry code 16289310", cls="text-ink-dim text-sm mt-3 font-mono"),
                        cls="mb-10",
                    ),
                    Div(
                        H3("Registered office", cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        P("Predictive Labs Ltd", cls="text-ink"),
                        P("155 Minories Street, Suite 275", cls="text-ink-muted"),
                        P("London, EC3N 1AD", cls="text-ink-muted"),
                        P("United Kingdom", cls="text-ink-muted"),
                        P("Company no. 14857334", cls="text-ink-dim text-sm mt-3 font-mono"),
                        cls="mb-10",
                    ),
                    Div(
                        H3("Channels", cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        A("GitHub", href=GITHUB_URL, target="_blank", cls="block text-ink hover:text-accent mb-2"),
                        A("LinkedIn", href=LINKEDIN_URL, target="_blank", cls="block text-ink hover:text-accent mb-2"),
                    ),
                    cls="p-10 rounded-2xl bg-bg-elevated border border-line",
                ),
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
    )


if __name__ == "__main__":
    serve()
