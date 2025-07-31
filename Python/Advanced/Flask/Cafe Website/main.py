from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[URL()])
    opens = StringField('Opening Time e.g. 8:00am')
    closes = StringField('Closing Time e.g. 5:30pm')
    coffee_rating = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕'])
    wifi_rating = SelectField('Wifi Strength Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪'])
    power_sockets = SelectField('Power Socket Availability', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


cafe_values = ['cafe', 'location', 'opens', 'closes', 'coffee_rating', 'wifi_rating', 'power_sockets']


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        data_row = [form.data[key] for key in cafe_values if key in form.data]
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data_row)
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
