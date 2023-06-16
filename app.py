from flask import Flask, render_template, redirect
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Render the loading screen template
    return render_template('loading.html')

@app.route('/home')
def home():
    products = [
        {"title": "Product 1", "description": "Description 1", "price": "9.99"},
        {"title": "Product 2", "description": "Description 2", "price": "19.99"},
        {"title": "Product 3", "description": "Description 3", "price": "29.99"},
    ]
    # Simulate a delay or time-consuming task
   
    # Render the home template with the products data
    return render_template('home.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
