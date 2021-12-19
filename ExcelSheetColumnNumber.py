
class Solution:
    def titleToNumber(self, s):
        my_dict = dict()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(alphabet)):
            my_dict[alphabet[i]] = i + 1

        total = 0
        if len(s) == 1:
            return my_dict[s[0]]
        for character,index in zip(s,range(len(s)-1,0,-1)):
            total += 25 * index * (alphabet.index(character) + 1) + my_dict[character]
        if len(s) > 1:
            total += my_dict[s[-1]]
        return total