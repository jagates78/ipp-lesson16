import pprint
with open("jazz_greats_3.txt") as file:
    jazz_greats_nl = file.readlines()
jazz_greats = [great.rstrip("\n") for great in jazz_greats_nl]
pprint.pprint(jazz_greats[0:2], width = 100)
print("-"*25)
def non_us_jazz_greats(x):
    non_us = []
    for i in x:
        if "US" not in i:
            non_us.append(i)
    return non_us
pprint.pprint(non_us_jazz_greats(jazz_greats))
jazz_greats_split = [great.split(sep = "|") for great in jazz_greats[1:]]
print("-"*25)
pprint.pprint(jazz_greats_split[0:3])
def born_in_or_after_1920(x):
    jazz_greats_1920 = []
    for great in jazz_greats_split:
        birthday = great[1]
        birth_year = birthday[-4:]
        if int(birth_year) >= 1920:
            jazz_greats_1920.append(great)
    return jazz_greats_1920
pprint.pprint(born_in_or_after_1920(jazz_greats_split))