from datetime import datetime

class BloodOath:
    all = []

    def __init__(self, follower, cult, initiation_date=datetime.now().date()):
        self.initiation_date = initiation_date
        self.cult = cult
        self.follower = follower
        BloodOath.all.append(self)