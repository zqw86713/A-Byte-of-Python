poem = ''' \
Programing is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

#	open a file to edit.
f = open('poem.txt', 'w')

#	save text to the file..
f.write(poem)

#	close a file.
f.close()

#	if not specified, editor will use default read mode.
f = open('poem.txt')

while True:
	line = f.readline()
	#	if the length is zero, 
	if len(line) == 0:
		break
	#	Try not to start a new line.
	print(line, end = '')

#	to close a file.
f.close()