import openai
import os

# Get the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_blog_post():
    # Using the new API method (v1.0.0+)
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
        prompt="Write a detailed blog post about making money online using AI tools, including affiliate links for Jasper AI, Copy.ai, and Writesonic.",
        max_tokens=1500
    )
    return response['choices'][0]['text'].strip()

blog_post = generate_blog_post()

# Save the generated blog post to an HTML file
with open("blog/generated_post.html", "w") as file:
    file.write(f"<html><body><h1>AI Tools for Earning Money</h1><p>{blog_post}</p></body></html>")
