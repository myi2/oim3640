from flask import Flask, render_template, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import datetime
import pandas as pd
import os
import homeharvest  # Assuming it's a module in your project

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace_with_a_secret_key'

# Define the form with relevant fields and validators
class PropertyForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    municipality = StringField('Municipality', validators=[DataRequired(), Length(min=2, max=50)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=50)])
    listing_type = SelectField('Listing Type', choices=[('for_sale', 'For Sale'), ('for_rent', 'For Rent'), ('pending', 'Pending')])
    past_days = IntegerField('Past Days', validators=[DataRequired()])
    submit = SubmitField('Scrape Properties')

# Define the scrape function and saving mechanism
def scrape_and_save(municipality, state, listing_type, past_days, user_name):
    directory = os.path.join(app.root_path, 'scraped_data')  # app instead of current_app
    if not os.path.exists(directory):
        os.makedirs(directory)
    current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{user_name}_{current_timestamp}.csv"
    file_path = os.path.join(directory, filename)  # Full path where the file will be saved
    properties = homeharvest.scrape_property(location=f"{municipality}, {state}", listing_type=listing_type, past_days=past_days)
    properties.to_csv(file_path, index=False)  # Save file to full path
    return file_path  # Return the full path for use in send_file

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = PropertyForm(request.form)
    if request.method == 'POST' and form.validate():
        filename = scrape_and_save(
            form.municipality.data,
            form.state.data,
            form.listing_type.data,
            form.past_days.data,
            form.name.data.replace(" ", "_")
        )
        return send_file(filename, as_attachment=True)

    # Render the template from the "templates" folder
    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
