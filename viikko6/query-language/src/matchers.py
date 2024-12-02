# class QueryBuilder:
#     def __init__(self):
#         #self._matchers = matchers
#         pass

#     def plays_in(self, player):
#         return player.team == self._team
    
#     def has_at_least(self, value, attr):
#         player_value = getattr(player, self._attr)

#         return player_value >= self._value






class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        result = False

        for matcher in self._matchers:
            if matcher.test(player):
              result = True  

        return result

class All:
    def __init__(self):
        pass
    def test(self,player):
        return True
    
class Not:
    def __init__(self, has_at_least):
        self._class = has_at_least

    def test(self, player):
        if self._class.test(player):
            return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
