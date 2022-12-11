# define the text_to_lines function
def text_to_lines(text, max_length):
	# split the text into a list of words
	words = text.split()

	# initialize a list to hold the lines of text
	lines = []

	# initialize a variable to keep track of the current line
	current_line = ""

	# iterate over the words
	for word in words:
		# check if the current word can be added to the current line
		if len(current_line) + len(word) <= max_length:
			# add the word to the current line
			current_line += f"{word} "
		else:
			# add the current line to the list of lines
			lines.append(current_line)

			# start a new line and add the word to it
			current_line = f"{word} "

	# add the remaining line to the list of lines
	lines.append(current_line)

	# return the list of lines
	return lines


test_text1 = "Row, row, row your boat. Gently down the stream. Row, row, row your boat. Gently down the stream."
separate_lines = text_to_lines(test_text1, 25)

for line in separate_lines:
	print(f"{len(line)}: {line}")
