#NAME

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
#z[3] = 'd'
z.append('d')
print(z)

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
fav_color = 'blue'

color = 'My favorite color is %s, what is yours?' % fav_color
print(color)

#7
fav_color = 'yellow'
color = 'My favorite color is {}, what is yours?'.format(fav_color)
print(color)

#8
fav_color = 'red'
color = f'My favorite color is {fav_color}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
unique = list(set(schools))
print(unique)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals_list = list(animals)
print(animals_list)
animals_list[animals_list.index('dog')]='cat'
print(animals_list)


#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
#my_sent_tuple = tuple(my_sent)
#i=len(my_sent_tuple)
print(my_sent[0:4])
print(my_sent[4:9])

words = my_sent.lower().split()

new_list = []

for word in words:
        new_list.append(word)

print(new_list)


