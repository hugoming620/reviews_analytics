#reviews_analytics

data = []
count = 0
with open ('reviews.txt','r') as f :
	for line in f :
		data.append(line.strip())
		count += 1
		if count % 100000 == 0 :
			print (len(data)) 


print(len(data))


