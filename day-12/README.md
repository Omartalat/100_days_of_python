# Number Guessing Game

This is a simple number guessing game written in Python. The game generates a random number between 1 and 100 (inclusive) and asks the player to guess it. The player can choose between two difficulty levels: "easy" (10 attempts) or "hard" (5 attempts). If the player runs out of attempts without guessing the number, they lose.

## How to Run the Game

1. Clone the repository to your local machine.
2. Run the game by executing the `guess-the-number-start.py` file with Python 3.

## Example Usage

```
$ python guess-the-number-start.py

  /$$$$$$                                               /$$$$$$$$ /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                             |__  $$__/| $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$ /$$  
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/|__/  
    
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100. 
Choose a difficulty. Type 'easy' or 'hard': easy
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too high.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 10
Too low.
Guess again.
You have 7 attempts remaining to guess the number.
Make a guess: 15
Too low.
Guess again.
You have 6 attempts remaining to guess the number.
Make a guess: 20
Too high.
Guess again.
You have 5 attempts remaining to guess the number.
Make a guess: 17
Too low.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: 18
You got it! The answer was 18
``` 

## Dependencies

This game requires the following Python modules:

* `art`: for the ASCII art logo.
* `random`: for generating random numbers.

## License

This code is licensed under the MIT License. Feel free to use it for educational or personal purposes.
