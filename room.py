class Room:

    def __init__(self, number = 0):

        self.objects = {}
        self.number = number
        self.owner = None
        self.ways = []