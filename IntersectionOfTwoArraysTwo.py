def make_dict(dictionary,lst):
    for number in lst:
        dictionary[number] = dictionary[number] + 1 if number in dictionary.keys() else 1




class Solution:
    def intersect(self, nums1, nums2):
        my_dict_one = dict()
        my_dict_two = dict()
        nums3 = []

        make_dict(my_dict_one,nums1)
        make_dict(my_dict_two, nums2)

        for key in my_dict_one.keys():
            if my_dict_two.get(key) != None:
                nums3 += [key] * min(my_dict_one[key], my_dict_two[key])

        return nums3

