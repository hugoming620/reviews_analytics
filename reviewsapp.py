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

