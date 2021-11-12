### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
   JS client side. Python server side
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

    dic.get('c', 0)
    dic['c'] = None



- What is a unit test?
    Unit test is used to test one function.
- What is an integration test?
    Integration test is used to test integration of functions.
- What is the role of web application framework, like Flask?
    It helps to define the response and request methods.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

URL Parameter feels more like subject of page
Query Parameter feels more like “extra info about page”


- How do you collect data from a URL placeholder parameter using Flask?
@app.route("/")
def hello():
    return request.args.get("attribute")

- How do you collect data from the query string using Flask?
if url is /search?query=str
@app.route("/search")
def search():
    string = request.args["query"]
    return f"{string}"


- How do you collect data from the body of the request using Flask?
@app.route("/my/route", methods=["POST"])
    ... = request.form['...']

- What is a cookie and what kinds of things are they commonly used for?

Cookies are name/string-value pair stored by the client (browser).

- What is the session object in Flask?
A dictionary that contains session key and value.

- What does Flask's `jsonify()` do?
 jsonify serializes data to JSON format,