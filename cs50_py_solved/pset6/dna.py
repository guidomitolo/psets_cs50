from sys import argv, exit
import csv

if len(argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    exit(1)

STRs = {}
with open(argv[2], 'r') as sequence:
    string = sequence.readline()

    # str1 = 'AGATC'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('AGATC',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('AGATC',i+len('AGATC')):
            count = 0
    STRs['AGATC'] = bigger

    # str2 = 'TTTTTTCT'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('TTTTTTCT',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('TTTTTTCT',i+len('TTTTTTCT')):
            count = 0
    STRs['TTTTTTCT'] = bigger

    # str3 = 'AATG'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('AATG',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('AATG',i+len('AATG')):
            count = 0
    STRs['AATG'] = bigger

    # str4 = 'TCTAG'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('TCTAG',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('TCTAG',i+len('TCTAG')):
            count = 0
    STRs['TCTAG'] = bigger

    # str5 = 'GATA'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('GATA',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('GATA',i+len('GATA')):
            count = 0
    STRs['GATA'] = bigger

    # str6 = 'TATC'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('TATC',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('TATC',i+len('TATC')):
            count = 0
    STRs['TATC'] = bigger

    # str7 = 'GAAA'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('GAAA',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('GAAA',i+len('GAAA')):
            count = 0
    STRs['GAAA'] = bigger

    # str8 = 'TCTG'
    count = 0
    bigger = 0
    for i in range(len(string)):
        if string.startswith('TCTG',i):
            count +=1
            if count > bigger:
                bigger = count
        elif string.startswith('TCTG',i+len('TCTG')):
            count = 0
    STRs['TCTG'] = bigger

ranking = {}
with open(argv[1], 'r') as file:
    database = csv.DictReader(file)

    for dictionary in database:
        matches = 0
        for key, value in dictionary.items():
            if key == 'name':
                continue
            else:
                if int(value) in STRs.values():
                    matches+=1
            ranking[dictionary['name']] = matches

for key, value in ranking.items():
    if value == len(dictionary.values())-1:
        print(key)
        exit(0)
print('No match')
exit(1)