likes = 10
retweets = 0
try:	
	media = likes / retweets
except ZeroDivisionError:
	media = 0
print(media)
