from flask import Flask, render_template

app = Flask(__name__)

# ----------- MAIN PAGES -----------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# ----------- PRODUCT PAGES -----------

@app.route('/hair-accessories')
def hair():
    return render_template('hair.html')

@app.route('/flowers')
def flowers():
    return render_template('flowers.html')

@app.route('/keychains')
def keychains():
    return render_template('keychains.html')

@app.route('/pot')
def pot():
    return render_template('pot.html')

@app.route('/miscellaneous')
def miscellaneous():
    return render_template('miscellaneous.html')

@app.route('/laddu-gopal-poshak')
def laddu():
    return render_template('laddu-gopal-poshak.html')


# ----------- RUN SERVER -----------

if __name__ == '__main__':
    app.run(debug=True)