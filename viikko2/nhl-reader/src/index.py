from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table
from rich.console import Console


def main():

    print(f"Select season [purple][2018-19/2019-20/2020-21/2022-23/2023-24/2024-25/][/purple]: ")
    season = input("")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    players = PlayerReader(url)
    stats = PlayerStats(players)

    print(f"Select nationality [purple][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/][/purple]: ")
    country = input("")

    sorted_players = stats.top_scorers_by_nationality(country)

    table = Table(title=f"Top scorers of {country} season {season}")

    table.add_column("name", justify="left", style="cyan", no_wrap=True)
    table.add_column("team", justify="right", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in sorted_players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    Console().print(table)

if __name__ == "__main__":
    main()
