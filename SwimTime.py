import json

class SwimTime:
    def __init__(self):
        self.location = "Henrey Gunn High School"
        self.date = "11/23/24"
        self.stroke = "Butterfly"
        self.length = 50 
        self.time = 190
        self.rank = 1/2
        self.note = "almost got DQed two hand touch"
    def __repr__(self):
       return f"I went to {self.location} on {self.date} and did {self.stroke} {self.length} meter\yard, and got a time of {self.time} with a rank of {self.rank} my thoughts are {self.note}. " 
    

    def to_json(self):
        data = {
            "date": self.date,
            "location": self.location,
            "stroke": self.stroke,
            "length": self.length,
            "time": self.time,
            "rank": self.rank,
            "notes": self.note
        }
        data = json.dumps(data)
        return data
    
    def from_json(self, data):
        data = json.loads(data)

        self.date = data["date"]
        self.location = data["location"]
        self.stroke = data["stroke"]
        self.length = data["length"]
        self.time = data["time"]
        self.rank = data["rank"]
        self.note = data["notes"]
        
    def from_dict(self, data):
        self.date = data["date"]
        self.location = data["location"]
        self.stroke = data["stroke"]
        self.length = data["length"]
        self.time = data["time"]
        self.rank = data["rank"]
        self.note = data["notes"]