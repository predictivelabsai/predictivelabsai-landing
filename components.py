"""
Shared FastHTML components for the Predictive Labs landing site.

Design tokens come from Tailwind via CDN with a dark-first palette extended in
a small inline config block. Custom CSS for the three.js canvas container and
scroll-reveal lives in static/site.css.
"""

from fasthtml.common import (
    Html, Head, Body, Meta, Title, Link, Script, Style, NotStr,
    Nav, Main, Footer, Header, Section, Article, Aside, Div, Span, A, Img, Svg,
    H1, H2, H3, H4, H5, H6, P, Ul, Ol, Li, Button, Small, Strong, Em, I,
    Video, Source,
)

SITE_NAME = "Predictive Labs"
SITE_TAGLINE = "AI for public outcomes."
CONTACT_EMAIL = "info@predictivelabs.ai"
GITHUB_URL = "https://github.com/predictivelabsai"
LINKEDIN_URL = "https://www.linkedin.com/company/predictive-labs-ltd/"

NAV_ITEMS = [
    ("Platform", "/platform"),
    ("Solutions", None, [
        ("Defense & public security", "/solutions/defense"),
        ("Health & life sciences", "/solutions/healthcare"),
        ("Public management & mobility", "/solutions/public"),
        ("Financial services", "/solutions/financial"),
    ]),
    ("Case studies", "/case-studies"),
    ("Signal", "/signal"),
    ("Research", "/research"),
    ("Team", "/team"),
    ("Contact", "/contact"),
]


TAILWIND_CONFIG = """
tailwind.config = {
  theme: {
    extend: {
      colors: {
        bg: { DEFAULT: '#0D2A70', elevated: '#163A8C', raised: '#1F4BAC' },
        ink: { DEFAULT: '#F5F5F7', muted: '#C2CEE8', dim: '#95A5D1' },
        line: { DEFAULT: '#2B4A8E', bright: '#3A60B2' },
        accent: { DEFAULT: '#5EEAD4', dim: '#1E3A3A', deep: '#134E4A' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
      },
      letterSpacing: {
        tightest: '-0.04em',
        tighter: '-0.025em',
      },
    },
  },
};
"""


def Eyebrow(text, *, href=None):
    cls = "font-mono text-[11px] tracking-[0.18em] uppercase text-accent"
    if href:
        return A(text, href=href, cls=cls + " hover:text-ink transition-colors")
    return Span(text, cls=cls)


# Map of sector keywords to canonical destination pages. Used by SectorLink()
# to keep cross-links consistent across the site.
SECTOR_HREF = {
    "health": "/solutions/healthcare",
    "healthcare": "/solutions/healthcare",
    "hospital": "/solutions/healthcare",
    "clinical": "/solutions/healthcare",
    "defense": "/solutions/defense",
    "defence": "/solutions/defense",
    "public management": "/solutions/public",
    "mobility": "/solutions/public",
    "municipal": "/solutions/public",
    "financial": "/solutions/financial",
    # These don't yet have dedicated solution pages — point to Signal where
    # we show sector data publicly.
    "energy": "/signal",
    "education": "/signal",
}


def SectorLink(label: str, *, sector: str | None = None, cls: str = ""):
    """Inline prose link. Looks up SECTOR_HREF by sector key (or by label
    lowercased if sector omitted). Styled as a subtle underline so prose
    reads naturally but a reader can see it's navigable."""
    key = (sector or label).lower().strip()
    href = SECTOR_HREF.get(key)
    if href is None:
        return Span(label)
    return A(
        label,
        href=href,
        cls=f"text-ink underline decoration-accent/50 decoration-1 underline-offset-4 hover:decoration-accent hover:text-accent transition-colors {cls}".strip(),
    )


def Heading(level, text, *, cls=""):
    tag = {1: H1, 2: H2, 3: H3, 4: H4}[level]
    base = {
        1: "text-4xl sm:text-5xl md:text-7xl font-medium tracking-tightest text-ink leading-[1.05] md:leading-[1.02]",
        2: "text-2xl sm:text-3xl md:text-5xl font-medium tracking-tighter text-ink leading-[1.12] md:leading-[1.08]",
        3: "text-lg sm:text-xl md:text-2xl font-medium tracking-tight text-ink",
        4: "text-base md:text-lg font-medium text-ink",
    }[level]
    return tag(text, cls=f"{base} {cls}".strip())


