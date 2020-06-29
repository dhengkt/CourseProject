s4 = "Immutable Object"
s5 = "Immutable Object"
print(id(s4))
print(id(s5))

# In this function
# O(n) is the worst and average case
# O(i) is the best case
def isPalindrome(words):
    isPal = True                        # 1 Assignment
    for ch in range(len(words) // 2):   # n/2 comparisons
        if words[ch] != words[-ch-1]:   # n/2 comparisons
            isPal = False               #
            break
    return isPal


def main():
    s = input("Enter a string: ")
    if isPalindrome(s):
        print(s + " is a palindrome.")
    else:
        print(s + " is not a palindrome.")

    x = 3
    y = 4
    print(x,y)
    swap(x, y)
    print(x,y)

main()