import json

class CubeSolve:
    def __init__(self):
        self.location = "UC Berkeley"
        self.date  = "11/3/24"
        self.event = "3x3x3"
        self.round = 1
        self.rank = 147 
        self.solves = [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
    
    def __repr__(self):
        if self.best() < 1:
            return f"I went to {self.location} on {self.date} and did a {self.event} solve. In round {self.round}, I got a rank #{self.rank}. My best time was less than a second {self.best()} and my average was {self.average()} seconds."
        else:
            return f"I went to {self.location} on {self.date} and did a {self.event} solve. In round {self.round}, I got a rank #{self.rank}. My best time was {self.best()} and my average was {self.average()} seconds."

    def best(self):
        return min(self.solves)
    
    def average(self):
        middles = self.solves
        middles.remove(min(self.solves))
        middles.remove(max(self.solves))

        return sum(middles) / 3
    
    def to_json(self):
        data =  {
            "date": self.date,
            "location": self.location,
            "event": self.event, 
            "round": self.round,
            "rank": self.rank,
            "five_solves": self.solves 
        }

        data = json.dumps(data)
        return data
    
    def from_json(self, data):
        data = json.loads(data)

        self.date = data["date"]
        self.location = data["location"]
        self.event = data["event"]
        self.round = data["round"]
        self.rank = data["rank"]
        self.solves = data["five_solves"]
    
    def from_dict(self, data):
        self.date = data["date"]
        self.location = data["location"]
        self.event = data["event"]
        self.round = data["round"]
        self.rank = data["rank"]
        self.solves = data["five_solves"]
    