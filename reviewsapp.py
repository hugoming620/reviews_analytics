#reviews_analytics

data = []
count = 0
with open ('reviews.txt','r') as f :
	for line in f :
		data.append(line.strip())
		count += 1
		if count % 100000 == 0 :
			print (len(data)) 

print('檔案讀取完畢，總共有', len(data) ,'筆資料')


sum_len = 0
for word in data :
	sum_len = sum_len + len(word)

print('每筆留言平均數是：' ,sum_len / len(data))


new = []
for reviews in data :
	if len(reviews) < 100 :
		new.append(reviews)
print('一共有',len(new),'筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for review in data :
	if 'good' in review :
		good.append(review)
print('一共有',len(good),'留言有good')
print(good[5])


#list comprehension
good = [review for review in data if 'good' in review]
print(len(good))


#文字計數
wc = {}
for d in data :
	words = d.split(' ')
	for word in words:
		if word in wc :
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

print(len(wc))
print(wc['Hugo'])

while True:
	word = input('你想查什麼字： ')	
	if word == 'q':
		break	
	if word in wc:
		print(word,'這個字出現過' ,wc[word],'次')
	else:
		print('這個字沒有出現過～')
print('感謝使用')


