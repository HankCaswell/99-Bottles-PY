def bottle_song():
	bottles = 99
		
	while bottles > 0:
		print(f"{bottles}{is_plural(bottles)} of beer on the wall {bottles}{is_plural(bottles)} of beer. Take one down and pass it around, {bottles-1}{is_plural(bottles-1)} of beer on the wall.")
		bottles -= 1
	if bottles == 0:
		print(f"No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall ")

#Helper function to determine if "Bottles" in the string is plural

def is_plural(bottles):
	if bottles >1:
		return "bottles"
	return "bottle"
		
print(bottle_song(3))

####kldjsfalkfdajalskdfjdfls