def Body_(text, *, cls="", muted=True):
    tone = "text-ink-muted" if muted else "text-ink"
    return P(text, cls=f"text-base md:text-lg leading-relaxed {tone} {cls}".strip())


def Button_(text, *, href="#", primary=True, cls=""):
    base = "inline-flex items-center gap-2 px-5 py-3 rounded-full text-sm font-medium transition-all duration-200"
    if primary:
        style = "bg-accent text-bg hover:bg-ink shadow-[0_0_0_1px_#5EEAD4] hover:shadow-[0_0_0_1px_#F5F5F7]"
    else:
        style = "bg-transparent text-ink border border-line-bright hover:border-accent hover:text-accent"
    return A(text, Span("→", cls="text-base"), href=href, cls=f"{base} {style} {cls}".strip())


def Pill(text, *, cls=""):
    return Span(
        text,
        cls=f"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono tracking-wider uppercase text-ink-muted bg-bg-elevated border border-line {cls}".strip(),
    )


def Navbar(current_path: str = "/"):
    def _nav_item(item):
        if len(item) == 2:
            label, href = item
            active = current_path == href
            return Li(
                A(
                    label,
                    href=href,
                    cls=f"text-sm text-ink-muted hover:text-ink transition-colors {'text-ink' if active else ''}",
                )
            )
        label, _, children = item
        return Li(
            Div(
                Span(label, cls="text-sm text-ink-muted hover:text-ink transition-colors flex items-center gap-1 cursor-default"),
                Span("▾", cls="text-xs text-ink-dim"),
                cls="flex items-center gap-1",
            ),
            Ul(
                *[
                    Li(
                        A(
                            sub_label,
                            href=sub_href,
                            cls="block px-4 py-2 text-sm text-ink-muted hover:text-ink hover:bg-bg-raised",
                        )
                    )
                    for sub_label, sub_href in children
                ],
                cls="absolute right-0 mt-3 w-64 rounded-xl border border-line bg-bg-elevated py-2 shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200",
            ),
            cls="relative group",
        )

    # Flatten nav items for the mobile menu
    def _flat_mobile():
        out = []
        for item in NAV_ITEMS:
            if len(item) == 2:
                out.append(item)
            else:
                label, _, children = item
                out.append((label, None))  # section label
                out.extend(children)
        return out

    mobile_items = [
        Li(Span(lbl, cls="block text-xs font-mono tracking-widest uppercase text-ink-dim pt-3"))
        if href is None
        else Li(A(lbl, href=href, cls=f"block py-2 text-base {'text-accent' if current_path == href else 'text-ink hover:text-accent'}"))
        for lbl, href in _flat_mobile()
    ]

    return Nav(
        Div(
            A(
                Span("◆", cls="text-accent mr-2"),
                Span(SITE_NAME, cls="font-medium tracking-tight"),
                href="/",
                cls="flex items-center text-ink text-base hover:text-accent transition-colors",
            ),
            Ul(
                *[_nav_item(i) for i in NAV_ITEMS],
                cls="hidden lg:flex items-center gap-7",
            ),
            A(
                "Talk to us",
                href="/contact",
                cls="hidden lg:inline-flex items-center gap-2 px-4 py-2 rounded-full text-xs font-medium bg-ink text-bg hover:bg-accent transition-colors",
            ),
            Button(
                Span("☰", id="nav-burger-icon", cls="text-2xl leading-none"),
                type="button",
                aria_label="Open menu",
                onclick=(
                    "const m=document.getElementById('mobile-nav');"
                    "const i=document.getElementById('nav-burger-icon');"
                    "const open=m.classList.toggle('hidden')===false;"
                    "i.textContent=open?'✕':'☰';"
                ),
                cls="lg:hidden text-ink hover:text-accent w-10 h-10 flex items-center justify-center rounded-full border border-line",
            ),
            cls="max-w-7xl mx-auto px-5 md:px-6 flex items-center justify-between h-16 gap-4",
        ),
        Div(
            Ul(*mobile_items, cls="px-5 pb-5 pt-2 space-y-1"),
            Div(
                A(
                    "Talk to us",
                    href="/contact",
                    cls="block text-center px-4 py-3 rounded-full text-sm font-medium bg-accent text-bg mx-5 mb-5",
                ),
            ),
            id="mobile-nav",
            cls="hidden lg:hidden border-t border-line bg-bg-elevated",
        ),
        cls="sticky top-0 z-50 backdrop-blur-md bg-bg/80 border-b border-line",
    )


