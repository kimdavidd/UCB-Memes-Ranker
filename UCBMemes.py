import csv
import time
import variables
from_date = input('From what date (YYYY-MM-DD)?: ')
to_date = input('To what date (YYYY-MM-DD)?: ')
num_memes = input('How many hot memes do you want to see? ')
variables.from_date = from_date
variables.to_date = to_date
import get_fb_posts_fb_group
import webbrowser


with open('1717731545171536_facebook_statuses.csv') as csvfile:
    memes = csv.reader(csvfile)
    sorted_by_reacts = sorted(memes, key=lambda row: int(row[7]), reverse=True)

    from_converted_day = time.strptime(from_date, "%Y-%m-%d")
    to_converted_day = time.strptime(to_date, "%Y-%m-%d")

    i = 0
    curr = 0
    so_far = 0
    while i < int(num_memes) and curr < len(sorted_by_reacts):
        date = sorted_by_reacts[curr][6]
        year = date[:4]
        if date[6] == '-':
            month = date[5]
            if len(date) == 8:
                day = date[7]
            else:
                day = date[7:9]
        else:
            month = date[5:7]
            if len(date) == 9:
                day = date[8]
            else:
                day = date[8:10]
        trunc_date = year + "-" + month + "-" + day
        converted_day = time.strptime(trunc_date, "%Y-%m-%d")
        if from_converted_day <= converted_day and to_converted_day >= converted_day:
            webbrowser.open(sorted_by_reacts[curr][5])
            i += 1
            so_far = i
            if i == int(num_memes):
                quit()
        curr += 1
    for i in range(int(num_memes) - so_far):
        if i < len(sorted_by_reacts):
            webbrowser.open(sorted_by_reacts[i][5])
