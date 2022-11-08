def add_time(start, duration, starting_day=""):
    # split time
    pieces = start.split()
    time = pieces[0].split(":")
    end = pieces[1]
    # print(time,end)
    # Calculate 24-hour clock format
    if end == "PM":
        hour = int(time[0]) + 12
        time[0] = str(hour)
        # print(time)
        # split duration
    dur_time = duration.split(":")
    # print(dur_time)
    #  find new hour and minutes
    new_hour = int(time[0]) + int(dur_time[0])
    new_minutes = int(time[1]) + int(dur_time[1])
    # print(new_hour,new_minutes)

    if new_minutes >= 60:
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    # print(new_hour,new_minutes)

    add_day = 0
    if new_hour > 24:
        add_day = new_hour // 24
        new_hour -= add_day * 24

    if new_hour > 0 and new_hour < 12:
        end = "AM"
    elif new_hour == 12:
        end = "PM"
    elif new_hour > 12:
        end = "PM"
        new_hour -= 12
    else:
        end = "AM"
        new_hour += 12
    # print(new_hour,new_minutes)

    if add_day > 0:
        if add_day == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(add_day) + " days later)"
    else:
        days_later = ""

    weekdays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")
    if starting_day:
        weeks = add_day // 7
        item = weekdays.index(
            starting_day.lower().capitalize())+(add_day - 7 * weeks)
        if item > 6:
            item -= 7
        day = ", " + weekdays[item]
    else:
        day = ""
        #  AM AND PM print(new_time)
    new_time = str(new_hour) + ":" + \
        (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + \
        " " + end + day + days_later

    return new_time


print(add_time("2:59 AM", "24:00"))
