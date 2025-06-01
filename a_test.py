from divisors import divide
import csv

def func(x):
    return x + 2

def test_answer():
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

    assert divide(4) == 3


def test_answer2():
    assert divide(4) == 2
