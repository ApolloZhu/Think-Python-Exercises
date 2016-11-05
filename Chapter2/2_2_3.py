# in seconds
interval_at_ease = 8 * 60 + 15 
interval_at_tempo = 7 * 60 + 12

seconds_passed = interval_at_ease + interval_at_tempo * 3 + interval_at_ease
minutes_passed = int(seconds_passed / 60)

now_minute = (52 + minutes_passed) % 60
now_hour = int(6 + (52 + minutes_passed) / 60)
print(str(now_hour)+":"+str(now_minute)) # real: 07:30:06
