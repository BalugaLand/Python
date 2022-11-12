import jieba
text = open("D:/text.txt", "r").read()
text = text.lower()
words = jieba.lcut(text)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    counts[word] = 0
for word in words:
    if len(word) == 1:
        continue
    counts[word] += 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print("{0:<8}{1:>8}次".format(word, count))
