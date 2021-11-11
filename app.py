from flask import Flask, request, render_template, redirect, jsonify, session
from forex_python.converter import CurrencyCodes, CurrencyRates
from decimal import Decimal
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


@app.route("/")
def show_homepage():
    """show the converter form"""
    return render_template("/converter.html")

@app.route("/converter.html")
def redirect_result():
    """redirect to result page"""
    return redirect("/result.html")

@app.route("/result", methods = ['POST'])
def convert_currency():
    """redirect to result page"""
    c = CurrencyRates(force_decimal=True)
    c_code = CurrencyCodes()
    currency = request.form["currency"]
    newCurrency = request.form["newCurrency"]
    amount = request.form["amount"]
    msg = []
    err = True
    if not c_code.get_currency_name(currency):
        msg.append(f"{currency} is not a valid currency.")
        err = False
    if not c_code.get_currency_name(newCurrency):
        msg.append(f"{newCurrency} is not a valid currency.")
        err = False
    if not amount.isnumeric():
        msg.append(f"{amount} is not a valid number.")
        err = False
    if not err: 
        return render_template("/converter.html", msg = msg)
    code = c_code.get_symbol(newCurrency)
    result = round(c.convert(currency, newCurrency, Decimal(amount)), 2)
    return render_template("/result.html", code = code, result = result)

