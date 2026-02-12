from fasthtml.common import *

# Color scheme inspired by Predictive Labs
colors = {
    'cream': '#F5F1E8',
    'dark_green': '#2C4A3A',
    'text_dark': '#2D2D2D',
    'text_light': '#666666',
    'accent': '#4A7C59'
}

# Custom CSS
css = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    body {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.6;
        color: {colors['text_dark']};
        background-color: {colors['cream']};
    }}
    
    .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }}
    
    .hero {{
        padding: 80px 20px;
        text-align: left;
    }}
    
    .hero h1 {{
        font-size: 3rem;
        font-weight: 400;
        margin-bottom: 30px;
        color: {colors['text_dark']};
        font-family: Georgia, serif;
    }}
    
    .hero h2 {{
        font-size: 2rem;
        font-weight: 300;
        margin-bottom: 30px;
        color: {colors['text_dark']};
    }}
    
    .hero p {{
        font-size: 1.1rem;
        line-height: 1.8;
        color: {colors['text_light']};
        max-width: 900px;
    }}
    
    .section {{
        padding: 60px 20px;
        background-color: {colors['cream']};
    }}
    
    .section-dark {{
        background-color: {colors['dark_green']};
        padding: 80px 20px;
    }}
    
    .section-title {{
        font-size: 2.5rem;
        font-weight: 400;
        margin-bottom: 50px;
        color: {colors['text_dark']};
        font-family: Georgia, serif;
    }}
    
    .grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 40px;
        margin-top: 40px;
    }}
    
    .grid-2 {{
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    }}
    
    .card {{
        background: white;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}
    
    .card h3 {{
        font-size: 1.3rem;
        margin-bottom: 15px;
        color: {colors['text_dark']};
        font-weight: 600;
    }}
    
    .card p {{
        color: {colors['text_light']};
        line-height: 1.7;
    }}
    
    .numbered-item {{
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }}
    
    .number {{
        font-size: 2rem;
        font-weight: 300;
        color: {colors['text_light']};
        min-width: 40px;
    }}
    
    .feature-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 30px;
        margin-top: 40px;
    }}
    
    .feature {{
        text-align: center;
    }}
    
    .feature-icon {{
        font-size: 3rem;
        margin-bottom: 20px;
    }}
    
    .feature h4 {{
        font-size: 1.2rem;
        margin-bottom: 15px;
        color: {colors['text_dark']};
        font-weight: 600;
    }}
    
    .feature p {{
        color: {colors['text_light']};
        line-height: 1.6;
    }}
    
    .cta {{
        text-align: center;
        padding: 60px 20px;
    }}
    
    .cta h2 {{
        font-size: 2.5rem;
        margin-bottom: 30px;
        color: {colors['text_dark']};
        font-family: Georgia, serif;
    }}
    
    .cta p {{
        font-size: 1.1rem;
        color: {colors['text_light']};
        margin-bottom: 30px;
    }}
    
    .email-link {{
        color: {colors['accent']};
        text-decoration: none;
        font-weight: 600;
        border-bottom: 2px solid {colors['accent']};
        padding-bottom: 2px;
    }}
    
    .email-link:hover {{
        opacity: 0.8;
    }}
    
    @media (max-width: 768px) {{
        .hero h1 {{
            font-size: 2rem;
        }}
        .hero h2 {{
            font-size: 1.5rem;
        }}
        .grid, .grid-2 {{
            grid-template-columns: 1fr;
        }}
    }}
