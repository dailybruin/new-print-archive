import Levenshtein

LEV_RATIO_THRESHOLD = 0.8
TOKEN_FILE_PATH = "date-tokens.csv"

def extract_date(header_tokens, token_file_path):
    global weekday_list
    global month_list
    global day_list
    global year_list

    # First line of ./date-tokens.csv should contain weekday tokens, the second line should contain month tokens, etc.
    with open("date-tokens.csv", "r") as file:
        weekday_line = file.readline()
        month_line = file.readline()
        day_line = file.readline()
        year_line = file.readline()
        if (weekday_line == "" or month_line == "" or day_line == "" or year_line == ""):
            print "Error: need lines in file ./date-tokens.csv with tokens for weekdays, months, days, years in that order"
            return
        weekday_list = weekday_line.split(",")
        month_list = month_line.split(",")
        day_list = day_line.split(",")
        year_list = year_line.split(",")

    date_checklist = { 'weekday': "", 'month': "", 'day': "", 'year': ""  }

    for i, token in enumerate(header_tokens):
        for weekday in weekday_list:
            if Levenshtein.ratio(token, weekday) >= LEV_RATIO_THRESHOLD:
                date_checklist['weekday'] = weekday
                date_index = i + 1

                if date_index < len(header_tokens):
                    for month in month_list:
                        if Levenshtein.ratio(header_tokens[date_index], month) >= LEV_RATIO_THRESHOLD:
                            date_checklist['month'] = month
                            date_index = date_index + 1
                            break

                if date_index < len(header_tokens):
                    for day in day_list:
                        if Levenshtein.ratio(header_tokens[date_index], day) >= LEV_RATIO_THRESHOLD:
                            date_checklist['day'] = day
                            date_index = date_index + 1
                            break

                if date_index < len(header_tokens):
                    for year in year_list:
                        if Levenshtein.ratio(header_tokens[date_index], year) >= LEV_RATIO_THRESHOLD:
                            date_checklist['year'] = year
                            break

                if date_checklist['month'] != "" and (date_checklist['year'] != "" or date_checklist['day'] != ""):
                    return date_checklist['weekday'] + " " + date_checklist['month'] + " " + date_checklist['day'] + " " + date_checklist['year']
                else:
                    date_checklist = {'weekday': "", 'month': "", 'day': "", 'year': ""}

    for i, token in enumerate(header_tokens):
        for month in month_list:
            if Levenshtein.ratio(token, month) >= LEV_RATIO_THRESHOLD:
                date_checklist['month'] = month
                date_index = i + 1

                if date_index < len(header_tokens):
                    for day in day_list:
                        if Levenshtein.ratio(header_tokens[date_index], day) >= LEV_RATIO_THRESHOLD:
                            date_checklist['day'] = day
                            date_index = date_index + 1
                            break

                if date_index < len(header_tokens):
                    for year in year_list:
                        if Levenshtein.ratio(header_tokens[date_index], year) >= LEV_RATIO_THRESHOLD:
                            date_checklist['year'] = year
                            date_index = date_index + 1
                            break

                if date_index < len(header_tokens):
                    for weekday in weekday_list:
                        if Levenshtein.ratio(header_tokens[date_index], weekday) >= LEV_RATIO_THRESHOLD:
                            date_checklist['weekday'] = weekday
                            break

                if date_checklist['month'] != "" and (date_checklist['year'] != "" or date_checklist['day'] != ""):
                    return date_checklist['weekday'] + " " + date_checklist['month'] + " " + date_checklist['day'] + " " + date_checklist['year']
                else:
                    date_checklist = {'weekday': "", 'month': "", 'day': "", 'year': ""}

    for i, token in enumerate(header_tokens):
        for month in month_list:
            if Levenshtein.ratio(token, month) >= LEV_RATIO_THRESHOLD:
                date_checklist['month'] = month
                date_index = i + 1

                if date_index < len(header_tokens):
                    for day in day_list:
                        if Levenshtein.ratio(header_tokens[date_index], day) >= LEV_RATIO_THRESHOLD:
                            date_checklist['day'] = day
                            date_index = date_index + 1
                            break

                if date_index < len(header_tokens):
                    for year in year_list:
                        if Levenshtein.ratio(header_tokens[date_index], year) >= LEV_RATIO_THRESHOLD:
                            date_checklist['year'] = year
                            date_index = date_index + 1
                            break

                if date_index < len(header_tokens):
                    for weekday in weekday_list:
                        if Levenshtein.ratio(header_tokens[date_index], weekday) >= LEV_RATIO_THRESHOLD:
                            date_checklist['weekday'] = weekday
                            break

                if date_checklist['month'] != "" and (date_checklist['year'] != "" or date_checklist['day'] != ""):
                    return date_checklist['weekday'] + " " + date_checklist['month'] + " " + date_checklist['day'] + " " + date_checklist['year']
                else:
                    date_checklist = {'weekday': "", 'month': "", 'day': "", 'year': ""}

if __name__ == "__main__":
    print extract_date(raw_input().lower().replace(',', '').split(" "), TOKEN_FILE_PATH)