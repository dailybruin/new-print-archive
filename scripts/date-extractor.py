import Levenshtein

lev_ratio_threshold = 0.8

weekday_list = []
month_list = []
day_list = []
year_list = []

# First line of ./date-strings.csv should contain weekday strings, the second line should contain month strings, etc.
with open("date-strings.csv", "r") as file:
    weekday_line = file.readline()
    if (weekday_line == ""):
        print "Error: need 4 lines in file ./date-strings.csv"
        exit()
    month_line = file.readline()
    if (month_line == ""):
        print "Error: need 4 lines in file ./date-strings.csv"
        exit()
    day_line = file.readline()
    if (day_line == ""):
        print "Error: need 4 lines in file ./date-strings.csv"
        exit()
    year_line = file.readline()
    if (year_line == ""):
        print "Error: need 4 lines in file ./date-strings.csv"
        exit()

    weekday_list = weekday_line.split(",")
    month_list = month_line.split(",")
    day_list = day_line.split(",")
    year_list = year_line.split(",")

header_tokens = raw_input().lower().replace(',', '').split(" ")
date_checklist = { 'weekday': "", 'month': "", 'day': "", 'year': ""  }

for i, token in enumerate(header_tokens):
    for weekday in weekday_list:
        if Levenshtein.ratio(token, weekday) >= lev_ratio_threshold:
            date_checklist['weekday'] = weekday
            date_index = i + 1

            if date_index < len(header_tokens):
                for month in month_list:
                    if Levenshtein.ratio(header_tokens[date_index], month) >= lev_ratio_threshold:
                        date_checklist['month'] = month
                        date_index = date_index + 1
                        break

            if date_index < len(header_tokens):
                for day in day_list:
                    if Levenshtein.ratio(header_tokens[date_index], day) >= lev_ratio_threshold:
                        date_checklist['day'] = day
                        date_index = date_index + 1
                        break

            if date_index < len(header_tokens):
                for year in year_list:
                    if Levenshtein.ratio(header_tokens[date_index], year) >= lev_ratio_threshold:
                        date_checklist['year'] = year
                        date_index = date_index + 1
                        break

            if date_checklist['month'] != "" and (date_checklist['year'] != "" or date_checklist['day'] != ""):
                print date_checklist['weekday'] + " " + date_checklist['month'] + " " + date_checklist['day'] + " " + date_checklist['year']
                exit()
            else:
                date_checklist = {'weekday': "", 'month': "", 'day': "", 'year': ""}

for i, token in enumerate(header_tokens):
    for month in month_list:
        if Levenshtein.ratio(token, month) >= lev_ratio_threshold:
            date_checklist['month'] = month
            date_index = i + 1

            if date_index < len(header_tokens):
                for day in day_list:
                    if Levenshtein.ratio(header_tokens[date_index], day) >= lev_ratio_threshold:
                        date_checklist['day'] = day
                        date_index = date_index + 1
                        break

            if date_index < len(header_tokens):
                for year in year_list:
                    if Levenshtein.ratio(header_tokens[date_index], year) >= lev_ratio_threshold:
                        date_checklist['year'] = year
                        date_index = date_index + 1
                        break

            if date_index < len(header_tokens):
                for weekday in weekday_list:
                    if Levenshtein.ratio(header_tokens[date_index], weekday) >= lev_ratio_threshold:
                        date_checklist['weekday'] = weekday
                        date_index = date_index + 1
                        break

            if date_checklist['month'] != "" and (date_checklist['year'] != "" or date_checklist['day'] != ""):
                print date_checklist['weekday'] + " " + date_checklist['month'] + " " + date_checklist['day'] + " " + date_checklist['year']
                exit()
            else:
                date_checklist = {'weekday': "", 'month': "", 'day': "", 'year': ""}

for i, token in enumerate(header_tokens):
    for month in month_list:
        if Levenshtein.ratio(token, month) >= lev_ratio_threshold:
            date_checklist['month'] = month
            date_index = i + 1

            if date_index < len(header_tokens):
                for day in day_list:
                    if Levenshtein.ratio(header_tokens[date_index], day) >= lev_ratio_threshold:
                        date_checklist['day'] = day
                        date_index = date_index + 1
                        break

            if date_index < len(header_tokens):
                for year in year_list:
                    if Levenshtein.ratio(header_tokens[date_index], year) >= lev_ratio_threshold:
                        date_checklist['year'] = year
                        date_index = date_index + 1
                        break

            if date_index < len(header_tokens):
                for weekday in weekday_list:
                    if Levenshtein.ratio(header_tokens[date_index], weekday) >= lev_ratio_threshold:
                        date_checklist['weekday'] = weekday
                        date_index = date_index + 1
                        break

            if date_checklist['month'] != "" and (date_checklist['year'] != "" or date_checklist['day'] != ""):
                print date_checklist['weekday'] + " " + date_checklist['month'] + " " + date_checklist['day'] + " " + date_checklist['year']
                exit()
            else:
                date_checklist = {'weekday': "", 'month': "", 'day': "", 'year': ""}
