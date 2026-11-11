import pandas as pd
#load the csv
cfb_data = pd.read_csv("cfb.csv")
#get user input for season
season = int(input("Enter a season to analyze: "))
season_data = cfb_data[cfb_data["Season"] == season]
#check if season exists
if season_data.empty:
    print(f"Sorry, {season} was not found.")
    exit()
#make categories for wins
categories = {
    "10 or more wins": [],
    "8 to 9 wins": [],
    "6 to 7 wins": [],
    "Fewer than 6 wins": []
}
#search the rows for team name and wins
for row, col in season_data.iterrows():
    team_name = col["Team"]
    wins = col["Win"]

    if wins >= 10:
        categories["10 or more wins"].append(team_name)
    elif wins >= 8:
        categories["8 to 9 wins"].append(team_name)
    elif wins >= 6:
        categories["6 to 7 wins"].append(team_name)
    else:
        categories["Fewer than 6 wins"].append(team_name)

print(f"\nCollege Football Results for {season}")

for category, teams in categories.items():
    print(f"\n{category}:")
    for team in teams:
        print(f"- {team}")