from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts= all_posts)

@app.route('/post/<iden>')
def get_post(iden):
    response = requests.get(blog_url)
    all_posts = response.json()
    item_with_id = next((item for item in all_posts if item['id'] == int(iden)), None)
    return render_template("post.html", title= item_with_id['title'], subtitle= item_with_id['subtitle'], text= item_with_id['body'])

if __name__ == "__main__":
    app.run(debug=True)
