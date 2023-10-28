from .bloodoath import BloodOath

class Cult:
    all = []

    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        Cult.all.append(self)

    def recruit_follower(self, follower):
        BloodOath(follower, self)

    def cult_population(self):
        return len([oath for oath in BloodOath.all if oath.cult == self])

    @classmethod
    def find_by_name(cls, name):
        if isinstance(name, str):
            for cult in cls.all:
                if cult.name == name:
                    return cult
        else:
            print("Name must be a string")
            return None

    @classmethod
    def find_by_location(cls, location):
        if isinstance(location, str):
            return [cult for cult in cls.all if cult.location == location]
        else:
            print("Location must be a string")
            return None

    @classmethod
    def find_by_founding_year(cls, year):
        if isinstance(year, int):
            return [cult for cult in cls.all if cult.founding_year == year]
        else:
            print("Year must be a number")
            return None    