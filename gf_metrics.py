'''
🏳️ METRICS:

- makes 3 variables global for ease of access
    - errors: how many wrong answers the player has provided
    - score: how many correct answers the player ahs provided
    - keyword: the keyword at play (can change it for a whole new game!)

'''
class Metrics:
    def __init__(self):
        self.errors = 0
        self.score = 0
        self.keyword = "gatorade" # fill in the blank!

metrics = Metrics()