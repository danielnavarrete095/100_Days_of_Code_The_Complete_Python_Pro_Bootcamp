from os import sep
from tempfile import tempdir
from flask import Flask, render_template, request
import requests
from post import Post
from smtp import send_mail
from keys import *

app = Flask(__name__)

all_posts = []

@app.route('/')
def home():
    global all_posts
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    all_posts = []
    for post in posts:
        all_posts.append(Post(post['id'], post['title'], post['subtitle'], post['body']))
    print(all_posts)
    return render_template("index.html", posts=posts)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    global all_posts
    print(f"blog_id: {blog_id}")
    print(all_posts)
    post_with_id = next(post for post in all_posts if post.id == blog_id)
    return render_template("post.html", post=post_with_id)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        req = request.form
        name = req['name']
        email = req['email']
        phone = req['phone']
        message = req['message']
        print(name, email, phone, message, sep="\n")
        mail_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        send_mail((GMAIL_USER, GMAIL_PASSWORD), HOTMAIL_USER, "New message from blog", mail_message)
        return render_template("contact.html", message="Message sent succesfully!")

if __name__ == "__main__":
    app.run(debug=True)
