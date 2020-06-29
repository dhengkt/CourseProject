DIGIT_ARRAY = "0123456789ABCDEF"

def baseConvert(num, base, ans):
    if num < 0 or base <= 0 or base > 16:
        return None
    elif num < base:
        answer = DIGIT_ARRAY[num] + ans
        return answer
    else:
        answer = DIGIT_ARRAY[num % base] + ans
        return baseConvert(num // base, base, answer)

# s = ""
# n = eval(input("Input a  number: "))
# print("Hex rep of {} is {}".format(n, baseConvert(n, 16, s)))

def binomialCoefficient(n, k):
    if k <= 0 or n < 1 or k > n:
        return "Error: Please check the input numbers"
    elif k == 1:
        return n
    elif n == k or k == 0:
        return 1
    else:
        return binomialCoefficient(n - 1, k - 1) + binomialCoefficient(n - 1, k)


n = eval(input("Enter the number of n: "))
k = eval(input("Enter the number of k: "))
print("Combination of choosing {} out of {} is {}".format(k, n, binomialCoefficient(n, k)))
