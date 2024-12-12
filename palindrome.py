 def is_palindrome(n):
    str_n = str(n)
    if str_n == str_n[::-1]:
        return "Yes"
    else:
        return "No"
