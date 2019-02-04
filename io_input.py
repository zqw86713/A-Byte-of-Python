import string

def remove_punctuations(word):
	return "".join(i.lower() for i in word if i in string.ascii_letters )

def reverse(text):
	return text[::-1]

def is_palindrom(text):
	test = remove_punctuations(text)
	return text == reverse(text)


something = input("Enter text: ")

if is_palindrom(something):
	print("yes, it is a palindrom.")
else:
	print("no, it is not a palindrom.")


#	marks = ('.', '?', '!', ':', ';', '-', '_', '(', ')', '[', ']', '...',#	 '\'','"', '"','\/' ',')

