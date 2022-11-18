# Name: Gaia Willis
dogs = ["Sadie","Molly","Ella","Milo","Buddy","Rocky", "Annabelle","Gonzo", "Diego", "Tank"]
dogs2 = []

def main():
		how_many = len(dogs)
		print("\nNumber of dogs in the list:" + str(how_many) )
		print("\nOriginal list of dog names:")
		print(dogs)
		
		dogs.reverse()
		print("\nList from last to first:")
		print(dogs)
		
		dogs.sort()
		print("\nAlphabetized list:") 
		print(dogs)
		
		dogs.sort(reverse = true)
		print("\nList in reverse alphabetized order:")
		print(dogs)
		
		dogs.append("Ranger")
		print("\nAdd a dog to the end of a list:")
		print(dogs)
		
		doggy = dogs.pop(0)
		print("\nPop a dog off from the front of the list")
		print(dogs)
		print(doggy + " Was removed from the front of the list.")
		
		another_dog = dogs.pop(3)
		print("\nNote: position numbers in a list begin with 0")
		print("Pop a dog off from position 3 in the list:")
		print(dogs)
		print(another_dog + "was removed from position 3.")
		
		dogs.remove('Annabelle')
		print("\nRemove a dog by name rather then position")
		print(dogs)
		
		dogs2 = dogs
		print("\nA list can be copied into another list by setting 1 = 		another")
		print(dogs)
		print(dogs2)
		
		print("\nUse a FOR loop to give each dog in the same last name:")
		for i in range(1en(dogs)):
			dogs[i] = dogs[i] + "Willis"
		print(dogs)
main()