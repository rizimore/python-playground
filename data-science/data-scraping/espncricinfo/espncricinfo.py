"""
Players Scraper

@author Mubashir Rasool Razvi
@version 1.0.0

Get all the players info like batting and fielding averages, bowling averages, name, country, team, age, role, batting
and bowling styles, etc. from espncricinfo.com
"""

import requests
from bs4 import BeautifulSoup

players_data = []

players_index = requests.get("https://www.espncricinfo.com/ci/content/player/index.html").text
players_index_soup = BeautifulSoup(players_index, "lxml")

for country in players_index_soup.select("#ciHalloffameDropdown > option"):
    country_name = country.text
    country_code = country['value']

    team_index = requests.get("https://www.espncricinfo.com/ci/content/player/index.html?country=" + str(country_code)).text
    team_index_soup = BeautifulSoup(team_index, "lxml")

    for player in team_index_soup.select("td.divider > a"):
        player_id = player['href'].replace("/ci/content/player/", "").replace(".html", "").strip()
        player_name = player.text
        player_url = "https://www.espncricinfo.com/" + player['href']

        player_index = requests.get(player_url).text
        player_index_soup = BeautifulSoup(player_index, "lxml")

        player_full_name = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(1) > span").text.strip()
        player_country = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div.ciPlayernametxt > div > h3 > b").text.strip()
        player_born = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(2) > span").text.strip()
        player_age = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(3) > span").text.strip()
        player_role = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(5) > span").text.strip()
        player_batting_style = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(6) > span").text.strip()
        player_bowling_style = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(7) > span").text.strip()
        player_image = player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(2) > img")['src']

        player_major_teams = []
        for team in player_index_soup.select("#ciHomeContentlhs > div.pnl490M > div:nth-child(2) > div:nth-child(1) > p:nth-child(4) > span"):
            player_major_teams.append(team.text.replace(",",  "").strip())

        players_data.append({
            "ID": player_id,
            "Name": player_name,
            "Full Name": player_full_name,
            "Country": player_country,
            "Born": player_born,
            "Age": player_age,
            "Role": player_role,
            "Batting Style": player_batting_style,
            "Bowling Style": player_batting_style,
            "Image": player_image,
            "Teams": player_major_teams,
            "BF-ODIs-Mat": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2)").text.strip(),
            "BF-ODIs-Inns": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(3)").text.strip(),
            "BF-ODIs-NO": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(4)").text.strip(),
            "BF-ODIs-Runs": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(5)").text.strip(),
            "BF-ODIs-HS": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(6)").text.strip(),
            "BF-ODIs-Ave": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(7)").text.strip(),
            "BF-ODIs-BF": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(8)").text.strip(),
            "BF-ODIs-SR": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(9)").text.strip(),
            "BF-ODIs-100": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(10)").text.strip(),
            "BF-ODIs-50": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(11)").text.strip(),
            "BF-ODIs-4s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(12)").text.strip(),
            "BF-ODIs-6s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(13)").text.strip(),
            "BF-ODIs-Ct": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(14)").text.strip(),
            "BF-ODIs-St": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(15)").text.strip(),
            "BF-T20Is-Mat": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2)").text.strip(),
            "BF-T20Is-Inns": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(3)").text.strip(),
            "BF-T20Is-NO": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(4)").text.strip(),
            "BF-T20Is-Runs": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(5)").text.strip(),
            "BF-T20Is-HS": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(6)").text.strip(),
            "BF-T20Is-Ave": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(7)").text.strip(),
            "BF-T20Is-BF": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(8)").text.strip(),
            "BF-T20Is-SR": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(9)").text.strip(),
            "BF-T20Is-100": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(10)").text.strip(),
            "BF-T20Is-50": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(11)").text.strip(),
            "BF-T20Is-4s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(12)").text.strip(),
            "BF-T20Is-6s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(13)").text.strip(),
            "BF-T20Is-Ct": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(14)").text.strip(),
            "BF-T20Is-St": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(15)").text.strip(),
            "BF-FC-Mat": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(2)").text.strip(),
            "BF-FC-Inns": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(3)").text.strip(),
            "BF-FC-NO": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(4)").text.strip(),
            "BF-FC-Runs": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(5)").text.strip(),
            "BF-FC-HS": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(6)").text.strip(),
            "BF-FC-Ave": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(7)").text.strip(),
            "BF-FC-BF": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(8)").text.strip(),
            "BF-FC-SR": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(9)").text.strip(),
            "BF-FC-100": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(10)").text.strip(),
            "BF-FC-50": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(11)").text.strip(),
            "BF-FC-4s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(12)").text.strip(),
            "BF-FC-6s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(13)").text.strip(),
            "BF-FC-Ct": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(14)").text.strip(),
            "BF-FC-St": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(15)").text.strip(),
            "BF-LISTA-Mat": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(2)").text.strip(),
            "BF-LISTA-Inns": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(3)").text.strip(),
            "BF-LISTA-NO": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(4)").text.strip(),
            "BF-LISTA-Runs": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(5)").text.strip(),
            "BF-LISTA-HS": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(6)").text.strip(),
            "BF-LISTA-Ave": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(7)").text.strip(),
            "BF-LISTA-BF": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(8)").text.strip(),
            "BF-LISTA-SR": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(9)").text.strip(),
            "BF-LISTA-100": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(10)").text.strip(),
            "BF-LISTA-50": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(11)").text.strip(),
            "BF-LISTA-4s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(12)").text.strip(),
            "BF-LISTA-6s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(13)").text.strip(),
            "BF-LISTA-Ct": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(14)").text.strip(),
            "BF-LISTA-St": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(15)").text.strip(),
            "BF-T20s-Mat": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(2)").text.strip(),
            "BF-T20s-Inns": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(3)").text.strip(),
            "BF-T20s-NO": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(4)").text.strip(),
            "BF-T20s-Runs": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(5)").text.strip(),
            "BF-T20s-HS": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(6)").text.strip(),
            "BF-T20s-Ave": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(7)").text.strip(),
            "BF-T20s-BF": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(8)").text.strip(),
            "BF-T20s-SR": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(9)").text.strip(),
            "BF-T20s-100": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(10)").text.strip(),
            "BF-T20s-50": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(11)").text.strip(),
            "BF-T20s-4s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(12)").text.strip(),
            "BF-T20s-6s": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(13)").text.strip(),
            "BF-T20s-Ct": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(14)").text.strip(),
            "BF-T20s-St": player_index_soup.select_one("#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(15)").text.strip(),
            "B-ODIs-Mat": 0,
            "B-ODIs-Inns": 0,
            "B-ODIs-Balls": 0,
            "B-ODIs-Runs": 0,
            "B-ODIs-Wkts": 0,
            "B-ODIs-BBI": 0,
            "B-ODIs-BBM": 0,
            "B-ODIs-Ave": 0,
            "B-ODIs-Econ": 0,
            "B-ODIs-SR": 0,
            "B-ODIs-4w": 0,
            "B-ODIs-5w": 0,
            "B-ODIs-10": 0,
            "B-T20Is-Mat": 0,
            "B-T20Is-Inns": 0,
            "B-T20Is-Balls": 0,
            "B-T20Is-Runs": 0,
            "B-T20Is-Wkts": 0,
            "B-T20Is-BBI": 0,
            "B-T20Is-BBM": 0,
            "B-T20Is-Ave": 0,
            "B-T20Is-Econ": 0,
            "B-T20Is-SR": 0,
            "B-T20Is-4w": 0,
            "B-T20Is-5w": 0,
            "B-T20Is-10": 0,
            "B-FC-Mat": 0,
            "B-FC-Inns": 0,
            "B-FC-Balls": 0,
            "B-FC-Runs": 0,
            "B-FC-Wkts": 0,
            "B-FC-BBI": 0,
            "B-FC-BBM": 0,
            "B-FC-Ave": 0,
            "B-FC-Econ": 0,
            "B-FC-SR": 0,
            "B-FC-4w": 0,
            "B-FC-5w": 0,
            "B-FC-10": 0,
            "B-LISTA-Mat": 0,
            "B-LISTA-Inns": 0,
            "B-LISTA-Balls": 0,
            "B-LISTA-Runs": 0,
            "B-LISTA-Wkts": 0,
            "B-LISTA-BBI": 0,
            "B-LISTA-BBM": 0,
            "B-LISTA-Ave": 0,
            "B-LISTA-Econ": 0,
            "B-LISTA-SR": 0,
            "B-LISTA-4w": 0,
            "B-LISTA-5w": 0,
            "B-LISTA-10": 0,
            "B-T20s-Mat": 0,
            "B-T20s-Inns": 0,
            "B-T20s-Balls": 0,
            "B-T20s-Runs": 0,
            "B-T20s-Wkts": 0,
            "B-T20s-BBI": 0,
            "B-T20s-BBM": 0,
            "B-T20s-Ave": 0,
            "B-T20s-Econ": 0,
            "B-T20s-SR": 0,
            "B-T20s-4w": 0,
            "B-T20s-5w": 0,
            "B-T20s-10": 0
        })

        print(players_data)
        exit(1)

def get_table_cell(soup, row, cell):
    player_index_soup.select_one(
        "#ciHomeContentlhs > div.pnl490M > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2)").text.strip()