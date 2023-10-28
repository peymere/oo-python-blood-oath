from .bloodoath import BloodOath


class Follower:
    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)

    @property
    def blood_oaths(self):
        return [b_o for b_o in BloodOath.all if b_o.follower == self]

    @property
    def cults(self):
        return [b_o.cult for b_o in self.blood_oaths]

    def join_cult(self, cult):
        BloodOath(self, cult)

    

    @classmethod
    def of_a_certain_age(cls, min_age):
        return [f for f in Follower.all if f.age >= min_age]
