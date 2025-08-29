import random
import string

choice = input("Type 'encode' or 'decode': ").lower()
message = input("Enter your message: ").lower()
words = message.split()
new_words = []

for word in words:
    if choice == "encode":
        if len(word) >= 3:
            prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            suffix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            new_words.append(prefix + word[1:] + word[0] + suffix)
        else:
            new_words.append(word[::-1])
    elif choice == "decode":
        if len(word) >= 3:
            core = word[3:-3]
            new_words.append(core[-1] + core[:-1])
        else:
            new_words.append(word[::-1])

print("Result:", " ".join(new_words))