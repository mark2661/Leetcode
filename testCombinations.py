def generate_combinations(letter, remaining, main_dict, max_length, i = 0):
    val = get_letter(remaining,i,main_dict)
    i += 1
    if val and len(letter) < max_length:
        return [letter + val] + generate_combinations(letter, remaining, main_dict, max_length, i) \
               + generate_combinations(letter + val, remaining, main_dict, max_length, i)
    else:
        return []

def get_letter(digit,i,main_dict):
    letter_list = main_dict[digit]
    if i < len(letter_list):
        return letter_list[i]
    else:
        return None

def get_letters(digit,main_dict):
    return main_dict[digit]

class Solution:
    def letterCombinations(self, digits):
        length = len(digits)
        answer = []
        main_dict = dict()
        main_dict["2"] = ("a", "b", "c")
        main_dict["3"] = ("d", "e", "f")
        main_dict["4"] = ("g", "h", "i")
        main_dict["5"] = ("j", "k", "l")
        main_dict["6"] = ("m", "n", "o")
        main_dict["7"] = ("p", "q", "r", "s")
        main_dict["8"] = ("t", "u", "v")
        main_dict["9"] = ("w", "x", "y", "z")

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(get_letters(digits, main_dict))

        main_digit = digits[0]
        digits = digits[1:]
        main_letter_list = get_letters(main_digit, main_dict)
        n = 2
        while len(digits) > 0:
            answer = []
            for letter in main_letter_list:
                answer = answer + generate_combinations(letter, digits[0], main_dict, n)
            main_letter_list = answer
            digits = digits[1:]
            n += 1

        return [n for n in answer if len(n) == length]


my_solution = Solution()
print(my_solution.letterCombinations("5678"))