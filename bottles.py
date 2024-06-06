def bottle_song(num):
	
	while (num > 1):
		lyric = f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num - 1} bottles of beer on the wall."
		print(lyric)
		num -= 1

bottle_song(6)

