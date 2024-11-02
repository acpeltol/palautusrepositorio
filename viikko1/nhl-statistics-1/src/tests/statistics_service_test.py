from statistics_service import StatisticsService, SortBy
from player import Player
from enum import Enum
import unittest

#class SortBy(Enum):
#    POINTS = 1
#    GOALS = 2
#    ASSISTS = 3



class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

        

        self.but = PlayerReaderStub().get_players()

    def test_stats_players_value(self):
        k = self.stats._players[0]

        q = self.but[0]

        self.assertEqual(str(k), str(q))

    def test_search_existing_player(self):
        player1 = self.stats.search("Semenko")

        result = self.but[0]

        self.assertEqual(str(player1),str(result))

    def test_search_NOT_existing_player(self):
        player1 = self.stats.search("Fulimaonso")

        self.assertEqual(player1,None)

    def test_team(self):
        result = str(self.but[1])

        result_test = str(self.stats.team("PIT")[0])

        self.assertEqual(result,result_test)

    def test_top(self):

        result_test = self.stats.top(1)

        result_test[0] = str(result_test[0])
        result_test[1] = str(result_test[1])

        result_listen = [str(self.but[4]),str(self.but[1])]

        self.assertEqual(result_test, result_listen)

    def test_sort_by_points(self):
        result_test = self.stats.top(1, SortBy.POINTS)

        result_test[0] = str(result_test[0])
        result_test[1] = str(result_test[1])

        result_listen = [str(self.but[4]),str(self.but[1])]

        self.assertEqual(result_test, result_listen)

    def test_sort_by_goals(self):
        result_test = self.stats.top(1, SortBy.GOALS)

        result_test[0] = str(result_test[0])
        result_test[1] = str(result_test[1])

        result_listen = [str(self.but[1]),str(self.but[3])]

        self.assertEqual(result_test, result_listen)

    def test_sort_by_assists(self):
        result_test = self.stats.top(4, SortBy.ASSISTS)

        result_test = [str(i) for i in result_test]

        result_listen = [str(self.but[4]),str(self.but[3]),str(self.but[1]),str(self.but[2]),str(self.but[0])]

        self.assertEqual(result_test, result_listen)




