from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from sassutils.wsgi import SassMiddleware
from decimal import *
import os, json, numpy, pymysql
from db import db
from models.category import Category
from models.product import Product

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_IMAGES = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
app.config['SECRET_KEY'] = 'jollibeeFoodMenu'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/foodmenu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pltliont_eyetracking_foodMenu:pltliont_eyetracking_foodMenu@localhost:3306/pltliont_eyetracking_foodMenu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)
app.config.from_object(__name__)
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'main': ('static/sass', 'static/css', '/static/css')
})

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()
    category = Category.query.filter_by(categoryId='chicken-joy').first()
    if category is None:
        category1 = Category(categoryId='chicken-joy', name='Chicken Joy',
                             description='Crispy and flavorful fried chicken dish.',
                            image='jb-chicken-joy.png')
        category2 = Category(categoryId='burger-steak', name='Burger Steak',
                             description='A classic comfort food with juicy beef patty and mushroom gravy.',
                            image='jb-burger-steak.png')
        category3 = Category(categoryId='palabok', name='Palabok',
                            description='A Filipino noodle dish with shrimp sauce, boiled eggs, and meat toppings.',
                            image='jb-palabok.png')
        category4 = Category(categoryId='beverages', name='Beverages',
                            description='Refreshing drinks to complement your favorite fast-food meals.',
                            image='jb-beverages.png')
        category5 = Category(categoryId='burgers', name='Burgers',
                            description='Juicy and flavorful beef patties topped with signature sauces and toppings.',
                            image='jb-burgers.png')
        category6 = Category(categoryId='chicken-sandwich', name='Chicken Sandwich',
                            description='A crispy and succulent chicken fillet in a warm bun.',
                            image='jb-chicken-sandwich.png')
        db.session.add_all([category1, category2, category3, category4, category5, category6])
        db.session.commit()
        product1 = Product('chicken-joy-solo1', '1pc Chickenjoy Solo',
                           'Philippines’ best-tasting crispylicious, juicylicious Chickenjoy that is crispy on the outside, tender and juicy on the inside.',
                           40, 'jb-chicken-joy.png', 'chicken-joy')
        product2 = Product('chicken-joy-solo2', '2pc Chickenjoy Solo',
                           'Philippines’ best-tasting crispylicious, juicylicious Chickenjoy that is crispy on the outside, tender and juicy on the inside.',
                           80, 'jb-chicken-joy2.png', 'chicken-joy')
        product3 = Product('chicken-joy-spag', '1pc Chickenjoy Solo w/ Jolly Spaghetti w/ Drink',
                           'Philippines’ best-tasting crispylicious, juicylicious Chickenjoy paired with the meatiest, cheesiest, sweet-sarap Jolly Spaghetti.',
                           60, 'jb-chicken-joy-spag.png', 'chicken-joy')
        product4 = Product('chicken-joy-bs', '1pc Chickenjoy Solo w/ Burger Steak',
                           'Philippines’ best-tasting crispylicious, juicylicious Chickenjoy that is crispy on the outside, tender and juicy on the inside.',
                           50, 'jb-chicken-joy.png', 'chicken-joy')
        db.session.add_all([product1, product2, product3, product4])
        db.session.commit()
        product11 = Product('burger-steak-solo1', '1pc Burger-Steak Solo',
                           '100% pure beef patty with a hearty serving of flavorful mushroom gravy and steamed rice.',
                           10, 'jb-burger-steak.png', 'burger-steak')
        product12 = Product('burger-steak-solo2', '2pc Burger-Steak Solo',
                            '2 pieces of 100% pure beef patty with a hearty serving of flavorful mushroom gravy and a cup of steamed rice.',
                            20, 'jb-burger-steak2.png', 'burger-steak')
        product13 = Product('burger-steak-shanghai', '1pc Burger-Steak w/ Shanghai',
                            '100% pure beef patty with a hearty serving of flavorful mushroom gravy and steamed rice with 3 pieces of crispy Shanghai rolls',
                            15, 'jb-burger-steak3.png', 'burger-steak')
        db.session.add_all([product11, product12, product13])
        db.session.commit()
        product21 = Product('palabok-solo', 'Palabok Solo',
                            'A classic favorite-premium bihon noodles topped with Jollibee’s signature palabok sauce and delicious meat toppings.',
                            10, 'jb-palabok.png', 'palabok')
        product22 = Product('palabok-chicken-joy', '1pc. Chickenjoy w/ Palabok',
                            'A classic favorite-premium bihon noodles topped with Jollibee’s signature palabok sauce and delicious meat toppings.',
                            10, 'jb-palabok-chicken-joy.png', 'palabok')
        product23 = Product('palabok-family-pan', '1pc. Palabok Family Pan',
                            'Your classic favorite saucy-sarap Palabok with tasty toppings for sharing with the whole family! Good for 4-5 pax.',
                            100, 'jb-palabok-family-pan.png', 'palabok')
        db.session.add_all([product21, product22, product23])
        db.session.commit()
        product31 = Product('coffee', 'Coffee',
                            'Freshly brewed coffee with a balance of strong coffee taste, milk taste and just the right sweetness',
                            10, 'jb-coffee.png', 'beverages')
        product32 = Product('coke', 'Coke',
                            'Refreshing, ice-cold Coke to perfectly match your favorite meal',
                            10, 'jb-beverages.png', 'beverages')
        product33 = Product('coke-float', 'Coke Float',
                            'Coke soda topped with creamy vanilla soft serve and rich, indulgent chocolate syrup',
                            10, 'jb-coke-float.png', 'beverages')
        db.session.add_all([product31, product32, product33])
        db.session.commit()
        product41 = Product('yumburger', 'Yumburger',
                            'Your favorite langhap-sarap Yumburger made with 100% pure beef and special burger dressing, in between soft buns.',
                            10, 'jb-yumburger.png', 'burgers')
        product42 = Product('yumburger-cheesy', 'Cheesy Yumburger',
                            'Your favorite langhap-sarap Yumburger with creamy cheddar cheese.',
                            15, 'jb-yumburger-cheesy.png', 'burgers')
        product43 = Product('champ', 'Champ',
                            'The iconic 1/3-pound Champ patty with tomato, lettuce and cheese in sesame seed buns.',
                            20, 'jb-champ.png', 'burgers')
        db.session.add_all([product41, product42, product43])
        db.session.commit()
        product51 = Product('chicken-sandwich-solo', 'Chicken Sandwich',
                            'Crunchylicious. 100% Real, Large Chicken ',
                            10, 'jb-chicken-sandwich.png', 'chicken-sandwich')
        product52 = Product('chicken-sandwich-fries', 'Chicken Sandwich w/ Fries and Drink',
                            'Crunchylicious. 100% Real, Large Chicken ',
                            10, 'jb-chicken-sandwich2.png', 'chicken-sandwich')
        db.session.add_all([product51, product52])
        db.session.commit()

