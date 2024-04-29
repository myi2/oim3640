# HomeHarvest: Real Estate Listings Scraper

## Project Overview

**The Big Idea:** HomeHarvest is a Python-based tool designed to automate the collection of real estate listings from various websites. Users can input criteria such as location, price range, and home features (e.g., number of bedrooms, bathrooms, square footage) to receive tailored property recommendations. The minimum viable product (MVP) will provide a list of homes matching these criteria, with stretch goals including a user-friendly web interface and integration with mapping APIs for enhanced searches.

**Team Members:** Adrien Schaal & Moises Yi

## Learning Objectives

- **Primary Objective:** Develop a Python-based web scraper to efficiently navigate and extract data from real estate websites.
- **Secondary Objective:** Master data manipulation to structure scraped data into a user-friendly format.
- **Tertiary Objective:** Explore machine learning algorithms to enhance property recommendations based on user preferences.

## Implementation Strategy

1. **Tool Exploration:** Evaluate Python libraries such as Beautiful Soup, Scrapy, and Selenium for web scraping capabilities.
2. **Data Modeling:** Design a data model to effectively store and manipulate the scraped data.
3. **Website Selection:** Identify real estate websites that allow scraping and provide comprehensive data.
4. **Scraping Logic:** Develop scripts to extract listings based on user-defined criteria.
5. **Data Filtering:** Implement algorithms to sort and present relevant listings.
6. **Stretch Goals:** Build a web interface using Flask or Django for easy user interaction.

## How to Use the Web Application

1. **Open the Application**
   - Start by navigating to the HomeHarvest application in your web browser.

2. **Enter Your Details**
   - Fill in each field with the appropriate information:
     - **Your Name:** Type your name here.
     - **Municipality:** Enter the municipality where you're looking for properties.
     - **State:** Input the state for your property search.
     - **Listing Type:** Select the type of listing you are interested in from the dropdown menu (e.g., For Sale, For Rent).
     - **Past Days:** Specify the number of past days you want to search for listings. This filters the properties to only show recent listings.

3. **Submit Your Search**
   - Once all fields are filled out, click the `Scrape Properties` button. This green button is located at the bottom of the form.

4. **View Your Results**
   - After clicking the `Scrape Properties` button, the application will process your request and provide you with a downloadable file containing all the real estate listings that meet your specified criteria.

Make sure to input accurate information to get the best results tailored for you. Happy house hunting!
## Technical Setup

### Installation

Clone the repository:

```bash
[git clone https://github.com/yourusername/homeharvest.git](https://github.com/myi2/oim3640/blob/main/helloflask/Final_Project_Website/App_3.py)
cd homeharvest
