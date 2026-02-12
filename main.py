from fasthtml.common import *

# CSS for styling - Predictive Labs color scheme
css = """
/* Tailwind-inspired CSS with Predictive Labs colors */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #2D2D2D;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.hero {
    background: #F5F1E8;
    min-height: 80vh;
    display: flex;
    align-items: center;
    text-align: center;
    padding: 4rem 0;
}

.hero h1 {
    font-size: 3.5rem;
    font-weight: 400;
    color: #2D2D2D;
    margin-bottom: 1.5rem;
    line-height: 1.2;
    font-family: Georgia, serif;
}

.hero .tagline {
    color: #4A7C59;
    display: block;
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
}

.hero p {
    font-size: 1.25rem;
    color: #666666;
    margin-bottom: 2rem;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.8;
}

.badge {
    display: inline-block;
    background: #E8F5E9;
    color: #2C4A3A;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-size: 0.875rem;
    margin-bottom: 1.5rem;
}

.btn {
    display: inline-block;
    padding: 0.75rem 2rem;
    border-radius: 0.5rem;
    text-decoration: none;
    font-weight: 500;
    margin: 0 0.5rem;
    transition: all 0.3s ease;
}

.btn-primary {
    background: #4A7C59;
    color: white;
}

.btn-primary:hover {
    background: #3A6249;
}

.section {
    padding: 4rem 0;
}

.section h2 {
    font-size: 2.5rem;
    font-weight: 400;
    color: #2D2D2D;
    text-align: center;
    margin-bottom: 1rem;
    font-family: Georgia, serif;
}

.section p {
    text-align: center;
    color: #666666;
    font-size: 1.125rem;
    max-width: 800px;
    margin: 0 auto 3rem;
}

.grid {
    display: grid;
    gap: 2rem;
}

.grid-4 {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.grid-2 {
    grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
}

.card {
    background: white;
    border-radius: 0.75rem;
    padding: 2rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    border: 1px solid #e5e7eb;
}

.card h3 {
    font-size: 1.3rem;
    color: #2D2D2D;
    margin-bottom: 1rem;
    font-weight: 600;
}

.card p {
    color: #666666;
    line-height: 1.7;
    text-align: left;
}

.numbered-card {
    background: white;
    border-radius: 0.75rem;
    padding: 2rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    border: 1px solid #e5e7eb;
}

.numbered-card .number {
    font-size: 2rem;
    color: #666666;
    font-weight: 300;
    margin-bottom: 1rem;
}

.numbered-card h3 {
    font-size: 1.3rem;
    color: #2D2D2D;
    margin-bottom: 1rem;
    font-weight: 600;
}

.numbered-card p {
    color: #666666;
    line-height: 1.7;
}

.feature-card {
    text-align: center;
    background: white;
    border-radius: 0.75rem;
    padding: 2rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.feature-card h4 {
    font-size: 1.2rem;
    color: #2D2D2D;
    margin-bottom: 1rem;
    font-weight: 600;
}

.feature-card p {
    color: #666666;
    line-height: 1.6;
}

.bg-light {
    background: #F5F1E8;
}

.bg-dark {
    background: #2C4A3A;
    color: white;
    padding: 4rem 0;
}

.divider {
    background: #2C4A3A;
    height: 80px;
}

.contact-section {
    background: #F5F1E8;
    padding: 4rem 0;
    text-align: center;
}

.contact-section h2 {
    color: #2D2D2D;
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    font-family: Georgia, serif;
}

.contact-section p {
    color: #666666;
    font-size: 1.25rem;
    margin-bottom: 2rem;
}

.email-link {
    color: #4A7C59;
    text-decoration: none;
    font-weight: 600;
    border-bottom: 2px solid #4A7C59;
    padding-bottom: 2px;
}

.email-link:hover {
    opacity: 0.8;
}

.navbar {
    background: white;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    padding: 1rem 0;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: 600;
    color: #4A7C59;
    text-decoration: none;
}

.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
}

.nav-links a {
    text-decoration: none;
    color: #2D2D2D;
    font-weight: 500;
}

.nav-links a:hover {
    color: #4A7C59;
}

.main-content {
    margin-top: 80px;
}

@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.5rem;
    }
    
    .hero .tagline {
        font-size: 1.8rem;
    }
    
    .section h2 {
        font-size: 2rem;
    }
    
    .grid-4, .grid-2 {
        grid-template-columns: 1fr;
    }
    
    .nav-links {
        display: none;
    }
}
"""

