def add_time(start, duration, startday = None ):
    
    ''' 
    Calculates the datetime of the start date plus some time
    
    Args:
        start (str): time of day in a 12 hr format with a ':' separating
            the hours and minutes followed space and then 'AM' or 'PM'.
        duration (str): amount of time required adding with a ':' separating
            the hours and minutes.
        startday (str, optional): Day of the that the start is.
    
    Returns:
        str : formatted datetime in 12 hr format, if there is a change in date, 
            data representing the new date will be returned, if a start day was
            inputted, a day of the week will also be returned
    '''

    # Split the first variable to get access to the individual parts
    start_time_hour_min = start.split(':')
    start_time_min_am_pm = start_time_hour_min[1]
    start_time_min_am_pm_split = start_time_min_am_pm.split(' ')
    am_pm = start_time_min_am_pm_split[1]
    
    # Split the second variable to get access to the individual parts
    duration_split = duration.split(':')
    
    # Assign the individual parts
    start_time_hour = start_time_hour_min[0]
    start_time_min = start_time_min_am_pm_split[0]
    duration_hour = duration_split[0]
    duration_min = duration_split[1]

    # Convert the strings into integers
    start_time_hour_int = int(start_time_hour)
    start_time_min_int = int(start_time_min)
    duration_hours_int = int(duration_hour)
    duration_min_int = int(duration_min)

    # Calc the new min to be displayed 
    new_min = start_time_min_int + duration_min_int
    
    # Adjust the start hour if the min is larger than 60 (new hour)
    min_conv_2_hour = 0
    while new_min >= 60:
        min_conv_2_hour += 1
        new_min -= 60
  
    # Calc the new hour to be displayed 
    new_hour = start_time_hour_int + duration_hours_int + min_conv_2_hour
  
    # Adjust the day counter if the hour is larger than 24 (new day)
    # Adjust the AM/PM marker if the hour is larger than 12 (new half day)
    hour_conv_2_day = 0

    while new_hour >= 12:
        if am_pm == 'AM':
            am_pm = 'PM'
        else:
            am_pm = 'AM'
            hour_conv_2_day += 1
        new_hour -= 12

    # Adjust the hour if the hour is less than 1
    if new_hour == 0:
        new_hour += 12
        
    # Create string for day count notification
    if hour_conv_2_day > 1:
        strhour_conv_2_day = str(hour_conv_2_day)
        days = ' (' + strhour_conv_2_day + ' days later)'
    elif hour_conv_2_day == 1:
        days = ' (next day)'
    else:
        days = None
    
    # Create string for day count notification
    # Convert string weekday into int to calculate the end day
    if startday is not None:
        low_startday = startday.lower()
        day2num = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 
                   'friday': 5, 'saturday': 6, 'sunday': 7}

        daynumber = day2num[low_startday]

        # Make day adjustment if hours intially exceeded 24
        new_day_number = daynumber + hour_conv_2_day
        
        # Adjust the day number if the number is larger than 6 (new week)
        while new_day_number > 6:
            new_day_number -= 7

        # Convert the day back into human readable string
        num2day = {1: ', Monday', 2: ', Tuesday', 3: ', Wednesday', 
                   4: ', Thusday', 5: ', Friday', 6: ', Saturday', 
                   7: ', Sunday', 0: ', Sunday'}
        
        new_day = num2day[new_day_number]
    
    # Convert the hour back into string
    new_hour_str = str(new_hour)

    # Convert the minutes back into string with a spacer if required for fomat
    if new_min < 10:
        new_min_str = '0' + str(new_min)    
    else:
        new_min_str = str(new_min)

    # Adjust the AM/PM marker with a spacer for fomat
    am_pm = ' ' + am_pm
    
    # Compile the result
    new_time = new_hour_str + ':' + new_min_str + am_pm
  
    if startday is not None:
        new_time += new_day
    
    if days is not None:
        new_time += days

    return new_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))