# zones_of_nepal = ["Mechi", "Koshi", "Sagarmatha", "Janakpur", "Bagmati", "Narayani", "Gandaki", "Lumbini", "Dhaulagiri", "Rapti", "Karnali", "Bheri", "Seti", "Mahakali"]

# print(zones_of_nepal[6])

# print(zones_of_nepal[9])

# print(zones_of_nepal[-1])

# print(zones_of_nepal[-2])

# # if I want to change the list item Mechi to Meechi, then write below code

# zones_of_nepal[0] = "Meechi"

# print(zones_of_nepal[0])

# # if I want to change the list item Janakpur to Jankpur, then write below code

# zones_of_nepal[3] = "Jankpur"

# print(zones_of_nepal[3])

# # if I want to change the list item Lumbini to Lumbin, then write below code
# print(zones_of_nepal)

# zones_of_nepal.append("New Karnali")

# print(zones_of_nepal)

# zones_of_nepal = ["Mechi", "Koshi", "Sagarmatha", "Janakpur", "Bagmati", "Narayani", "Gandaki", "Lumbini", "Dhaulagiri", "Rapti", "Karnali", "Bheri", "Seti", "Mahakali"]

# Inserting "Terai" at index 5
# zones_of_nepal.insert(5, "Terai")

# # Inserting "Himal" at index 3
# zones_of_nepal.insert(3, "Himal")

# # Inserting "New Zone" at index 8
# zones_of_nepal.insert(8, "New Zone")

# # print(zones_of_nepal)

# # formatted_zones = ', '.join(['"' + zone + '"' for zone in zones_of_nepal])

# print(zones_of_nepal)


# zones_of_nepal.extend(["Ramesh","Rawat"])
# zones_of_nepal.insert(0,"Ramesh")
# zones_of_nepal.remove("Ramesh")
# zones_of_nepal.pop(2)
# zones_of_nepal.clear()
# print(zones_of_nepal)




fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting at position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'

print(fruits)