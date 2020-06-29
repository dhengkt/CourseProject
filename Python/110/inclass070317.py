#inclass070317.py
#Katie Chi

#Those are practice from class.

x = 0
for i in [0,2,4,6]:
	print(i)
	x = x + i
print(i,x)

list(range(8,3,-1))

for name in ["Carlos", "Connor", "Eben", "Isaac", "John", "Katie"]:
	if name == "Katie":
		print("My name is", name + ".")
	else:
		print("Your name is", name + ".")

for words in ["Once", "upon", "a", "time", "..."]:
	print(words, end=" ")
