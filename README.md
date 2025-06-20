# python-Guess-the-number
The Guess the Number game is an interactive command-line application where players guess a secret number between 1 and 50. With 'easy' (10 attempts) and 'hard' (5 attempts) modes, players receive feedback on their guesses until they win or run out of attempts.
Run the program using Python:

```bash
python 7.Guessthenumber.py
```

Follow the prompts to guess the number. Choose your difficulty level and try to guess the secret number within the allowed attempts!

## Detailed Logic Breakdown

### Step 1: Game Configuration and Setup

- **Imports**:
  - `import random`: Essential for generating a secret number.
  - `import logo_Art7`: Imports ASCII art for a polished game start.

- **Game Constants**:
  - `EASY_LEVEL_ATTEMPTS = 10`
  - `HARD_LEVEL_ATTEMPTS = 5`
  
  These constants improve code readability and maintainability.

### Step 2: Modular Design: The Helper Functions

- **set_difficulty(level_chosen)**:
  - Translates user input ('easy' or 'hard') into the corresponding number of attempts.

- **check_answer(guessed_number, answer, attempts)**:
  - Evaluates the player's guess, provides feedback, and manages the remaining attempts.

### Step 3: The Main Game Controller: The game() Function

- **Initialization**: Prints the logo and selects a random secret number.
- **Difficulty Selection**: Prompts the user for difficulty and validates input.
- **Main Guessing Loop**: Continues until the player guesses the number or runs out of attempts.

### Step 4: Executing a Single Turn

- **Status Update**: Informs the player of remaining attempts.
- **Get Player Input**: Prompts for the player's guess.
- **Evaluate and Update State**: Calls `check_answer` to provide feedback and update attempts.
- **Check for Loss Condition**: Ends the game if attempts reach zero.

### Step 5: Starting the Program

- **Code**: 
  ```python
  game()
  ```
- **Purpose**: This line initiates the game, starting the entire interactive process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
