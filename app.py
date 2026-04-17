from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def factorial():

    if request.method == "POST":

        num = int(request.form["num"])

        fact = 1

        for i in range(1, num+1):
            fact *= i

        return f"Faktorial: {fact}"

    return render_template("index.html")

app.run(debug=True)
