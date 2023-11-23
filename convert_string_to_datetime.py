date = "oct 14 1997 7:15 AM"
print (type(date))
date_time = datetime. strptime(date, "%b %d %Y %I: %M%p")
print (date_time)
print (time (date_time))