
import random, colors

with open("words.txt", "r") as read:
	words = read.read().strip("\n").split()
	read.close()

final_word = []
word = random.choice(words)
slot1, slot2, slot3, slot4, slot5 = " ", " ", " ", " ", " "

lives = 6

alp = dict(
a = 0,
b = 0,
c = 0,
d = 0,
e = 0,
f = 0,
g = 0,
h = 0,
i = 0,
j = 0 ,
k = 0,
l = 0,
m = 0,
n = 0,
o = 0,
p = 0,
q = 0,
r = 0,
s = 0,
t = 0,
u = 0,
v = 0,
w = 0,
x = 0,
y = 0,
z = 0,
)

def check_letters():
	global word, alp
	for i in range(len(word)):
		alp[word[i]] += 1

def print_word():
	global word, final_word, slot1, slot2, slot3, slot4, slot5, alp, lives
	word_list = list(word)
	
	final_word = []

	alp_copy = alp.copy()

	for i in range(5):
		slot = [slot1, slot2, slot3, slot4, slot5][i]
		if slot == word_list[i] and alp_copy[slot] > 0:
			alp_copy[slot] -= 1
			final_word.append(f"{colors.green}{slot}{colors.end}")
		else:
			final_word.append(None)
	for i in range(5):
		slot = [slot1, slot2, slot3, slot4, slot5][i]
		if final_word[i] is None:
			if slot in word_list and alp_copy[slot] > 0:
				if word_list.count(slot) > final_word.count(f"{colors.green}{slot}{colors.end}") + final_word.count(f"{colors.yellow}{slot}{colors.end}"):
					alp_copy[slot] -= 1
					final_word[i] = f"{colors.yellow}{slot}{colors.end}"
				else:
					final_word[i] = f"{colors.red}{slot}{colors.end}"
			else:
				final_word[i] = f"{colors.red}{slot}{colors.end}"
	
	print(*final_word)
	return final_word

while True:
	print(f"lives: {lives}")
	check_letters()
	slot1, slot2, slot3, slot4, slot5 = input("space the letters with \" \":\n").split(" ")
	print_word()
	
