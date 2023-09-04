import datetime
import pytz

current_time = datetime.datetime.now()

formatted_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_current_time)
print("")

# Get the current UTC time
current_utc_time = datetime.datetime.utcnow()
tz_hr_difference = current_utc_time.utcoffset().total_seconds // 3600

# Get a list of all the timezones
all_timezones = pytz.all_timezones


for timezone in all_timezones:
    tz = pytz.timezone(timezone)
    print(tz)
    # print(current_utc_time.astimezone(tz).utcoffset())
    
    local_time = current_utc_time.replace(tzinfo=pytz.utc).astimezone(tz)
    local_time_hr_diff = local_time.utcoffset().total_seconds() // 3600
    print("local_time : ",local_time," == current_time : ",current_utc_time.astimezone())
    print(local_time.utcoffset().total_seconds() // 3600)
    
    if local_time == current_utc_time:
        print("current timezone : ", timezone)
        break
    