def Section_(*content, bleed=False, cls=""):
    inner_cls = "max-w-7xl mx-auto px-5 md:px-6" if not bleed else "w-full"
    return Section(Div(*content, cls=inner_cls), cls=f"py-14 md:py-20 lg:py-28 {cls}".strip())


def Footer_():
    columns = [
        ("Platform", [
            ("Overview", "/platform"),
            ("Case studies", "/case-studies"),
            ("Signal", "/signal"),
            ("Research", "/research"),
        ]),
        ("Solutions", [
            ("Defense & public security", "/solutions/defense"),
            ("Health & life sciences", "/solutions/healthcare"),
            ("Public management & mobility", "/solutions/public"),
            ("Financial services", "/solutions/financial"),
        ]),
        ("Company", [
            ("Team", "/team"),
            ("Contact", "/contact"),
            ("GitHub", GITHUB_URL),
            ("LinkedIn", LINKEDIN_URL),
        ]),
    ]

    col_divs = [
        Div(
            H4(title, cls="text-xs font-mono tracking-[0.18em] uppercase text-ink-muted mb-5"),
            Ul(
                *[Li(A(label, href=href, cls="text-sm text-ink hover:text-accent transition-colors"), cls="mb-2") for label, href in links],
                cls="space-y-2",
            ),
        )
        for title, links in columns
    ]

    return Footer(
        Div(
            Div(
                Div(
                    A(
                        Span("◆", cls="text-accent mr-2"),
                        Span(SITE_NAME, cls="font-medium text-ink tracking-tight"),
                        href="/",
                        cls="flex items-center text-lg mb-4",
                    ),
                    P(SITE_TAGLINE, cls="text-ink-muted text-sm max-w-xs mb-5 leading-relaxed"),
                    P(
                        "Manmouna OÜ · Registry code 16289310", NotStr("<br>"),
                        "Teelise tn 10, Tallinn, 10916, Estonia",
                        cls="text-ink-dim text-xs leading-relaxed",
                    ),
                ),
                *col_divs,
                cls="grid grid-cols-2 md:grid-cols-4 gap-10",
            ),
            Div(
                Div(f"© {__import__('datetime').datetime.now().year} Manmouna OÜ t/a Predictive Labs.", cls="text-ink-dim text-xs"),
                Div(
                    A("GitHub", href=GITHUB_URL, cls="text-ink-dim text-xs hover:text-accent mr-4"),
                    A("LinkedIn", href=LINKEDIN_URL, cls="text-ink-dim text-xs hover:text-accent mr-4"),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", cls="text-ink-dim text-xs hover:text-accent break-all"),
                    cls="flex items-center flex-wrap gap-y-2",
                ),
                cls="mt-10 md:mt-14 pt-6 border-t border-line flex items-start md:items-center justify-between flex-wrap gap-4",
            ),
            cls="max-w-7xl mx-auto px-5 md:px-6",
        ),
        cls="py-12 md:py-16 border-t border-line bg-bg-elevated",
    )


def page(title: str, current_path: str = "/", *content, head_extra=None, body_extra=None):
    head_children = [
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Meta(name="description", content=f"{SITE_NAME} — {SITE_TAGLINE}"),
        Title(f"{title} · {SITE_NAME}"),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap",
        ),
        Script(src="https://cdn.tailwindcss.com"),
        Script(NotStr(TAILWIND_CONFIG)),
        Link(rel="stylesheet", href="/static/site.css"),
    ]
    if head_extra:
        head_children.extend(head_extra if isinstance(head_extra, list) else [head_extra])

    body_children = [
        Navbar(current_path),
        Main(*content, cls="min-h-screen"),
        Footer_(),
    ]
    if body_extra:
        body_children.extend(body_extra if isinstance(body_extra, list) else [body_extra])

    return Html(
        Head(*head_children),
        Body(*body_children, cls="bg-bg text-ink font-sans antialiased"),
        lang="en",
    )


# ---------- Higher-level building blocks ----------

