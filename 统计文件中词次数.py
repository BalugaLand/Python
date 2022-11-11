text = open("D:/text.txt","r",encoding="UTF-8").read()    # 英文
c = True
counts={}
qian20={}
text1 = text.lower().replace(",","").replace(".","").replace("\"","").strip().split()
for i in text1:
    counts[i] = 0
for n in text1:
    if n in counts:
        counts[n] += 1
print(counts)
ff = dict(sorted(counts.items(),key = lambda d:d[1],reverse=True))
print("次数最多的20个词:{}".format(str(list(ff.keys())[:20]).replace("[","").replace("]","")))






# import jieba                # 中文
# f = open(file="D:/西游记之女儿国奇遇.txt",mode="r").read()
# words=jieba.lcut(f)
# counts={}
# for word in words:
#     if len(word) == 1:
#         continue
#     counts[word] = 0
# for word in words:
#     if len(word) == 1:
#         continue
#     else :
#         counts[word] += 1
# print(counts)
# ci = list(dict(sorted(counts.items(),key = lambda d:d[1],reverse=True)).keys())[:20]
# print(f"次数最多的20个词:{ci}")
