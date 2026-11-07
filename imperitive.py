import pprint

def show(title, x):
    print("\n" * 2 + "-" * 25)
    print(title)
    print("-"*25)
    pprint.pprint(x[0:3])
    print("...")
    print("-"*25)


with open("jazz_greats_3.txt") as file:
    jazz_greats_nl = file.readlines()
jazz_greats = [great.rstrip("\n") for great in jazz_greats_nl]

show("raw jazz greats", jazz_greats[0:2])

def non_us_jazz_greats(x):
    non_us = []
    for i in x:
        if "US" not in i:
            non_us.append(i)
    return non_us

show("non_us_jazz_greats", non_us_jazz_greats(jazz_greats))

jazz_greats_split = [great.split(sep = "|") for great in jazz_greats[1:]]

show("jazz greats split", jazz_greats_split)

def born_in_or_after_1920(x):
    jazz_greats_1920 = []
    for great in jazz_greats_split:
        birthday = great[1]
        birth_year = birthday[-4:]
        if int(birth_year) >= 1920:
            jazz_greats_1920.append(great)
    return jazz_greats_1920

show("born in or after 1920", born_in_or_after_1920(jazz_greats_split))

names = [great[0] for great in jazz_greats_split]

show("names", names)

def alphasort(x):
    last_name_first = [great[0].split()[-1:] + great for great in x]
    sorted_last = sorted(last_name_first)
    alpha = [great[1:] for great in sorted_last]
    return alpha

show("sorted names", alphasort(jazz_greats_split))