def Hero(*, eyebrow="AI for public outcomes", headline=None, lede=None, ctas=None, canvas=True, tall=True):
    headline = headline or (Span("Decisions made "), Span("with evidence,", cls="text-accent"), Span(" at the scale of the public good."))
    lede = lede or (
        "Predictive Labs builds AI systems for European public services — in ",
        SectorLink("health"), ", ",
        SectorLink("defense"), ", ",
        SectorLink("public management"), " and ",
        SectorLink("mobility"),
        " — that are auditable by design and open where they can be.",
    )
    ctas = ctas or [("See what we build", "/platform", True), ("Talk to us", "/contact", False)]

    height = "min-h-[82vh] md:min-h-[88vh]" if tall else "min-h-[56vh] md:min-h-[60vh]"

    canvas_div = Div(id="three-hero", cls="absolute inset-0 z-10 opacity-60 pointer-events-none") if canvas else None

    video_div = Video(
        Source(src="/static/video/hero-bg-720.mp4", type="video/mp4"),
        autoplay=True,
        muted=True,
        loop=True,
        playsinline=True,
        preload="metadata",
        poster="/static/video/hero-bg-poster.jpg",
        id="hero-video",
        cls="absolute inset-0 w-full h-full object-cover z-0 opacity-55 pointer-events-none",
    )

    lede_nodes = lede if isinstance(lede, tuple) else (lede,)

    return Section(
        Div(
            video_div,
            canvas_div,
            Div(cls="absolute inset-0 z-20 bg-gradient-to-b from-bg/40 via-transparent to-bg pointer-events-none"),
            Div(
                Eyebrow(eyebrow),
                H1(*headline if isinstance(headline, tuple) else [headline], cls="mt-5 md:mt-6 text-[40px] sm:text-5xl md:text-7xl lg:text-[84px] font-medium tracking-tightest text-ink leading-[1.05] md:leading-[1.02] max-w-5xl"),
                P(*lede_nodes, cls="mt-6 md:mt-8 text-base md:text-xl text-ink-muted max-w-2xl leading-relaxed"),
                Div(
                    *[Button_(text, href=href, primary=primary) for text, href, primary in ctas],
                    cls="mt-8 md:mt-10 flex items-center gap-3 flex-wrap",
                ),
                cls="relative z-30 max-w-7xl mx-auto px-5 md:px-6 py-16 md:py-0",
            ),
            cls=f"relative {height} flex items-center overflow-hidden bg-bg",
        ),
        Div(
            Div(
                Div("AI for public outcomes", cls="text-[11px] md:text-xs font-mono tracking-[0.18em] uppercase text-ink-dim"),
                Div(
                    Span("Active engagements across ", cls="text-ink-muted text-xs md:text-sm"),
                    Span("6 ", cls="text-accent text-xs md:text-sm font-mono"),
                    Span("European public-sector programmes", cls="text-ink-muted text-xs md:text-sm"),
                ),
                cls="max-w-7xl mx-auto px-5 md:px-6 py-4 md:py-5 flex items-center justify-between flex-wrap gap-3",
            ),
            cls="border-y border-line bg-bg-elevated/60",
        ),
    )


def Pillar(number: str, title: str, body: str, *, icon="◆"):
    return Div(
        Div(
            Span(icon, cls="text-accent text-xl"),
            Span(number, cls="font-mono text-xs tracking-widest text-ink-dim ml-auto"),
            cls="flex items-center mb-6",
        ),
        Heading(3, title, cls="mb-3"),
        P(body, cls="text-ink-muted text-sm leading-relaxed"),
        cls="p-7 rounded-2xl bg-bg-elevated border border-line hover:border-accent/50 transition-colors group",
    )


def MetricTile(value, unit, caption, *, cls=""):
    return Div(
        Div(
            Span(value, cls="text-4xl md:text-5xl font-medium tracking-tighter text-ink"),
            Span(unit, cls="text-lg text-accent ml-1"),
            cls="flex items-baseline",
        ),
        P(caption, cls="text-ink-muted text-sm mt-2"),
        cls=f"p-6 rounded-2xl bg-bg-elevated border border-line {cls}".strip(),
    )


