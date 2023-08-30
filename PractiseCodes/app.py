from flask import Flask, render_template

app = Flask(__name__)

products = {
    1: {'name': 'product1', 'price': 10.99, 'description': 'This is product 1', 'image': 'https://picsum.photos/200/200'},
    2: {'name': 'product2', 'price': 20.99, 'description': 'This is product 2', 'image': 'https://picsum.photos/200/200'},
    3: {'name': 'product3', 'price': 30.99, 'description': 'This is product 3', 'image': 'https://picsum.photos/200/200'},
}

@app.route('/')
def welcome():
    return 'Welcome to the E-Commerce Application'

@app.route('/products')
def display_products():
    return render_template('products.html', products = products)



if __name__ == '__main__':
    app.run()