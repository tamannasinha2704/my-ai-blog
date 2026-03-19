import os
import random
import datetime
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version='v1')
)

# Expanded topics to ensure diversity and reduce overlap
TOPICS = [
    # --- 20% AI & New Trends ---
    "Agentic workflows in healthcare diagnostic automation",
    "The rise of Collaborative AI agents in financial risk modeling",
    "Multi-modal AI: Integrating vision and voice in hospital management systems",
    "Sovereign AI: Why nations are building private LLMs for citizen data",
    "Small Language Models (SLMs) for edge computing in medical devices",
    "The impact of Retrieval-Augmented Generation (RAG) on financial research",
    "Liquid Neural Networks and their potential in real-time patient monitoring",
    "AI Safety and alignment in autonomous robotic surgery",
    "Prompt Engineering vs Fine-tuning for specialized legal-tech AI",
    "The energy efficiency of Green AI in sustainable finance",

    # --- 20% UX Thinking & Product Breakdowns (AI PM Perspective) ---
    "Product Breakdown: How Robinhood uses AI for behavioral nudging",
    "UX Thinking: The 'Invisible' UI in AI-driven health tracking apps",
    "Product Breakdown: Duolingo's AI-tutor and the psychology of retention",
    "Mental Models: Designing for trust in AI-powered wealth management",
    "Product Breakdown: Notion AI and the evolution of collaborative workspaces",
    "The role of an AI PM in balancing model accuracy vs. user friction",
    "UX Breakdown: How ChatGPT changed the expectations for conversational UI",
    "Product Strategy: Why Canva integrated AI to democratize design UX",
    "Reducing 'Hallucination Anxiety' in professional AI dashboard design",
    "Product Breakdown: Stripe’s use of ML for seamless fraud prevention UX",

    # --- 20% ML & New Trends in ML ---
    "Vision Transformers (ViT) for early-stage cancer detection",
    "Federated Learning: Training ML models on private financial data",
    "Self-Supervised Learning in genomic sequence analysis",
    "Neural Architecture Search (NAS) for optimizing trading bots",
    "Graph Neural Networks (GNNs) for drug discovery and molecular interaction",
    "Reinforcement Learning from Human Feedback (RLHF) in fintech chatbots",
    "Diffusion Models beyond art: Synthesizing medical imaging data",
    "Quantization techniques for deploying ML models on mobile health apps",
    "Zero-shot learning for identifying emerging financial market anomalies",
    "The transition from CNNs to Foundation Models in medical computer vision",

    # --- 10% Data Science ---
    "Feature engineering for predictive maintenance in pharmaceutical labs",
    "Synthetic data generation for testing HIPAA-compliant health systems",
    "Dimensionality reduction in high-frequency trading datasets",
    "The ethics of data bias in AI-driven credit scoring models",
    "Bayesian statistics for clinical trial outcome prediction",

    # --- 10% Data Analytics ---
    "Real-time ETL pipelines for tracking global disease outbreaks",
    "Advanced cohort analysis for digital health subscription models",
    "Using SQL and Python to audit algorithmic transparency in fintech",
    "Predictive analytics for hospital bed capacity management",
    "Causal inference in analyzing the impact of interest rates on tech stocks",

    # --- 10% Bioinformatics Trends ---
    "Single-cell RNA sequencing and the future of personalized medicine",
    "AlphaFold 3: The next frontier in protein folding and drug design",
    "CRISPR and AI: Optimizing gene editing for hereditary diseases",
    "Metagenomics: Analyzing the human microbiome for preventative health",
    "Digital Twins: Modeling human organs for virtual drug testing",

    # --- 10% Financial Markets & AI/World News ---
    "How Sentiment Analysis of global news drives AI-led market volatility",
    "The impact of GPU supply chain news on the NASDAQ 100",
    "AI-driven reactions to central bank interest rate announcements",
    "The correlation between AI breakthrough announcements and retail trading",
    "Algorithmic market reactions to geopolitical shifts and news cycles"
]

def generate_post():
    topic = random.choice(TOPICS)
    
    # Updated prompt to enforce the "No Semicolon" rule and unique content
    prompt = f"""
    Write a unique technical blog post about {topic}.
    
    STRICT RULES:
    1. TITLE: Create a single, punchy narrative title (e.g., 'The NLP Revolution Comes to Image Analysis with Vision Transformers'). 
       DO NOT use semicolons or 'Main Title: Subtitle' format.
    2. CONTENT: Focus on a SPECIFIC, unique angle of this topic to avoid overlapping with previous general posts.
    
    Structure:
    - Concept: Clear explanation of the specific angle.
    - Code/Practical Example: High-quality snippet or breakdown.
    - Impact: Why this specific technique matters.
    
    Format as Jekyll Markdown with this front matter:
    ---
    layout: post
    title: "[Your Punchy Title Here]"
    date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S +0530')}
    categories: blog
    ---
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3-flash', # Using the latest stable flash model
            contents=prompt
        )
        content = response.text
        
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        unique_id = random.randint(1000, 9999)
        filename = f"_posts/{date_str}-post-{unique_id}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated unique post: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Keeping it to 1 post per day to maintain high quality and avoid API limits
    generate_post()