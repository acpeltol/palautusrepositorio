class PlayerStats:
    def __init__(self, players):
        self.players = players.players_list

    def top_scorers_by_nationality(self, nat):
        player_stats = []
        for i in self.players:
            if i.nat == nat:
                player_stats.append(i)

        sort = sorted(player_stats, key=lambda i: i.points, reverse=True)

        return sort