def CaseStudyCard(cs, *, compact=False):
    tech = Div(
        *[Pill(t) for t in cs.get("tech", [])[:6]],
        cls="flex flex-wrap gap-2 mt-5",
    )
    return Article(
        Div(
            Span(cs["flag"], cls="text-xl mr-2"),
            Span(cs["country"], cls="text-xs font-mono tracking-widest text-ink-muted uppercase"),
            Span("·", cls="text-ink-dim mx-2"),
            Span(cs["sector"], cls="text-xs font-mono tracking-widest text-ink-muted uppercase"),
            Span(cs["status"], cls="ml-auto text-xs font-mono text-accent px-2 py-1 rounded-full border border-accent/40"),
            cls="flex items-center mb-5",
        ),
        Heading(3, cs["title"], cls="mb-2"),
        P(cs["buyer"], cls="text-ink-muted text-sm font-mono mb-5"),
        Div(
            Div(
                Div("Problem", cls="text-[10px] font-mono tracking-widest uppercase text-ink-dim mb-1"),
                P(cs["problem"], cls="text-ink-muted text-sm leading-relaxed"),
                cls="mb-4",
            ),
            Div(
                Div("Approach", cls="text-[10px] font-mono tracking-widest uppercase text-ink-dim mb-1"),
                P(cs["approach"], cls="text-ink text-sm leading-relaxed"),
                cls="mb-4",
            ),
            Div(
                Div("Capability", cls="text-[10px] font-mono tracking-widest uppercase text-ink-dim mb-1"),
                P(cs["capability"], cls="text-ink-muted text-sm leading-relaxed italic"),
            ) if not compact else None,
        ),
        tech if not compact else None,
        cls="p-7 rounded-2xl bg-bg-elevated border border-line hover:border-accent/40 transition-colors",
    )


def NewsSection(*, category: str, title: str = "From the feed",
                subtitle: str | None = None, eyebrow: str = "News"):
    """Render a compact news block. Items are pulled from content/news.py's
    in-memory cache; if empty (cold start, before the background refresher
    has populated the cache) the section is hidden entirely so we never
    show an empty shell."""
    from content import news as _news

    items = _news.items_for(category)
    if not items:
        return Div()  # empty placeholder — hidden via absence of children

    def _item(it):
        pub = _news.format_published(it.get("published"))
        meta = [Span(it["source"], cls="text-ink-dim text-xs font-mono")]
        if pub:
            meta.append(Span("·", cls="text-ink-dim text-xs mx-2"))
            meta.append(Span(pub, cls="text-ink-dim text-xs"))
        return A(
            Div(
                H4(it["title"], cls="text-ink text-base md:text-lg font-medium leading-snug mb-3 group-hover:text-accent transition-colors"),
                Div(*meta, cls="flex items-center flex-wrap"),
                cls="p-5 md:p-6 h-full rounded-2xl bg-bg-elevated border border-line group-hover:border-accent/60 transition-colors",
            ),
            href=it["url"],
            target="_blank",
            rel="noopener",
            cls="block group",
        )

    last = _news.last_refresh_iso()

    return Section_(
        Div(
            Div(
                Eyebrow(eyebrow),
                Heading(2, title, cls="mt-4 max-w-3xl"),
                P(subtitle, cls="mt-4 text-ink-muted max-w-2xl leading-relaxed") if subtitle else None,
                cls="md:flex-1",
            ),
            Div(
                Span("Refreshed hourly from public RSS + Atom feeds.",
                     cls="text-ink-dim text-xs"),
                Span(NotStr("&nbsp;·&nbsp;") + f"Last refresh: {last}" if last else "",
                     cls="text-ink-dim text-xs"),
                cls="text-left md:text-right md:max-w-xs mt-4 md:mt-0",
            ),
            cls="mb-10 flex flex-col md:flex-row md:items-end md:justify-between gap-4",
        ),
        Div(
            *[_item(it) for it in items],
            cls="grid md:grid-cols-2 gap-4",
        ),
        cls="border-t border-line",
    )


def CTASection(*, headline="Brief us on your programme.", body="We work with public-sector buyers in the UK, the Nordics, the Benelux and the Baltics. Tell us the problem — we'll tell you if we can help.", cta_label="Start the conversation", cta_href="/contact"):
    return Section(
        Div(
            Div(
                Eyebrow("Engage"),
                Heading(2, headline, cls="mt-4 max-w-3xl"),
                P(body, cls="mt-5 text-ink-muted text-lg max-w-2xl leading-relaxed"),
                Div(
                    Button_(cta_label, href=cta_href, primary=True),
                    Button_("See case studies", href="/case-studies", primary=False),
                    cls="mt-8 flex items-center gap-3 flex-wrap",
                ),
                cls="max-w-7xl mx-auto px-6 py-20 md:py-28 relative z-10",
            ),
            Div(cls="absolute inset-0 bg-gradient-to-br from-accent/5 via-transparent to-transparent pointer-events-none"),
            cls="relative border-y border-line bg-bg-elevated/60 overflow-hidden",
        ),
    )
