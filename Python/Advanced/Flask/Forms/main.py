from flask import Flask, render_template, request
import smtplib
import requests

EMAIL = ''
PASSWORD = ''


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        email_sender(email, name, message)
        return f"<h1>Success</h1>"
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def email_sender(email, name, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= EMAIL, password= PASSWORD)
        connection.sendmail(from_addr= email,
                            to_addrs= '',
                            msg= f"Subject: Your Contact\n\n{message} from {email}, {name}")



if __name__ == "__main__":
    app.run(debug=True, port=5001)
