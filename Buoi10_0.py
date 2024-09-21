favorite_games = ["Free Fire", "Liên Quân", "PUBG", "FIFA", "GTA"]

print(favorite_games[0])
n = len(favorite_games)
print(n)
favorite_games.append("Minecraft")
n = len(favorite_games)
print(n)
print(favorite_games)
favorite_games.pop(4)
print(favorite_games)
favorite_games.remove("FIFA")
print(favorite_games)

favorite_games[2] = "PUBG Mobile"
print(favorite_games)