"""

app, rt = fast_app(hdrs=(Style(css),))

@rt('/')
def get():
    return Html(
        Head(
            Title("Welcome to Predictive Labs"),
            Meta(name="description", content="Transforming Enterprises with AI Excellence"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        ),
        Body(
            # Hero Section
            Div(
                Div(
                    H1("Welcome to Predictive Labs"),
                    H2("Transforming Enterprises with AI Excellence"),
                    P("At Predictive Labs, we specialize in delivering cutting-edge Artificial Intelligence and Generative AI (GenAI) solutions that drive business growth, optimize operations, and unlock new levels of insight. Our mission is to empower organizations with intelligent, scalable, and ethical AI systems that deliver measurable results."),
                    cls="container"
                ),
                cls="hero"
            ),
            
            # Dark divider
            Div(cls="section-dark"),
            
            # Our Expertise Section
            Div(
                Div(
                    H2("Our Expertise", cls="section-title"),
                    Div(
                        Div(
                            Div(
                                Span("1", cls="number"),
                                Div(
                                    H3("Generative AI Development"),
                                    P("Custom AI model development, fine-tuning, and evaluation tailored to specific business needs.")
                                )
                            , cls="numbered-item"),
                            Div(
                                Span("2", cls="number"),
                                Div(
                                    H3("AI Strategy Consulting"),
                                    P("Guiding enterprises through AI adoption, including use case identification, strategy formulation, and roadmap creation.")
                                )
                            , cls="numbered-item"),
                            Div(
                                Span("3", cls="number"),
                                Div(
                                    H3("Data Science & Analytics"),
                                    P("Advanced data modeling, forecasting, and optimization strategies for various industries.")
                                )
                            , cls="numbered-item"),
                            Div(
                                Span("4", cls="number"),
                                Div(
                                    H3("AI Solution"),
                                    P("We benchmark and evaluate solutions against industry standards.")
                                )
                            , cls="numbered-item"),
                        )
                    ),
                    cls="container"
                ),
                cls="section"
            ),
            
            # Dark divider
            Div(cls="section-dark"),
            
            # Industries We Serve Section
            Div(
                Div(
                    H2("Industries We Serve", cls="section-title"),
                    Div(
                        Div(
                            H3("Insurance"),
                            P("AI-driven risk assessment, fraud detection, and claims optimization."),
                            cls="card"
                        ),
                        Div(
                            H3("Financial Services"),
                            P("Predictive analytics, sales forecasting, and financial process automation."),
                            cls="card"
                        ),
                        Div(
                            H3("Pharma / Biotech / Health"),
                            P("AI-powered bioinformatics, manufacturing optimization, and data-driven research insights."),
                            cls="card"
                        ),
                        Div(
                            H3("Manufacturing"),
                            P("Process optimization, predictive maintenance, and supply chain forecasting."),
                            cls="card"
                        ),
                        cls="grid"
                    ),
                    cls="container"
                ),
                cls="section"
            ),
            
            # Dark divider
            Div(cls="section-dark"),
            
            # Sample Case Studies Section
            Div(
                Div(
                    H2("Sample Case Studies", cls="section-title"),
                    Div(
                        Div(
                            H3("Microsoft (NASDAQ: MSFT)"),
                            P(Strong("Project Focus: "), "Enterprise GenAI Implementation"),
                            P("We collaborated with Microsoft's European clients to implement advanced GenAI solutions, including Retrieval-Augmented Generation (RAG) systems. The projects involved model evaluation, fine-tuning for industry-specific applications, and ensuring robust performance across diverse enterprise scenarios."),
                            cls="card"
                        ),
                        Div(
                            H3("ARM Holdings (NASDAQ: ARM)"),
                            P(Strong("Project Focus: "), "Revenue Prediction & Forecasting"),
                            P("We built and deployed forecasting models for ARM Holdings to predict both royalty and non-royalty revenues via state-of-the-art (SOTA) time series models. By integrating external and alternative datasets, the models provided strategic foresight for revenue trends and enabled more informed business decisions."),
                            cls="card"
                        ),
                        Div(
                            H3("Nando's"),
                            P(Strong("Project Focus: "), "Sales Forecasting & Data Infrastructure"),
                            P("Our work with Nando's included developing a sophisticated data infrastructure, including a data lake that integrated diverse datasets such as POS, loyalty programs, rota schedules, weather, geolocation, and delivery data. We also implemented advanced demand forecasting models to optimize sales and inventory."),
                            cls="card"
                        ),
                        Div(
                            H3("London Stock Exchange Group (LSEG)"),
                            P(Strong("Project Focus: "), "Market Risk & VaR Modeling"),
                            P("Defined and developed a delta-gamma approximation VaR model post-acquisition of LCH.Clearnet. Optimized processing architecture using Spark and Hadoop technologies."),
                            cls="card"
                        ),
                        cls="grid grid-2"
                    ),
                    cls="container"
                ),
                cls="section"
            ),
            
            # Dark divider
            Div(cls="section-dark"),
            
            # Technology Stack Section
            Div(
                Div(
                    H2("Our Technology Stack", cls="section-title"),
                    Div(
                        Div(
                            Span("1", cls="number"),
                            Div(
                                H3("Gen AI and Agentic AI"),
                                P("LangGraph/Langchain, CrewAI, PydanticAI, AutoGen, HuggingFace, Smol Agents, Promptflow")
                            )
                        , cls="numbered-item"),
                        Div(
                            Span("2", cls="number"),
                            Div(
                                H3("ML / AI Libraries"),
                                P("PyTorch, JAX, PyCaret, SciKit-Learn, spaCy / NLP, FB Prophet, Transformers; Foundational LLMs: OpenAI, Anthropic, LLama, Mistral, DeepSeek, GraphRAG")
                            )
                        , cls="numbered-item"),
                        Div(
                            Span("3", cls="number"),
                            Div(
                                H3("Databases/Big Data"),
                                P("PostgreSQL, Presto, Athena, Redshift, BigQuery, MongoDB, Databricks, Snowflake")
                            )
                        , cls="numbered-item"),
                        Div(
                            Span("4", cls="number"),
                            Div(
                                H3("Cloud"),
                                P("AWS, Azure, Google Cloud Platform (GCP), Fly, Railway, Render")
                            )
                        , cls="numbered-item"),
                    ),
                    cls="container"
                ),
                cls="section"
            ),
            
            # Dark divider
            Div(cls="section-dark"),
            
            # Why Choose Section
            Div(
                Div(
                    H2("Why Choose Predictive Labs?", cls="section-title"),
                    Div(
                        Div(
                            Div("✓", cls="feature-icon"),
                            H4("Proven Expertise"),
                            P("A track record of successful projects with global enterprises across multiple industries."),
                            cls="feature"
                        ),
                        Div(
                            Div("⚙", cls="feature-icon"),
                            H4("Tailored Solutions"),
                            P("Customized AI models and strategies aligned with business objectives."),
                            cls="feature"
                        ),
                        Div(
                            Div("🚀", cls="feature-icon"),
                            H4("Innovation-Focused"),
                            P("Constantly pushing the boundaries of what AI can achieve."),
                            cls="feature"
                        ),
                        Div(
                            Div("⚡", cls="feature-icon"),
                            H4("Rapid AI Development"),
                            P("We deliver via RAD - Rapid Application Development."),
                            cls="feature"
                        ),
                        cls="feature-grid"
                    ),
                    cls="container"
                ),
                cls="section"
            ),
            
            # Dark divider
            Div(cls="section-dark"),
            
            # CTA Section
            Div(
                Div(
                    H2("Let's Build Together"),
                    P(
                        "Ready to leverage the power of Generative AI and AI / ML in general for your business? Connect with us at ",
                        A("info@predictivelabs.ai", href="mailto:info@predictivelabs.ai", cls="email-link"),
                        " to explore how we can transform your challenges into opportunities."
                    ),
                    cls="container"
                ),
                cls="cta"
            )
        )
    )

serve()
