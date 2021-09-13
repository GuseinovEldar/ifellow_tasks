class Clocks():
    def __init__(self):
        self.hour = int(input())
        self.minute = int(input())

    def degree(self):
        if abs(((((self.minute / 60) + (self.hour % 12)) / 12) - (self.minute / 60)) * 360) > 180:
            return 360 - abs(((((self.hour % 12) + (self.minute / 60)) / 12) - (self.minute / 60)) * 360)
        return print (abs(((((self.hour % 12) + (self.minute / 60)) / 12) - (self.minute / 60)) * 360))

run = Clocks()
run.degree()