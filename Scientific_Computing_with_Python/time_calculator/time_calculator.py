def add_time(start, duration, day=None):

    DAYS = [
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
        ]
    PREFIX = ['AM', 'PM']

    # modify the input from string to time (int) and prefix 'am / pm' (str)
    time, prefix = start.split()
    start_prefix = prefix

    start_h, start_min = time.split(':')
    duration_h, duration_min = duration.split(':')

    # caluculte new hours and minutes
    new_h = int(start_h) + int(duration_h)
    new_min = int(start_min) + int(duration_min)

    days_later = 0
    prefix_later = 0

    # check if min > 59
    while new_min > 59:
        new_min -= 60
        new_h += 1

    # to fix 00:04 am
    temp_h = new_h
    while new_h > 12:
        new_h -= 12

    # check if h > 11
    while temp_h > 11:
        temp_h -= 12
        prefix = 'PM' if prefix == 'AM' else 'AM'
        prefix_later += 1

    # get new prefix
    if prefix_later % 2 != 0:
        if start_prefix == 'PM':
            prefix_later += 1
        else:
            prefix_later -= 1

    # get days later
    days_later = prefix_later / 2

    # assemble new time
    new_time = f'{new_h}:{str(new_min).zfill(2)} {prefix}'

    # if days is specified, compute the new day
    if day:
        index_days = DAYS.index(day.title())
        new_index_days = int((index_days + days_later) % 7)
        new_time += f', {DAYS[new_index_days]}'

    # if only one day passes
    if days_later == 1:
        new_time += ' (next day)'

    # if more passed
    if days_later > 1:
        new_time += f' ({int(days_later)} days later)'

    return new_time