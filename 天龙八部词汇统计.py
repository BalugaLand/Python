import os
import jieba
if not os.path.exists("D:/天龙八部词汇统计"):
    os.mkdir("D:/天龙八部词汇统计")
f1 = open("D:/天龙八部词汇统计/天龙八部词汇统计江纵乐2222202105.txt","w",encoding="UTF-8")
f2 = open("D:/天龙八部-网络版.txt","r",encoding="UTF-8")
fc = f2.read()
words = jieba.lcut(fc)
count={}
for word in words:
    if len(word) == 1:
        continue
    count[word] = 0
for word in words:
    if len(word) == 1:
        continue
    else:
        count[word]+=1

items = list(count.items())
items.sort(key=lambda x: x[1], reverse=True)
i = 0
try:
    while True:
        w, c = items[i]
        txt =("{0:<8}{1:>8}次\n".format(w, c))
        print(txt)
        f1.write(txt)
        i += 1
except:
    pass
f1.close()
f2.close()
