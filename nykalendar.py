# python 3.6.5

import random as r
import urllib.request

# grab a giant list of words from some URL i found on stackoverflow answer
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
# only grab the proper nouns from the word list (not necessary)
upper_words = [word for word in words if word[0].isupper()]

day = 1 # keep track of how many days have been added so we only ad a year's worth to the calender
days = 365 # will need to be manually changed for leap years unless leap year calculation is implemented
months = []
while days > 0:
    no_weeks = r.randint(1,5) # pick a random number of weeks (1-5) for each month
    weeks = []
    for i in range(no_weeks):
        week = r.randint(1,5) # pick a random number of days (1-5) for each week
        # if the last week of the year ends up being too long (giving us more than 365 days),
        # then instead make the last week the correct number of days long
        if (days - week) <= 0:
            week = days
        weeks.append(week)
        days -= week
    months.append(weeks)

filename = "nykalendar.txt"
# remove 'file=text_file' to print to stdout instead
with open(filename, "w") as text_file:
    print('no. of months: {}\n=================\n'.format(len(months)), file=text_file)
    for m in range(len(months)):
        print('{}: '.format(m + 1) + r.choice(upper_words) + r.choice(['ary', 'y', 'ber', 'ober']), file=text_file)
        for w in range(len(months[m])):
            for i in range(months[m][w]):
                print('[ {} ]'.format(day), end=' ', file=text_file) # draw a box with a number in it for each day
                day += 1
            print('\n', file=text_file)
