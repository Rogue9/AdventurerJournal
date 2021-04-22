from flask import Flask, render_template, request
from datetime import datetime
import requests
import smtplib

EMAIL = "Gray24.Bulby37@gmail.com"
PASSWORD = "S3V4fZ(Tfo"
year= datetime.year
app = Flask(__name__)
response = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()
all_posts = []


@app.route('/')
def home():
    return render_template('index.html', data=response)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET','POST'])

def receive_data():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone_number']
        message = request.form['message']
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=f'{email}',
                                to_addrs='JRLEWIS84@GMAIL.COM',
                                msg=f"Message from Blog.Com User:\n\n{name}\n{email}\n{phone}\n{message}")
        return render_template('contact.html')
    elif request.method == "GET":
        return render_template('contact.html')


@app.route('/post/<int:index>')
def get_post(index):
    print(index)

    requested_post = None
    for blog_post in response:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)





if __name__ == "__main__":
    app.run(debug=True)