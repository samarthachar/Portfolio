import requests
from flask import Flask, render_template, flash, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField

app  = Flask(__name__)
app.secret_key = 'secret_key'

class PostcodeForm(FlaskForm):
    start = StringField('', render_kw={"placeholder": "Enter start postcode"})
    end = StringField('', render_kw={"placeholder": "Enter destination postcode"})
    submit = SubmitField('Get route!')

def format_postcode(postcode):
    if " " in postcode:
        postcode = postcode.replace(" ","")
    postcode =  postcode.upper().strip()
    return  f"{postcode[:-3]} {postcode[-3:]}"

def latandlong(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode.replace(" ","")}"
    data = requests.get(url=url).json()
    try:
        if data['error']:
            return False
    except:
        pass
    lat = data["result"]["latitude"]
    long = data["result"]["longitude"]
    return lat,long



@app.route("/", methods=["GET", "POST"])
def api():
    form = PostcodeForm()
    if form.validate_on_submit():

        start = form.start.data
        end = form.end.data

        start = latandlong(start)
        end = latandlong(end)

        if not start:
            flash("Please enter a valid start postcode", "warning")
            return redirect(url_for('api'))
        elif not end:
            flash("Please enter a valid end postcode", "warning")
            return redirect(url_for('api'))
        else:

            url=f"https://api.tfl.gov.uk/Journey/JourneyResults/{start[0]},{start[1]}/to/{end[0]},{end[1]}"
            data = requests.get(url=url).json()

            if "journeys" not in data:
                flash("No journey found for your inputs", "warning")
                return redirect(url_for('api'))

            legs = data["journeys"][0]["legs"]
            summaries = [leg["instruction"]["summary"] for leg in legs ]
            return render_template('index.html', form=form, route=summaries)
    return render_template("index.html", form = form, route=False)

if __name__ == "__main__":
    app.run(debug=True)