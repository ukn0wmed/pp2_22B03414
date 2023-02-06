def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


print(is_palindrome("Ata"))
print(is_palindrome("Do geese see God"))
print(is_palindrome("Hello there"))
