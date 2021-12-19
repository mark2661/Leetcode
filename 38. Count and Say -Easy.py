
class Solution:
    def countAndSay(self, n):

        my_dict = dict()
        return_string = ""
        for i in range(10):
            my_dict[i] = 0

        for char in str(n):
            my_dict[char] += 1

        for key in my_dict.keys():
            return_string = return_string + str(my_dict[key]) + str(key)

        return return_string
