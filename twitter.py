
credito = ("Jose Jorquera", "gtd", 2016)
tweet = None
likes = 0
retweets = 0
infotweet = {}
listatweet = []
print ("Bienvenidos a la aplicacion.")
usuario = input("Cual es tu usuario?:")
for i in [1,2,3]:
	print ("Tweet numero:",i)
	tweet = input("Que esta pasando?: ")
	likes = int(input("Cuantos likes quieres? :"))
	retweets = input("Cuantos retweets? :")
	infotweet = {"Autor": usuario, "Mensaje": tweet, "Likes": likes, "Retweets": retweets}
	listatweet.append(infotweet)
	if likes > 1:
		print ("Su tweet tiene 'me gusta'")
	elif likes == 1:
		print ("Tu tweet solo tiene un me gusta")
	else:
		print ("no tienes me gusta :(")
	if (retweets > 0): print ("Este tweet no tiene rtws")

for tweet in listatweet:
	print(str(tweet))
