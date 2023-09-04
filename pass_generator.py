from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class Password:
    def __init__(self):
        self.nr_letters = randint(8, 10)
        self.nr_symbols = randint(2, 4)
        self.nr_numbers = randint(2, 4)

    def generate(self):
        # Hard Level
        password_letters = [choice(letters) for _ in range(self.nr_letters)]
        password_num = [choice(numbers) for _ in range(self.nr_numbers)]
        password_sym = [choice(symbols) for _ in range(self.nr_symbols)]

        password_list = password_sym + password_num + password_letters
        shuffle(password_list)

        password = "".join(password_list)

        return password

