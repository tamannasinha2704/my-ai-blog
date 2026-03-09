import os
import random
import datetime
from google import genai
from google.genai import types

# 1. Setup New GenAI Client
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version='v1')
)
TOPICS = [
    "Data cleaning and processing techniques with Python code",
    "Data analytics and ML concepts (like Vision Transformers or Explainable AI)",
    "Product breakdown of a software (UI/UX and functionality)",
    "Latest AI trends (Agentic AI, Collaborative AI, or new automation tools)"
]

def generate_post():
    topic = random.choice(TOPICS)
    prompt = f"""
    Write a professional technical blog post about {topic}.
    Include:
    1. A catchy title.
    2. A 'Concept' section with explanation.
    3. A 'Code or Practical Example' section.
    4. A 'Why it matters' section.
    Format it as Jekyll Markdown with front matter:
    ---
    layout: post
    title: "Title Here"
    date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S +0530')}
    categories: blog
    ---
    Keep it concise but insightful.
    """
    
    try:
        # 2. Use the standard model ID
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt
        )
        content = response.text
        
        # Create filename: YYYY-MM-DD-title.md
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        unique_id = random.randint(1000, 9999)
        filename = f"_posts/{date_str}-post-{unique_id}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated: {filename}")
        
    except Exception as e:
        print(f"Error generating post: {e}")

if __name__ == "__main__":
    # Logic for 1-5 commits per day
    num_commits = random.randint(1, 5)
    print(f"Starting generation of {num_commits} posts...")
    for _ in range(num_commits):
        generate_post()