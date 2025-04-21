import os
from datetime import datetime

# Directory where the blog posts are stored
blog_directory = "blog"

# Get a list of blog posts, sorted by creation date
blog_posts = sorted(os.listdir(blog_directory), key=lambda x: os.path.getmtime(os.path.join(blog_directory, x)), reverse=True)

# Limit to latest 5 posts
latest_posts = blog_posts[:5]

# Generate the HTML for the homepage
homepage_content = """
<html>
<head>
    <title>Everyday AI Pro - Latest Posts</title>
</head>
<body>
    <h1>Latest Blog Posts</h1>
    <ul>
"""

# Create the list of latest posts
for post in latest_posts:
    post_title = post.replace(".html", "").replace("_", " ").title()
    post_date = datetime.fromtimestamp(os.path.getmtime(os.path.join(blog_directory, post))).strftime("%B %d, %Y")
    post_url = f"blog/{post}"
    
    # Read the first 150 words of the post for a snippet
    with open(os.path.join(blog_directory, post), "r") as file:
        content = file.read()
        snippet = content[:150] + "..."
    
    # Add each post to the homepage content
    homepage_content += f"""
    <li>
        <h2><a href="{post_url}">{post_title}</a></h2>
        <p>{snippet}</p>
        <p><small>Posted on {post_date}</small></p>
        <a href="{post_url}">Read More</a>
    </li>
    """

# Close the homepage content
homepage_content += """
    </ul>
</body>
</html>
"""

# Path to the index.html file
index_file_path = "index.html"

# Write the new homepage content to the index.html file
with open(index_file_path, "w") as index_file:
    index_file.write(homepage_content)

print("Homepage updated successfully")
