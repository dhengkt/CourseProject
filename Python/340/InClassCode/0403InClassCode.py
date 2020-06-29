
def rmCharAndReverse(string, char):

    ans = ""

    for i in range(len(string)):
        if string[i] != char:
            ans = string[i] + ans

    return ans

testString = "akadhenghdhdd"
print(rmCharAndReverse(testString, 'd'))


candidates = ["bernie", "pete", "kamela", "elizabeth"]

for candidates in candidates:
    print(candidates)