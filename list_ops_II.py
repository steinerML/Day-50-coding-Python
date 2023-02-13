#Dictionary Operations start: 11:30

provincies = ['Drenthe', 'Friesland', 'Gelderland', 'Gelderland', 'Limburg', 'Noord-Brabant', 'Overijssel', 'Utrecht', 'Zeeland', 'Zuid-Holland']

#Length of element 'Zuid-Holland'
print(len(provincies[-1]))

#Insert 'Flevoland' at the right place respecting the alphabetical order
print(provincies.insert(1,'Flevoland'))
print(provincies)

#Make a new list called 'selectie'with the last 6 elements of a
#list of unknown length.
gementee = []
selectie = gementee[-6:]

#Referentieblad methods.

#Count number of times an element appears.
print(provincies.count('Utrecht'))

#Insert element at a given index.
print(provincies.insert(0,'Rusia'))
print(provincies)

#Append, add element at the end of the list.
print(provincies.append('Vietnam'))
print(provincies)

#Index, returns the first occurrence of an element (index)
print(provincies.index('Gelderland'))

#Remove, removes the first occurrence of an element
provincies.remove('Utrecht')
print(provincies)

#Reverse, reverses the elements in the list.
provincies.reverse()
print(provincies)

#Sort, sorts the elements of the list in ascending order.
provincies.sort()
print(provincies)

#Sorted (function), returns a sorted list (alphabetically)
print(sorted(provincies))

#Zip two lists together and sort them alphabetically.
countries = ['Japan', 'Kenya', 'India', 'Turkey', 'Iran', 'North Korea', 'Liechtenstein', 'Brazil']
# grade = ['a','c','b','h','e','f','g','z','i']
grade = [8,2,3,4,5,6,7,1]
new_list = list(zip(grade,countries))
print(new_list)

new_list = sorted(list(zip(grade,countries)))
print(new_list)

#List comprehension
comp_list = [i**3 for i in (1,2,3)]
print(comp_list)

#Difference between 2 lists.
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

#We convert to sets.
set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)