@app.route('/')
def index():
    page = 1
    per_page = 3
    categories = Category.query.paginate(page=page,per_page=per_page,error_out=False)
    return render_template('index.html', error=None, categories=categories, page=page)

@app.route('/next')
def nextPage():
    page = 2
    per_page = 3
    categories = Category.query.paginate(page=page,per_page=per_page,error_out=False)
    return render_template('index.html', error=None, categories=categories, page=page)


@app.route('/<categoryId>/<page>')
def category(categoryId, page):
    page=int(page)
    category = Category.query.filter_by(categoryId=categoryId).first()
    if category is None:
        return redirect('/')
    products = Product.query.filter_by(categoryId=categoryId).paginate(page=int(page),per_page=3,error_out=False)
    length = products.total
    print(length)
    return render_template('category.html', error=None, category=category, products=products, page=page, categoryId=categoryId)

@app.route('/cart/<page>')
def cart(page):
    products = []
    serializedData = request.args
    data = json.dumps(serializedData)
    dataDict = json.loads(data)
    total = 0
    next=True
    back=True
    page = int(page)
    pageNum = page
    if len(dataDict) == 0:
        return redirect('/')
    dataString = list(dataDict.keys())[0]
    dataArray = dataString.split(",")
    array = numpy.array(dataArray)
    uniqueProducts, counts = numpy.unique(array, return_counts=True)
    for id, count in zip(uniqueProducts, counts):
        productDict = {}
        product = Product.query.filter_by(productId=id).first()
        subTotal = product.price*count
        productDict['product'] = product
        print(product.name)
        productDict['quantity'] = count
        productDict['subTotal'] = subTotal
        total = total + subTotal
        products.append(productDict)
    if page == 1:
        page = 0
        back=False
    else:
        multipler = page - 1
        page = 2 * multipler
    if not products[page:page+2]:
        return redirect(url_for('checkout'))
    if page+3 > len(products):
        next=False
    return render_template('cart.html', error=None, products=products[page:page+2], total=total, next=next, back=back, pageNum=pageNum)

@app.route('/checkout')
def checkout():
    products = []
    serializedData = request.args
    data = json.dumps(serializedData)
    dataDict = json.loads(data)
    print(dataDict)
    print(bool(dict))
    if len(dataDict) == 0:
        return redirect('/')
    dataString = list(dataDict.keys())[0]
    dataArray = dataString.split(",")
    array = numpy.array(dataArray)
    uniqueProducts, counts = numpy.unique(array, return_counts=True)
    for id, count in zip(uniqueProducts, counts):
        productDict = {}
        productDict['product'] = Product.query.filter_by(productId=id).first()
        productDict['quantity'] = count
        products.append(productDict)
    print(products)
    return render_template('checkout.html', error=None, products=products)

@app.route('/order', methods=['POST'])
def order():
    products = []
    total = 0
    names = request.form.getlist('name')
    quantities = request.form.getlist('quantity')
    if names is None:
        return redirect('/')
    if quantities is None:
        return redirect('/')
    for name, quantity in zip(names, quantities):
        productDict = {}
        prod = Product.query.filter_by(name=name).first()
        productDict['product'] = prod
        productDict['quantity'] = Decimal(quantity)
        total = total + (prod.price * Decimal(quantity))
        products.append(productDict)
    print(products)
    return render_template('order.html', products=products, total=total)

if __name__=='__main__':
    app.run(host='localhost', port=8000, debug=True)