import pyexcel as pe
import datetime

new_records = pe.get_records(file_name="jobs.xlsx")
old_records = pe.get_records(file_name="archive/jobs-121616.xlsx")

pairs = zip(new_records, old_records)

if any(x != y for x, y in pairs):
    print "Job Progress, generated", datetime.date.today().strftime('%B %d, %Y')
    for new, old in zip(new_records, old_records):
        for key, value in new.items():
            if value != old[key] and value !="":
                print "Door:", new["Door Name"], key, "-", value
else:
    print("No Reported Job Progress This Week")

#rotate current to last week if compair is good
