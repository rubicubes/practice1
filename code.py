import re

with open("wagahaihanekodearu.txt", encoding="utf-8") as f:
    text = f.read()

len_four = re.findall(r"[一-龠]{4}", text)
words = re.findall(r"[一-龠]{4}", text)
longest_words = [""]
length = 0
for i in words:
  l = len(i)
  if l > length:
    longest_word = [i]
    length = l
  elif l == length:
    longest_words.append(i)
print("四字連続漢字の数:", len(matches))
print("最初の10個:", matches[:10])
print(longest_words)
