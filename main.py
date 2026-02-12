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

.footer {
    background: #2C4A3A;
    color: white;
    padding: 3rem 0 1.5rem;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3rem;
    margin-bottom: 2rem;
}

.footer-section h3 {
    color: white;
    font-size: 1.2rem;
    margin-bottom: 1rem;
    font-weight: 600;
}

.footer-section p {
    color: #bfdbfe;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 0.5rem;
}

.footer-section a {
    color: #bfdbfe;
    text-decoration: none;
    display: block;
    margin-bottom: 0.5rem;
    transition: color 0.3s ease;
}

.footer-section a:hover {
    color: white;
}

.social-links {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.social-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    color: white;
    text-decoration: none;
    font-size: 1.2rem;
    transition: background 0.3s ease;
}

.social-icon:hover {
    background: rgba(255, 255, 255, 0.2);
}

.footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 1.5rem;
    text-align: center;
    color: #bfdbfe;
    font-size: 0.875rem;
}

.team-card {
    background: white;
    border-radius: 0.75rem;
    padding: 2rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    border: 1px solid #e5e7eb;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.team-card h3 {
    font-size: 1.3rem;
    color: #2D2D2D;
    margin-bottom: 0.5rem;
    font-weight: 600;
}

.team-card .role {
    color: #4A7C59;
    font-size: 1rem;
    margin-bottom: 1rem;
    font-weight: 500;
}

.linkedin-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: #0077B5;
    text-decoration: none;
    font-weight: 500;
    transition: opacity 0.3s ease;
}

.linkedin-link:hover {
    opacity: 0.7;
}

.linkedin-icon {
    width: 24px;
    height: 24px;
    fill: #0077B5;
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
                Li(A("Research", href="#research")),
                Li(A("Team", href="#team")),
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

def Research():
    projects = [
        ("Finesspresso", "https://research.finespresso.org/", "Advanced financial research platform leveraging AI for market analysis, sentiment tracking, and quantitative insights."),
        ("Reinforcement Learning", "https://rl-agents-v2.finespresso.org/login", "Interactive RL agents platform for training and deploying reinforcement learning models in financial trading environments."),
        ("Hedgefolio", "https://github.com/predictivelabsai/hedgefolio/", "Open-source portfolio optimization framework using modern portfolio theory and machine learning for risk-adjusted returns."),
        ("Fincode", "https://github.com/predictivelabsai/fincode", "Python library for financial data analysis, backtesting, and algorithmic trading strategy development.")
    ]
    
    return Section(
        Div(
            H2("Research & Open Source"),
            P("Explore our research initiatives and open-source contributions to the AI and finance communities."),
            Div(
                *[Div(
                    H3(name),
                    P(desc),
                    A("Learn More →", href=url, target="_blank", style="color: #4A7C59; font-weight: 600; text-decoration: none;"),
                    cls="card"
                ) for name, url, desc in projects],
                cls="grid grid-4"
            ),
            cls="container"
        ),
        cls="section bg-light",
        id="research"
    )

def Team():
    # LinkedIn icon SVG
    linkedin_svg = '''<svg class="linkedin-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'''
    
    team_members = [
        ("Julian Kaljuvee", "AI Engineer", "https://www.linkedin.com/in/juliankaljuvee/"),
        ("Raslen Guesmi", "Data Scientist / Machine Learning Engineer", "https://www.linkedin.com/in/raslen-guesmi/"),
        ("Siwei Feng", "AI Engineer / Data Scientist", "https://www.linkedin.com/in/siwei-feng-28488a398/"),
        ("Chenhao Xue", "Quantitative Research Consultant", "https://www.linkedin.com/in/chenhao-xue-68b93a1a3/")
    ]
    
    return Section(
        Div(
            H2("Our Team"),
            P("Meet the experts driving innovation at Predictive Labs."),
            Div(
                *[Div(
                    H3(name),
                    Div(role, cls="role"),
                    A(
                        NotStr(linkedin_svg),
                        Span("LinkedIn"),
                        href=linkedin,
                        target="_blank",
                        cls="linkedin-link"
                    ),
                    cls="team-card"
                ) for name, role, linkedin in team_members],
                cls="grid grid-4"
            ),
            cls="container"
        ),
        cls="section",
        id="team"
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

def PageFooter():
    return Div(
        Div(
            Div(
                Div(
                    H3("Predictive Labs"),
                    P("Transforming enterprises with cutting-edge AI and GenAI solutions."),
                    Div(
                        A("🔗", href="https://www.linkedin.com/company/predictive-labs-ltd/", target="_blank", cls="social-icon", title="LinkedIn"),
                        A("💻", href="https://github.com/predictivelabsai/", target="_blank", cls="social-icon", title="GitHub"),
                        cls="social-links"
                    ),
                    cls="footer-section"
                ),
                Div(
                    H3("Company"),
                    P("155 Minories Street, Suite 275"),
                    P("London, EC3N 1AD"),
                    P("United Kingdom"),
                    P("Company Number: 14857334"),
                    cls="footer-section"
                ),
                Div(
                    H3("Research"),
                    A("Finesspresso", href="https://research.finespresso.org/", target="_blank"),
                    A("Reinforcement Learning", href="https://rl-agents-v2.finespresso.org/login", target="_blank"),
                    A("Hedgefolio", href="https://github.com/predictivelabsai/hedgefolio/", target="_blank"),
                    A("Fincode", href="https://github.com/predictivelabsai/fincode", target="_blank"),
                    cls="footer-section"
                ),
                Div(
                    H3("Contact"),
                    A("info@predictivelabs.ai", href="mailto:info@predictivelabs.ai"),
                    cls="footer-section"
                ),
                cls="footer-grid container"
            ),
            Div(
                P("© 2026 Predictive Labs Ltd. All rights reserved."),
                cls="footer-bottom container"
            ),
            cls="container"
        ),
        cls="footer"
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
                Research(),
                Div(cls="divider"),
                Team(),
                Div(cls="divider"),
                Contact(),
                cls="main-content"
            ),
            PageFooter()
        )
    )

if __name__ == "__main__":
    serve()
