import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
response = requests.get("https://www.nba.com/stats")

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the sections with class "LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ"
sections = soup.find_all("div", class_="LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ")

# Define the file path
file_path = r"C:\Users\myi2\Documents\GitHub\oim3640\Sessions 22\data\nba_stats.csv"

# Open the CSV file for writing
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Section', 'Rank', 'Player', 'Team', 'Value'])  # Write the header row

    # Iterate over each section
    for section in sections:
        # Extract the section title
        section_title = section.find("h2", class_="LeaderBoardCard_lbcTitle___WI9J").text.strip()

        # Find the table within the section
        table = section.find("table", class_="LeaderBoardPlayerCard_lbpcTable__q3iZD")

        # Iterate over each row in the table
        for row in table.tbody.find_all("tr"):
            # Extract the data from each cell in the row
            rank = row.find("td", class_="LeaderBoardPlayerCard_lbpcTableCell__SnM1o").text.strip()
            player = row.find("a", class_="LeaderBoardPlayerCard_lbpcTableLink__MDNgL").text.strip()
            team = row.find("span", class_="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3").text.strip()
            value = row.find_all("a", class_="LeaderBoardPlayerCard_lbpcTableLink__MDNgL")[-1].text.strip()

            # Write the data to the CSV file
            writer.writerow([section_title, rank, player, team, value])
