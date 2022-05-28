from menu import *
def add(name, surname, number, comment):
    with open('log.csv', 'a') as logfile:
        logfile.write(f'{surname} {name} {number} {comment}' + '\n')

def Print():
    with open('log.csv', 'r') as logfile:
        s = logfile.readlines()
        print(s)
