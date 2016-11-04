from flask import Flask, render_template, request, redirect, session, flash

from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "secret_key"

mysql = MySQLConnector(app, "books")

@app.route("/")
def index():
	query = "SELECT title, first_name, last_name FROM books LEFT JOIN authors ON books.author_id=authors.id;"
	books = mysql.query_db(query)

	query = "SELECT id, first_name, last_name FROM authors;"
	authors = mysql.query_db(query)

	return render_template("index.html", books=books, authors=authors)

@app.route("/create_author", methods=["POST"])
def create_author():
	query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (:first_name, :last_name, NOW(), NOW());"
	data = {
		"first_name": request.form["first_name"],
		"last_name": request.form["last_name"],
	}

	mysql.query_db(query, data)
	
	return redirect("/")

@app.route("/create_book", methods=["POST"])
def create_book():
	query = "INSERT INTO books (title, author_id, created_at, updated_at) VALUES (:title, :author_id, NOW(), NOW());"

	data = {
		"title": request.form["title"],
		"author_id": request.form["author_id"],
	}

	print(query)
	print(data)
	mysql.query_db(query, data)

	return redirect("/")

app.run(debug=True)