# Create the FastHTML app
app, rt = fast_app(
    hdrs=[
        Style(css),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Title("Welcome to Predictive Labs")
    ]
)

def Navbar():
    return Nav(
        Div(
            A("Predictive Labs", href="#", cls="logo"),
            Ul(
                Li(A("Expertise", href="#expertise")),
                Li(A("Industries", href="#industries")),
                Li(A("Case Studies", href="#case-studies")),
                Li(A("Contact", href="#contact")),
                cls="nav-links"
            ),
            cls="container"
        ),
        cls="navbar"
    )

def Hero():
    return Section(
        Div(
            Div(
                Span("AI & GenAI Solutions", cls="badge"),
                H1(
                    "Welcome to Predictive Labs",
                    Span("Transforming Enterprises with AI Excellence", cls="tagline")
                ),
                P("At Predictive Labs, we specialize in delivering cutting-edge Artificial Intelligence and Generative AI (GenAI) solutions that drive business growth, optimize operations, and unlock new levels of insight. Our mission is to empower organizations with intelligent, scalable, and ethical AI systems that deliver measurable results."),
                cls="container"
            ),
            cls="hero"
        )
    )

def Expertise():
    services = [
        ("1", "Generative AI Development", "Custom AI model development, fine-tuning, and evaluation tailored to specific business needs."),
        ("2", "AI Strategy Consulting", "Guiding enterprises through AI adoption, including use case identification, strategy formulation, and roadmap creation."),
        ("3", "Data Science & Analytics", "Advanced data modeling, forecasting, and optimization strategies for various industries."),
        ("4", "AI Solution", "We benchmark and evaluate solutions against industry standards.")
    ]
    
    return Section(
        Div(
            H2("Our Expertise"),
            P("Comprehensive AI services powered by cutting-edge technology and deep industry expertise."),
            Div(
                *[Div(
                    Div(num, cls="number"),
                    H3(title),
                    P(desc),
                    cls="numbered-card"
                ) for num, title, desc in services],
                cls="grid grid-4"
            ),
            cls="container"
        ),
        cls="section bg-light",
        id="expertise"
    )

def Industries():
    industries = [
        ("Insurance", "AI-driven risk assessment, fraud detection, and claims optimization."),
        ("Financial Services", "Predictive analytics, sales forecasting, and financial process automation."),
        ("Pharma / Biotech / Health", "AI-powered bioinformatics, manufacturing optimization, and data-driven research insights."),
        ("Manufacturing", "Process optimization, predictive maintenance, and supply chain forecasting.")
    ]
    
    return Section(
        Div(
            H2("Industries We Serve"),
            P("Delivering specialized AI solutions across multiple high-impact sectors."),
            Div(
                *[Div(
                    H3(name),
                    P(desc),
                    cls="card"
                ) for name, desc in industries],
                cls="grid grid-4"
            ),
            cls="container"
        ),
        cls="section",
        id="industries"
    )

