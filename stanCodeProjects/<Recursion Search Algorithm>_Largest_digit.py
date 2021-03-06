"""
File: largest_digit.py
Name: AO Chuang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.

* Rules
1. Do NOT use data structure(list, tuple...) and string(str) in find_largest_digit().
2. Do NOT use for loop & while loop , only 'recursion function' are allowed.
3. O(N) efficiency
"""


def main():
    print(find_largest_digit(12345))      # 5
    print(find_largest_digit(281))        # 8
    print(find_largest_digit(6))          # 6
    print(find_largest_digit(-111))       # 1
    print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
    ans = find_largest_digit_helper(str(n))
    return ans


def find_largest_digit_helper(s):

    if len(s) <= 1:  # Base Case
        return s

    else:
        s1 = s[0]
        s2 = s[1]

        if not s1.isdigit():
            s = s[1:len(s)]
        else:
            if s1 >= s2:  # if s1 > s2
                s = s1 + s[2:len(s)]  # s1 will replace s2
            else:  # if s2 > s1
                s = s[1:len(s)]  # s1 will be dropped

        return find_largest_digit_helper(s)


if __name__ == '__main__':
    main()
