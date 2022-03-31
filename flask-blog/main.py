from tempfile import tempdir
from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

all_posts = []

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    for post in posts:
        all_posts.append(Post(post['id'], post['title'], post['subtitle'], post['body']))
    print(all_posts)
    return render_template("index.html", posts=posts)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    print(f"blog_id: {blog_id}")
    post_with_id = next(post for post in all_posts if post.id == blog_id)
    return render_template("post.html", post=post_with_id)

if __name__ == "__main__":
    app.run(debug=True)
