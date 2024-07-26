import matplotlib.pyplot as plt

def top_8_game_sales(game_data, graph_type):
    games = list(game_data.keys())
    sales = list(game_data.values())

    if graph_type == 'bar':
        plt.bar(games, sales, color='green', width=0.8)
    elif graph_type == 'line':
        plt.plot(games, sales, color='green', marker='o', linestyle='-')
    elif graph_type == 'pie':
        plt.pie(sales, labels=games, autopct='%1.1f%%')
    else:
        print("Invalid graph type chosen. Please choose from 'bar', 'line', or 'pie'.")
        return

    plt.title("Top 8 Best-Selling Video Games")
    if graph_type != 'pie':
        plt.xlabel("Game")
        plt.ylabel("Sales (in millions)")
    plt.show()

game_data = {
    "The Elder Scrolls V: Skyrim": 60,
    "Red Dead Redemption 2": 64,
    "Mario Kart 8 Deluxe": 70.43,
    "PUBG": 75,  "Wii Sports": 82.9,  "Grand Theft Auto V": 200,  "Minecraft":300, "Tetris": 520
 }

graph_types = ['bar', 'line', 'pie']
print("Available Graph Types:", graph_types)
choice = input("Choose the type of graph (bar, line, pie): ").lower()

while choice not in graph_types:
    choice = input("Invalid choice. Please choose from 'bar', 'line', or 'pie': ").lower()

top_8_game_sales(game_data, choice)
