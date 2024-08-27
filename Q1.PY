def reverse_and_capitalize(sentence):
	words = sentence.split()
	reversed_words = words[::-1]
	capitalized_words = [word.capitalize() for word in reversed_words]
	result = " ".join(capitalized_words)
	return result
sentence = "The Ganges is the longest river in India while The Nile in World"
print(reverse_and_capitalize(sentence))