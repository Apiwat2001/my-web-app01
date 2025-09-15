# app.py
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        print(f"Name: {name}, Email: {email}")  # ทดสอบการรับข้อมูล
        return redirect("/")
    return render_template("form.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # อ่านพอร์ตจาก environment
    app.run(host='0.0.0.0', port=port)
