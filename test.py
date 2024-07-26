import matplotlib.pyplot as plt

def top_8_game_sales(game_data):
    # Extract game names and sales from the input dictionary
    games = list(game_data.keys())
    sales = list(game_data.values())

    # Plot a bar graph using Matplotlib
    plt.bar(games, sales, color='green', width=0.8)

    # Set the plot title and axis labels
    plt.title("Top 8 Best-Selling Video Games")
    plt.xlabel("Game")
    plt.ylabel("Sales (in millions)")

    # Show the grid lines and display the plot
    plt.grid(axis='y', color='gray', linestyle='--')
    plt.show()

game_data = {
        "The Elder Scrolls V: Skyrim": 60,
        "Red Dead Redemption 2": 64,
        "Mario Kart 8 Deluxe" : 70.43,
        "PUBG": 75,
        "Wii Sports": 82.9,
        "Grand Theft Auto V": 200,
        "Minecraft": 300,
        "Tetris": 520
        }

top_8_game_sales(game_data)
