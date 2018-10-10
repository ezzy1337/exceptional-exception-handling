"""
Example Part 1: Attribute Error Thrown in can_build_at b/c settlement is None


Example Part 2: Score is calculated wrong because a None settlement got added to the players settlements list.

"""
class Player:
    def __init__(self):
        self.settlements = None
        self.cities = None
        self.roads = None
        self.has_longest_road = False
        self.has_largest_army = False

    @property
    def score():
        score = 0
        if self.settlements is not None:
            score += len(self.settlements) # Here lies a bug...cause there is a None in my list which adds a vp even though it's not a real city.
        if self.cities is not None:
            score += len(self.cities) * 2
        if self.has_longest_road:
            score += 2
        if self.has_largest_army:
            score += 2


class SettlersOfCatan:

    def can_build_at(self, x, y):
        for player in self.players:
            for settlement in player.settlements:
                coords = settlement.location # This could potentially throw AttributeError: 'NoneType' object has no attribute 'location'
                if 2 < coords[0] - x:
                    return False
                if 2 < coords[1] - y:
                    return False
        return True

    def build_settlement(self, x, y):
        if self.cannot_build_at(x, y)
            return None

        return Settlement(x, y)

    def exceptional_build_settlement(self, x, y):
        if self.cannot_build_at(x, y):
            raise InvalidPlacementError(f'${x}, ${y} is an invlaid placement.')
        return Settlement(x, y)
