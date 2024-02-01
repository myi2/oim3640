import time

# Get the current time in seconds since the epoch (January 1, 1970)
current_time = time.time()

days_since_epoch = int(current_time / (24 * 60 * 60))

current_hours = int((current_time % (24 * 60 * 60)) / 3600)
current_minutes = int((current_time % 3600) / 60)
current_seconds = int(current_time % 60)

print("Current Time: " + str(current_hours) + " hours, " + str(current_minutes) + " minutes, " + str(current_seconds) + " seconds")
print("Days since epoch: " + str(days_since_epoch))
