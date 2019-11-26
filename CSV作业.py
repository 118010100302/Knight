#求每门科目最高分、最低分、平均分
fr = open("score.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
Chinese = []
Math = []
English = []
for i in range(1,6):
    Chinese.append(ls[i][1])
    Math.append(ls[i][2])
    English.append(ls[i][3])
def average(subjects):
    s = 0.0
    for num in subjects:
        s = s + eval(num)
    return s / len(subjects)
Caverage = average(Chinese)
Maverage = average(Math)
Eaverage = average(English)
print("语文最高分：{} 语文最低分：{}".format(eval(max(Chinese)),eval(min(Chinese))),end = ' ')
print("语文平均分：{:.2f}".format(Caverage))
print("数学最高分：{} 数学最低分：{}".format(eval(max(Math)),eval(min(Math))),end = ' ')
print("数学平均分：{:.2f}".format(Maverage))
print("英语最高分：{} 英语最低分：{}".format(eval(max(English)),eval(min(English))),end = ' ')
print("英语平均分：{:.2f}".format(Eaverage))
fr.close()

#插入总分列
fo = open("score.csv","w")
def totalscore(x):
    s = 0
    for k in range(1,4):
        s = s + eval(x[k])
    return str(s)
lsg = ls[0]
lsa = ls[1]
lsb = ls[2]
lsc = ls[3]
lsd = ls[4]
lse = ls[5]
lsg.append('总分')
lsa.append(totalscore(lsa))
lsb.append(totalscore(lsb))
lsc.append(totalscore(lsc))
lsd.append(totalscore(lsd))
lse.append(totalscore(lse))
vlist = [ls[0],ls[1],ls[2],ls[3],ls[4],ls[5]]
for row in vlist:
    fo.write(",".join(row)+"\n")
fo.close()
#打开列表
fp = open("score.csv", "r")
ll = []
for line in fp:
    line = line.replace("\n","")
    ll.append(line.split(","))
print(ll)
fp.close()

    
    
