# Dumda
Python Library to get fast extensive Dummy Data for testing https://pypi.org/project/dumda/
## Installation
```
pip install dumda
```

## Usage:

### Cities

```python
from dumda import cities

# get a single random city, either from the
# entire pool or from a specific country
print(cities.get_random_city())
print(cities.get_random_city("United States"))

# get a list of random cities, this can also be
# called with a given country (cities.get_random_cities(5, "Zimbabwe")
print(cities.get_random_cities(10))
```
#### output
```bash
Somerset East
Paducah
['Watsa', 'Westerstede', 'Porto-Novo', 'Dushanbe', 
'Hoeyang', 'Uozu', 'Riyadh', 'Lashio', 'Arendal', 
'Tlapa de Comonfort']
``` 

### Names
the meta is pretty much the same with names and cities, except a few
additional operations
```python
from dumda import names
# get a random name
print(names.get_random_name())
# instead of specific countries, you can pass specific sex
print(names.get_random_name("boy"))
print()
# like, cities get a random list
b = names.get_random_names(15, "boy")
g = names.get_random_names(15, "girl")
the_class = b + g
print("class list: {}".format(the_class))

print()
# additional query options
# generate a full name, for more accurate dummy data
print(names.get_full_name())

# there is also a multiple version of the function, 
# and of course you can enter a sex
print(names.get_full_names(5))
print(names.get_full_name("boy"))
print(names.get_full_names(3, "girl"))

print()
# I added this just because, but you can also 
# get a list of names based on letter
good_names = names.get_names_by_letter("o", 3)
print(good_names)
print(good_names[-1])
```
#### output
```bash
Armando
Andre

class list: ['Lupe', 'Wilbert', 'Torrence', 'Shad', 'Kyson', 
'Keaton', 'Destin', 'Ridge', 'Jorden', 'Enzo', 'Reginal', 
'Aarav', 'Deontae', 'Reggie', 'Kameron', 'Anya', 'Therese', 
'Kaylee', 'Linette', 'Greta', 'Allie', 'Deanne', 'Coretta', 
'Nila', 'Jazlyn', 'Lolita', 'Cherry', 'Clare', 'Breanne', 'Cheri']

Davian Yung
['Glynda Zavala', 'Unknown Booth', 'Leigh Flood', 'Ben Dupree', 
'Adrien Zachary']
Kimberly Higgins
['Jocelyn Zelaya', 'Kalene Ross', 'Melba Tran']

['Oscar', 'Otis', 'Oliver']
Oliver
```

### Phone Numbers
In cases that you are making something like a phonebook or directory, you can also generate phone numbers (that follow U.S. formatting).
You can optionally pass an area code if you want to generate phones for people from a specific area.
```python
from dumda.phones import generate_number
# generate a random phone number based on US standard
print(generate_number())
# generate based on a given area code
print(generate_number("202"))
```
#### output:
```bash
901-212-2734
202-741-8998
```
### Emails
Using this package's name class you can also generate random emails
```python
from dumda.names import get_full_name
from dumda.emails import generate_email
# Pass a full name to generate an email
y = get_full_name()
x = generate_email(y)
print(y)
print(x)
z = get_full_name()
print(z)
print(generate_email(z))
```

##### output:
```bash
Armando Charles
acharles@foo.org
Virgie Innocent
virgieinnocent@qux.net
```

### Person Object
Now if you were thinking of combining these for some objects
in your program and wanted to keep it simple, I've got it covered.
```python
from dumda import Person
person_one = Person()
# optionally pass sex and country of person
person_two = Person(country="United Kingdom", sex="girl")
print(person_one.json())
print(person_two.json())

```

##### output:
```bash
{'full_name': 'Armando Charles', 'location': 'Fairhope', 'email': 'acharles@baz.net', 'phone': '763-859-7018'}
{'full_name': 'Kinsley Louis', 'location': 'Weybridge', 'email': 'kinsleyl@qux.com', 'phone': '623-88-6788'}
```
