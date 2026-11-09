import csv
import pprint

def show(title, x):
    print("\n" * 2 + "-" * 25)
    print(title)
    print("-"*25)
    pprint.pprint(x[0:3])
    print("...")
    print("-"*25)

with open("jazz_greats_3.txt", newline="", encoding="utf-8-sig") as file:
    jazz_greats = list(csv.DictReader(file, delimiter='|'))
show("Jazz greats", jazz_greats[0:2])

non_us = [great for great in jazz_greats if great["country_of_birth"] != "US"]
show("non us", non_us)

born_after_1920 = [great for great in jazz_greats if int(great["birthdate"][-4:]) >= 1920]
show("born after", born_after_1920)

def not_us(great:dict) -> bool:
    return great["country_of_birth"] != "US"

a = [great for great in jazz_greats if not_us(great)]
show("fancy", a)

def born_later(great:dict) -> bool:
    return int(great["birthdate"][-4:]) >= 1920

b = [great for great in jazz_greats if born_later(great)]
show("fancier", b)

c = [great for great in jazz_greats if born_later(great) and not_us(great)]
show("not in us, born late", c)

d = [great for great in jazz_greats if not born_later(great) and not not_us(great)]
show("born in us, early", d)

e = list(filter(not_us, jazz_greats))
pprint.pprint(e)

f = list(filter(born_later, jazz_greats))
pprint.pprint(f)

print("-"*35)

# def born_later_not_us(great) -> bool:
#     return not_us(great) and born_later(great) 

born_later_not_us = lambda great: not_us(great) and born_later(great) 

g = list(filter(born_later_not_us, jazz_greats))
pprint.pprint(g)

h = list(filter(lambda great: not_us(great) and born_later(great), jazz_greats))
pprint.pprint(h)

def build_compound_predicate(functions):
    def predicate(great):
        for f in functions:
            if not f(great):
                return False
        return True
    return predicate

predicate = build_compound_predicate([not_us, born_later])

i = list(filter(predicate, jazz_greats))
pprint.pprint(i)

print("-" * 35)
pprint.pprint(sorted(jazz_greats, key=lambda x: x['name']))

print("-" * 35)
pprint.pprint(sorted(jazz_greats, key=lambda x: x['name'].split()[-1]))

print("-" * 35)
pprint.pprint(sorted(jazz_greats, key=lambda x: x['birthdate'][-4:]))

mapped_stuff = list(map(len, ['Jim', 'Jules', 'Carolyn', 'Ruby']))
print(mapped_stuff)

names = ['Jim', 'Jules', 'Carolyn', 'Ruby']

mapped_stuff = [len(name) for name in names]
print(mapped_stuff)

from functools import reduce
nums = [1,2,3,4,5]
print(reduce(lambda accumulated,new: accumulated*new, nums))
print(reduce(lambda accumulated,new: accumulated+new, nums))


def sum_of_squares_even_nums(numbers) ->int:
    even_numbers = filter(lambda number: number % 2 == 0, numbers)

    squares = map(lambda even: even ** 2, even_numbers)

    sum_squares = reduce(lambda accumulated,new: accumulated+new, squares)

    return sum_squares

print(sum_of_squares_even_nums([1,2,3,4,5,6]))