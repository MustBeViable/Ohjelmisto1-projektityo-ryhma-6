class Playthrough:
    def __init__(self, player, location):
        self.player = player
        self.location = location
        self.money = 1000

nummela = "EFNU"
test_playthrough = Playthrough("Elias", nummela)
test_playthrough2 = Playthrough("Tuukka", nummela)

# testit
print(test_playthrough.player)
print(test_playthrough.location)
print(test_playthrough.money)