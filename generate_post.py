import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_blog_post():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Write a detailed blog post about making money online using AI tools, including affiliate links for Jasper AI, Copy.ai, and Writesonic.",
        max_tokens=1500
    )
    return response.choices[0].text.strip()

blog_post = generate_blog_post()

# Save the post to an HTML file
with open("blog/generated_post.html", "w") as file:
    file.write(f"<html><body><h1>AI Tools for Earning Money</h1><p>{blog_post}</p></body></html>")
