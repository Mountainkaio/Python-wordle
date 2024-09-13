
import random, colors

with open("words.txt", "r") as read:
	words = read.read().strip("\n").split()
	read.close()

final_word = []
word = random.choice(words)
print(word)
slot1, slot2, slot3, slot4, slot5 = " ", " ", " ", " ", " "

def print_word():
	global word, final_word, slot1, slot2, slot3, slot4, slot5
	final_word = []
	word = list(word)
	
	if slot1 in word and slot1 == word[0]:
		final_word.append(f"{colors.green}{slot1}{colors.end}")
	elif slot1 in word and slot1 != word[0]:
		final_word.append(f"{colors.yellow}{slot1}{colors.end}")
	else:
		final_word.append(f"{colors.red}{slot1}{colors.end}")
	
	if slot2 in word and slot2 == word[1]:
		final_word.append(f"{colors.green}{slot2}{colors.end}")
	elif slot2 in word and slot2 != word[1]:
		final_word.append(f"{colors.yellow}{slot2}{colors.end}")
	else:
		final_word.append(f"{colors.red}{slot2}{colors.end}")
	
	if slot3 in word and slot3 == word[2]:
		final_word.append(f"{colors.green}{slot3}{colors.end}")
	elif slot3 in word and slot3 != word[2]:
		final_word.append(f"{colors.yellow}{slot3}{colors.end}")
	else:
		final_word.append(f"{colors.red}{slot3}{colors.end}")
	
	if slot4 in word and slot4 == word[3]:
		final_word.append(f"{colors.green}{slot4}{colors.end}")
	elif slot4 in word and slot4 != word[3]:
		final_word.append(f"{colors.yellow}{slot4}{colors.end}")
	else:
		final_word.append(f"{colors.red}{slot4}{colors.end}")
		
	if slot5 in word and slot5 == word[4]:
		final_word.append(f"{colors.green}{slot5}{colors.end}")
	elif slot5 in word and slot5 != word[4]:
		final_word.append(f"{colors.yellow}{slot5}{colors.end}")
	else:
		final_word.append(f"{colors.red}{slot5}{colors.end}")
		
	print(*final_word)
		
while True:
	slot1, slot2, slot3, slot4, slot5 = input("space the letters with \" \":\n").split(" ")
	print_word()
	
	
