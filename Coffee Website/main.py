from flask import Flask, render_template,redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

def str_to_bool(value):
    return True if value == "True" else False if value == "False" else None

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=True)
    location: Mapped[str] = mapped_column(String(250), nullable=True)
    seats: Mapped[str] = mapped_column(String(250), nullable=True)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=True)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=False)


    def get_important(self):
        return [self.name, self.map_url,self.coffee_price, self.has_wifi, self.has_sockets]


with app.app_context():
    db.create_all()


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    map_url = StringField("Google Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    seats = StringField("Number of Seats", validators=[DataRequired()])

    has_toilet = SelectField("Toilet Available?", choices=[
        ("True", "Yes"),
        ("False", "No"),
        ("None", "Unknown")
    ])

    has_wifi = SelectField("WiFi Available?", choices=[
        ("True", "Yes"),
        ("False", "No"),
        ("None", "Unknown")
    ])

    has_sockets = SelectField("Power Sockets Available?", choices=[
        ("True", "Yes"),
        ("False", "No"),
        ("None", "Unknown")
    ])

    can_take_calls = SelectField("Can Take Calls?", choices=[
        ("True", "Yes"),
        ("False", "No"),
        ("None", "Unknown")
    ])

    coffee_price = FloatField("Coffee Price (£)", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteForm(FlaskForm):
    delete_cafe = SelectField("Name of Cafe", choices=[])
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.cafe.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            seats=form.seats.data,
            has_toilet=str_to_bool(form.has_toilet.data),
            has_wifi=str_to_bool(form.has_wifi.data),
            has_sockets=str_to_bool(form.has_sockets.data),
            can_take_calls=str_to_bool(form.can_take_calls.data),
            coffee_price=str(form.coffee_price.data)
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html', form=form)



@app.route('/cafes')
def cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    list_of_rows = []
    for cafe in all_cafes:
        list_of_rows.append(cafe.get_important())
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/delete', methods = ["GET", "POST"])
def delete():
    form = DeleteForm()
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    form.delete_cafe.choices = [(cafe.name, cafe.name) for cafe in all_cafes]
    if form.validate_on_submit():
        deleted_cafe = db.session.execute(db.select(Cafe).where(Cafe.name == form.delete_cafe.data)).scalar_one_or_none()
        if deleted_cafe:
            db.session.delete(deleted_cafe)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run()
