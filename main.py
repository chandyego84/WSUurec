# Controlling the UREC Chinook Student Center browser with Selenium Module
# Automate UREC reservations each weekday
from datetime import date

today = date.today().weekday()
reserve_days = '12345'
reserve_days_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday"}

if str(today) in reserve_days:
    from reserveClasses import ReservationBot
    test = ReservationBot("https://www.chinook.wsu.edu/reservations/chinook-lower-weight-room-basement-room-40-50/",
                         "NETWORKID", "PASSWORD")   
    if today == 2:
        test.sign_waivers('Tuesday', today-1, 27)
    else:
        for day_number, day in reserve_days_dict.items():
            if today == day_number:
                test.sign_waivers(f'{reserve_days_dict[day_number-1]}', today+1, 7)
