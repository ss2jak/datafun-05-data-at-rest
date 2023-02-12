#9.3.1 Writing to a Text File:Intro the with Statement

with open('accounts.txt' , mode='w') as accounts: 
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')
print()

#9.3.2 Reading Data from a Text File

with open ('accounts.txt' , mode='r') as accounts_file:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in accounts_file:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:>10}')
print()

#9.4 Updating Text Files
accounts = open('accounts.txt', 'r')

temp_file = open('temp_file.txt', 'w')

with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if account != '300':
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'Williams', balance])
            temp_file.write(new_record + '\n')
print()

import os

os.remove ('accounts.txt')

os.rename('temp_file.txt', 'accounts.txt')

#9.5 Serialization with JSON

accounts_dict = {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

import json

with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)
print()

##deserialization JSON text

with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)
print()

accounts_json
accounts_json['accounts']
accounts_json['accounts'][0]
print()

accounts_json['accounts'][1]
print()

##displaying the JSON text

with open('accounts.json', 'r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))
print()

#9.9 finally clause

try:
    print('try suite with no exceptions raised')
except:
    print('this will not execute')
else:
    print('else executes because no exceptions in the try suite') 
finally:
    print('finally always executes')

try:
    print('try suite that raises an exception')
    int('hello')
    print('this will not execute')
except ValueError:
    print('a ValueError occurred')
else:
   print('else will not execute because an exception occurred')
finally:
   print('finally always executes')
print()

#9.12.1 Python Standard Library Module csv
import csv

with open ('accounts.csv', mode='w', newline='') as accounts:
    writer = csv.writer(accounts)
    writer.writerow([100, 'Jones', 24.98])
    writer.writerow([200, 'Doe', 345.67])
    writer.writerow([300, 'White', 0.00])
    writer.writerow([400, 'Stone', -24.16])
    writer.writerow([500, 'Rich', 224.62])

print()

#Reading from a CSV file
print('Reading from a CSV file')

with open ('accounts.csv', 'r', newline='') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    reader = csv.reader(accounts)
    for record in reader:
         account, name, balance = record
         print(f'{account:<10}{name:<10}{balance:>10}')

#9.12.2 Reading CSV Files into Pandas DataFrames

import pandas as pd
df = pd.read_csv('accounts.csv',
                names=['account', 'name', 'balance'])
df.to_csv('accounts_from_dataframe.csv', index=False)

#9.12.3 Rading into Titanic Disaster Dataset
import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 'Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('display.precision', 2) #'precision' outputs error
titanic.head()
titanic.tail()

#9.12.4 Simple Data ANalysis with the Titatic Disaster Dataset

titanic.describe()

(titanic.survived == 'yes').describe()

#9.12.5 Passenger Age Histogram 
#pip install matplotlib(if not already active us this)

%matplotlib
histogram = titanic.hist()