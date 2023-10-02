# Higher-Lower Game

This is a simple Python script for playing a Higher-Lower game. In this game, the user is presented with two random celebrities, along with information about them, and must guess which of the two has more followers on Instagram. The game keeps track of the user's score and allows them to continue playing or quit at any time.

## Table of Contents
- [Introduction](#introduction)
- [How to Play](#how-to-play)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Description](#code-description)
- [License](#license)

## Introduction

The Higher-Lower game is a fun and addictive guessing game. In each round, the player is shown information about two celebrities, including their names, descriptions, and countries. The player's task is to guess which of these two celebrities has more followers on Instagram. The game continues until the player decides to quit, and their score is displayed at the end of each round.

## How to Play

1. Run the script using Python 3.
2. You will be presented with two celebrities and their information.
3. Type 'A' if you think the first celebrity has more Instagram followers or 'B' if you think the second one has more.
4. The script will reveal the correct answer and update your score.
5. Repeat steps 2-4 for as long as you want to continue playing.
6. To quit the game, simply close the terminal or press `Ctrl+C`.

## Requirements

- Python 3.x

## Usage

1. Clone this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

   ```
   python3 higher_lower_game.py
   ```

5. Follow the on-screen instructions to play the game.

## Code Description

- `starter(firstData, secondData)`: This function takes two dictionaries containing information about two celebrities and presents the user with their details. It then prompts the user to guess which celebrity has more followers on Instagram and returns the user's choice as a string ('A' or 'B').

- `compare(firstData, secondData, playerChoice)`: The `compare` function takes the two dictionaries, the user's choice, and compares the follower count of the two celebrities. It returns a boolean value indicating whether the user's choice was correct or not.

- `clear()`: This function is used to clear the terminal screen. It uses platform-specific commands (`cls` for Windows and `clear` for other operating systems).

- `game()`: The `game` function is the main simulation of the game. It initializes the score, randomly selects two celebrities, and loops through rounds of the game until the player decides to quit. It calls the `starter` and `compare` functions to manage each round of the game.

## Author

This coffee machine simulation was created by @Omartalat.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
