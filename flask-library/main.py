from turtle import title
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book title:{self.title}, Author: {self.author}>'
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

all_books = []
def create_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    db.commit()

def add_to_database():
    cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', 9.3)")
    db.commit()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form = request.form
        # all_books.append({"title": form.get("title"), "author": form.get("author"), "rating": form.get("rating")})
        new_book = Book(title=form.get('title'), author=form.get("author"), rating=form.get("rating"))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html')

@app.route("/edit=<int:book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    form = request.form
    book = Book.query.get(book_id)
    if request.method == "POST":
        book.rating = form.get('rating')
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", book=book)

@app.route("/delete")
def delete_book():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    # db.create_all()
    # book_1 = Book(title='Harry Potter', author='J. K. Rowling', rating=9.3)
    # book_1 = Book(title='Creativo', author='Roberto Mtz', rating=7.0)
    # db.session.add(book_1)
    # db.session.commit()
    all_books = db.session.query(Book).all()
    # app.run(debug=True, use_reloader=False)
    app.run(debug=True)

