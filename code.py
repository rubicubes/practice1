import re

with open("wagahaihanekodearu.txt", encoding="utf-8") as f:
    text = f.read()
    
text = text.replace("\n", "")
four = re.findall(r"[一-龠]{4}", text)
words = re.findall(r"[一-龠]{4,}", text)
longest_words = [""]
length = 0
for i in words:
  l = len(i)
  if l > length:
    longest_words = [i]
    length = l
  elif l == length:
    longest_words.append(i)
print(len(four))
print(longest_words)
