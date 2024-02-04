#You are given a string consisting of digits.
#Find the biggest two-digit value that is a consistent fragment of the given string. For example, two-digit consistent fragments of "58552" are ["50", "05", "55", "52"], representing the numbers [50, 5, 55, 52]. The biggest value among them is 55.
#Write a function: def solution(S) that, given a string S consisting of digits, returns the maximum two-digit value that is a consistent fragment of S.
#Examples: 1. Given S="50552", your function should return 55. 2. Given S="10101", your function should return 10. 3. Given S="88", your function should return 88.
#Assume that: string S is made only of digits (0-9); the number of digits of S is within the range [2..100]; S does not start with 'e'.



def solution(S):
    res = []
    for i in range(len(S)-1):
        res.append(S[i]+S[i+1])
    max_value = max(res)
    return int(max_value)

String = input("Enter the number to test:")
max_value = solution(String)
print("The maximum value for the string {} is {}".format(String,max_value))