import random


class Mastermind:
    def __init__(self):  # Constructor
        self._colors = 0
        self._positions = 0
        self._secret_code = []
        self._rounds = 0
        self._game_over = False

    def setup_game(self, colors, positions):  # Setter
        self._colors = colors
        self._positions = positions
        self._generate_secret_code()
        self._game_over = False
        self._rounds = 0

    def _generate_secret_code(self):  # Private method
        self._secret_code = [random.randint(1, self._colors)
                             for _ in range(self._positions)]

    def _get_hint(self, guess):  # Private method
        correct_positions = 0
        correct_colors = 0
        temp_code = self._secret_code.copy()
        temp_guess = guess[:]

        # Find correct positions
        for i in range(self._positions):
            if temp_guess[i] == temp_code[i]:
                correct_positions += 1
                temp_code[i] = temp_guess[i] = None
        # Find correct colors
        for i in range(self._positions):
            if temp_guess[i] and temp_guess[i] in temp_code:
                correct_colors += 1
                temp_code[temp_code.index(temp_guess[i])] = None
        return '*' * correct_positions + 'o' * correct_colors

    def _get_user_guess(self):  # Private method
        while True:
            guess = input(f"Enter your guess ({self._positions}"
                          f" digits) or end: ")
            if guess == "end":
                self.dump_game_state()
            elif len(guess) == self._positions:
                try:
                    converted_guess = [int(i) for i in guess]
                    return converted_guess
                except ValueError:
                    print("Invalid input. Please enter only numeric digits.")
            else:
                print(f"Incorrect number of digits. Please enter exactly "
                      f"{self._positions} digits.")

    def dump_game_state(self):  # Public method
        if not self._game_over:
            print(f"Secret code: {self._secret_code}")
            print(f"Total rounds played: {self._rounds}")
            exit()
        else:
            print('Still playing')

    def playing_game(self):  # Public method
        print(f"Starting Mastermind with {self._colors} colors and "
              f"{self._positions} positions.")
        while not self._game_over:
            # While game is not over it will run the loop
            guess = self._get_user_guess()
            self._rounds += 1
            hint = self._get_hint(guess)
            self._display_hint(hint)
            self._game_over = self._is_game_finished(hint)


    def _display_hint(self, hint):  # Private method
        print(f"Hint: {hint}")

    def _is_game_finished(self, hint):  # Private method
        return hint == '*' * self._positions
        # If it's correct, it will print 4 stars


if __name__ == '__main__':
    game = Mastermind()
    game.setup_game(6, 4)
    game.playing_game()
    game.dump_game_state()
