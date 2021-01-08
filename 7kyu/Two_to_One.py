# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
def longest(s1, s2):
    s3 = s1 + s2
    string_list = []
    for char in s3:
        if char not in string_list:
            string_list.append(char)
    return "".join(sorted(string_list))