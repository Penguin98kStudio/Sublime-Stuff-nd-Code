def store(new: str = "") -> str:
	try:
		store.history
		if new:
			store.history += new + "\n"
	except AttributeError:
		store.history = new + "\n"
	return store.history


for _ in range(int(input("Enter Count: "))):
	store(input("Enter Text: "))

print("What you entered was:\n" + store())
