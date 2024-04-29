from flask import Flask, render_template_string, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import datetime
from homeharvest import scrape_property
import pandas as pd
import os
from flask import Flask, render_template_string, request, send_file, current_app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'klk'

class PropertyForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    municipality = StringField('Municipality', validators=[DataRequired(), Length(min=2, max=50)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=50)])
    listing_type = SelectField('Listing Type', choices=[('for_sale', 'For Sale'), ('for_rent', 'For Rent'), ('pending', 'Pending')])
    past_days = IntegerField('Past Days', validators=[DataRequired()])
    submit = SubmitField('Scrape Properties')


# def scrape_and_save(municipality, state, listing_type, past_days, user_name):
#     directory = os.path.join(current_app.root_path, 'scraped_data')
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     filename = f"{user_name}_{current_timestamp}.csv"
#     file_path = os.path.join(directory, filename)  # Full path where the file will be saved
#     properties = scrape_property(location=f"{municipality}, {state}", listing_type=listing_type, past_days=past_days)
#     properties.to_csv(file_path, index=False)  # Save file to full path
#     return file_path  # Return the full path for use in send_file


def scrape_and_save(location, listing_type, past_days, user_name):
    current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{user_name}_{current_timestamp}.csv"
    properties = scrape_property(location, listing_type, past_days)
    properties.to_csv(filename, index=False)
    return filename

@app.route('/', methods=['GET', 'POST'])
def home():
    form = PropertyForm(request.form)
    if request.method == 'POST' and form.validate():
        filename = scrape_and_save(
            f"{form.municipality.data}, {form.state.data}",
            form.listing_type.data,
            form.past_days.data,
            form.name.data.replace(" ", "_")
        )
        return send_file(filename, as_attachment=True)
    
    # HTML content defined directly in the return statement
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Scrape Properties</title>
   <style>
       body {
           font-family: Arial, sans-serif;
           background-color: #f2f2f2;
           margin: 0;
           padding: 0;
       }

       .container {
           max-width: 600px;
           margin: 50px auto;
           background-color: #fff;
           padding: 20px;
           border-radius: 8px;
           box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
       }

       h1 {
           text-align: center;
           color: #333;
       }

       form {
           margin-top: 20px;
       }

       p {
           margin-bottom: 15px;
       }

       label {
           font-weight: bold;
       }

       input[type="text"] {
           width: 100%;
           padding: 8px;
           border-radius: 5px;
           border: 1px solid #ccc;
       }

       select {
           width: 100%;
           padding: 8px;
           border-radius: 5px;
           border: 1px solid #ccc;
       }

       input[type="submit"] {
           width: 100%;
           padding: 10px;
           background-color: #4CAF50;
           color: white;
           border: none;
           border-radius: 5px;
           cursor: pointer;
           font-size: 16px;
       }

       input[type="submit"]:hover {
           background-color: #45a049;
       }
   </style>
</head>
<body>
<div class="container">
   <h1>Enter Details to Scrape Properties</h1>
   <form method="post">
       {{ form.hidden_tag() }}
       <p>
           <label for="name"> Your Name:</label><br>
           {{ form.name(size=20) }}
       </p>
       <p>
           <label for="municipality">Municipality:</label><br>
           {{ form.municipality(size=20) }}
       </p>
       <p>
           <label for="state">State:</label><br>
           {{ form.state(size=20) }}
       </p>
       <p>
           <label for="listing_type">Listing Type:</label><br>
           {{ form.listing_type() }}
       </p>
       <p>
           <label for="past_days">Past Days:</label><br>
           {{ form.past_days(size=20) }}
       </p>
       <p>
           {{ form.submit() }}
       </p>
   </form>
</div>
</body>
</html>
    ''', form=form)

if __name__ == "__main__":
    app.run(debug=True)
    
    