from flask import Flask

app = Flask("Task Manager")

@app.route("/")
def home():
	return f"Hello from home page"

