class Player:
  def __init__(self, name, position):
    self.name = name
    self.position = position

class Team:
  def __init__(self, name):
    self.name = name
    self.players = []

  def add_player(self, player):
    self.players.append(player)

  def list_players(self):
    for player in self.players:
      print(f"Player name: {player.name}, as {player.position}")

  def remove_player(self, player):
    self.players.remove(player)

player1 = Player("Adriano", "obrońca")
player2 = Player("Jordano", "napastnik")
player3 = Player("Italiano", "bramkarz")
player4 = Player("Skrzydlano", "napastnik")

team = Team("Wariaty")
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)
team.add_player(player4)

team.list_players()
team.remove_player(player1)
print("-----")
team.list_players()