# Dumda
Python Library to get fast extensive Dummy Data for testing https://pypi.org/project/dumda/
## Installation
```
pip install dumda
```


## Usage:

## Cities

```python
from dumda.cities import Cities

# initialize cities class
c = Cities()

# get the full list of all available cities (23k+ cities)
c.get_all()
```

Of course, rarely or ever will someone need a list of 23 thousand cities. Not to mention the impact on speed.\
in more common cases, you can extract sample sizes of cities.

### get single
```python
from dumda.cities import Cities
c = Cities()
c.get_single()
```
#### output:
```bash
'Scicli'
```

### get a random set of cities
the most basic implementation; get a list of randomly selected cities of a chosen amount
```python
from dumda.cities import Cities
c = Cities()

c.get_random_cities(10)
```

#### output:
```bash
['Hawthorn South',
 'Paghmān',
 'Bruntál',
 'Secunda',
 'Beroun',
 'Luxu',
 'Kārkala',
 'Jelcz',
 'Al Qaryatayn',
 'Amadeo']
```
### get cities by identifiers
you can specify more on the exact cities you would like; cities by country or by letter. \
Getting a city by letter is primarily for fun, however imagine that you are making a fight application and want them to be domestic.
```python
from dumda.cities import Cities
from random import choice
c = Cities()
# Get city by letter
o_cities = c.get_by_letter("o")
print(o_cities)
print()
# Get City by country
us_cities = c.get_by_country("United States")
# Note there is no 'england' just united kingdom

class Flight:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
    
    def __repr__(self):
        return f"Flight from {self.origin} to {self.destination}"
    
    
if __name__ == '__main__':
    x = choice(us_cities)
    y = choice(us_cities)
    
    flight = Flight(x, y)
    print(flight)
```
#### output:
```bash
['Xankandi', 'Xaçmaz', 'Xique Xique', 'Xanxerê', 'Xinghua', 'Xucheng', 'Xunchang', 'Xuanzhou', 'Xixiang', 'Xiuying', 'Xiulin', 'Xiongzhou', 'Xinzhou', 'Xinzhou', 'Xinzhi', 'Xinyu', 'Xinyang', 'Xintai', 'Xinshi', 'Xinpu', 'Xinji', 'Xining', 'Xingtai', 'Xindian', 'Xindi', 'Ximei', 'Xihe', 'Xichang', 'Xiazhuang', 'Xiazhen', 'Xiashi', 'Xiaoweizhai', 'Xiaoshan', 'Xiaolingwei', 'Xiaogan', 'Xianyang', 'Xiantao', 'Xianshuigu', 'Xiannü', 'Xianning', 'Xianju', 'Xiangxiang', 'Xiangtan', 'Xiangyang', 'Xiangcheng Chengguanzhen', 'Xi’an', 'Xiamen', 'Xishan', 'Xinhui', 'Xinyi', 'Xincheng', 'Xiuyan', 'Xinqing', 'Xinmin', 'Xinglongshan', 'Xingcheng', 'Xilin Hot', 'Xifeng', 'Xiaoshi', 'Xanten', 'Xàtiva', 'Xirivella', 'Xánthi', 'Xam Nua', 'Xoxocotla', 'Xonacatlán', 'Xochitepec', 'Xochimilco', 'Xicotepec de Juárez', 'Xico', 'Xalapa de Enríquez', 'Xai-Xai', 'Xenia']

Flight from Reno to Marshalltown
```




## Names
###### Note: Names runs much slower than cities as there are 200,000 names in this package
functions overlap between the names and cities packages such as get_all, get_single, get_random and get_by_letter. \
However, there are some function unique to names.

### Get Names by Gender
you can get a list of names of a single group and optionally specify the amount
```python
from dumda.names import Names
names = Names()

# you can either leave the function call blank or
# pass an integer for the given amount. 
# Passing an integer is recommended as to remember that
# there are around 100,000 names for each sex
boys = names.boy_names(5)
girls = names.girl_names(5)

print(boys)
print(girls)
```
#### output:
```bash
['Sam', 'Erich', 'Malcolm', 'Mitchel', 'Elbert']
['Chantel', 'Aleta', 'Kari', 'Rena', 'Eve']
```

### Get Full Names
if need be, you can also get full names
```python
from dumda.names import Names
names = Names()

# get a given number of random full names
print(names.get_fullnames(5))

# get full names based off of sex
print(names.get_fullnames(5, 'boy'))
print(names.get_fullnames(5, 'girl'))
```

#### output:
```bash
['Kurt Trudell', 'Frieda Corridoni', 'Colleen Nicolo', 'Cruz Loudin', 'Orin Mcbreen']
['Noah Sharratt', 'Jerrie Skanes', 'Homer Newcomb', 'Nathaniel Cavendish', 'Sabrina Heltzel']
['Everett Tyre', 'Jeannette Trautwein', 'Theodore Slaubaugh', 'Maryanne Markos', 'Angel Norrix']
```


## Phone Numbers
In cases that you are making something like a phonebook or directory, you can also generate phone numbers (that follow U.S. formatting).
You can optionally pass an area code if you want to generate phones for people from a specific area.
```python
from dumda.phones import generate_number

# regular generation
x = generate_number()

# area code generation
dc_phones = list()
for i in range(5):
    phone = generate_number(area_code=202)
    dc_phones.append(phone)

print(x)
print(dc_phones)
```
#### output:
```bash
563-873-5164
['202-822-1231', '202-620-6058', '202-336-3025', '202-565-7063', '202-525-2625']
```
### Emails
Using this package's name class you can also generate random emails
```python
from dumda.names import Names
from dumda.emails import generate_email

names = Names()
name = names.get_fullnames(1)[0]

print(name)
# generate 5 times to show different ways it can generate
print(generate_email(name))
print(generate_email(name))
print(generate_email(name))
print(generate_email(name))
print(generate_email(name))
```

##### output:
```bash
Alison Snowden
alisons@qux.com
alisons@baz.com
asnowden@bar.net
asnowden@baz.com
alisons@baz.com
```

### Person Object
```python
from dumda import Person
person_one = Person()
person_two = Person()
print(person_one.get_json())
print(person_two.get_json())

# Alternatively you can just access values
# from the object as normal i.e. person_one.email
```

##### output:
```bash
{'full_name': 'Muhammad Santrizos', 'location': 'Universal City', 'email': 'muhammadsantrizos@baz.com', 'phone': '581-277-1989'}
{'full_name': 'Blair Lust', 'location': 'Avenel', 'email': 'blairl@qux.net', 'phone': '395-521-9731'}
```