def CaseStudies():
    cases = [
        ("Microsoft (NASDAQ: MSFT)", "Enterprise GenAI Implementation", "We collaborated with Microsoft's European clients to implement advanced GenAI solutions, including Retrieval-Augmented Generation (RAG) systems. The projects involved model evaluation, fine-tuning for industry-specific applications, and ensuring robust performance across diverse enterprise scenarios."),
        ("ARM Holdings (NASDAQ: ARM)", "Revenue Prediction & Forecasting", "We built and deployed forecasting models for ARM Holdings to predict both royalty and non-royalty revenues via state-of-the-art (SOTA) time series models. By integrating external and alternative datasets, the models provided strategic foresight for revenue trends and enabled more informed business decisions."),
        ("Nando's", "Sales Forecasting & Data Infrastructure", "Our work with Nando's included developing a sophisticated data infrastructure, including a data lake that integrated diverse datasets such as POS, loyalty programs, rota schedules, weather, geolocation, and delivery data. We also implemented advanced demand forecasting models to optimize sales and inventory."),
        ("London Stock Exchange Group (LSEG)", "Market Risk & VaR Modeling", "Defined and developed a delta-gamma approximation VaR model post-acquisition of LCH.Clearnet. Optimized processing architecture using Spark and Hadoop technologies.")
    ]
    
    return Section(
        Div(
            H2("Sample Case Studies"),
            P("Proven track record of delivering impactful AI solutions for global enterprises."),
            Div(
                *[Div(
                    H3(company),
                    P(Strong("Project Focus: "), focus, style="margin-bottom: 0.5rem;"),
                    P(desc),
                    cls="card"
                ) for company, focus, desc in cases],
                cls="grid grid-2"
            ),
            cls="container"
        ),
        cls="section bg-light",
        id="case-studies"
    )

def TechStack():
    stack = [
        ("1", "Gen AI and Agentic AI", "LangGraph/Langchain, CrewAI, PydanticAI, AutoGen, HuggingFace, Smol Agents, Promptflow"),
        ("2", "ML / AI Libraries", "PyTorch, JAX, PyCaret, SciKit-Learn, spaCy / NLP, FB Prophet, Transformers; Foundational LLMs: OpenAI, Anthropic, LLama, Mistral, DeepSeek, GraphRAG"),
        ("3", "Databases/Big Data", "PostgreSQL, Presto, Athena, Redshift, BigQuery, MongoDB, Databricks, Snowflake"),
        ("4", "Cloud", "AWS, Azure, Google Cloud Platform (GCP), Fly, Railway, Render")
    ]
    
    return Section(
        Div(
            H2("Our Technology Stack"),
            P("Built on industry-leading platforms and frameworks for maximum performance and scalability."),
            Div(
                *[Div(
                    Div(num, cls="number"),
                    H3(title),
                    P(desc),
                    cls="numbered-card"
                ) for num, title, desc in stack],
                cls="grid grid-4"
            ),
            cls="container"
        ),
        cls="section"
    )

def WhyChoose():
    features = [
        ("✓", "Proven Expertise", "A track record of successful projects with global enterprises across multiple industries."),
        ("⚙", "Tailored Solutions", "Customized AI models and strategies aligned with business objectives."),
        ("🚀", "Innovation-Focused", "Constantly pushing the boundaries of what AI can achieve."),
        ("⚡", "Rapid AI Development", "We deliver via RAD - Rapid Application Development.")
    ]
    
    return Section(
        Div(
            H2("Why Choose Predictive Labs?"),
            P("Partner with a team that combines technical excellence with business acumen."),
            Div(
                *[Div(
                    Div(icon, cls="feature-icon"),
                    H4(title),
                    P(desc),
                    cls="feature-card"
                ) for icon, title, desc in features],
                cls="grid grid-4"
            ),
            cls="container"
        ),
        cls="section bg-light"
    )

def Contact():
    return Section(
        Div(
            H2("Let's Build Together"),
            P(
                "Ready to leverage the power of Generative AI and AI / ML in general for your business? Connect with us at ",
                A("info@predictivelabs.ai", href="mailto:info@predictivelabs.ai", cls="email-link"),
                " to explore how we can transform your challenges into opportunities."
            ),
            cls="container"
        ),
        cls="contact-section",
        id="contact"
    )

@rt("/")
def get():
    return Html(
        Head(
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title("Welcome to Predictive Labs"),
            Style(css)
        ),
        Body(
            Navbar(),
            Div(
                Hero(),
                Div(cls="divider"),
                Expertise(),
                Div(cls="divider"),
                Industries(),
                Div(cls="divider"),
                CaseStudies(),
                Div(cls="divider"),
                TechStack(),
                Div(cls="divider"),
                WhyChoose(),
                Div(cls="divider"),
                Contact(),
                cls="main-content"
            )
        )
    )

if __name__ == "__main__":
    serve()
