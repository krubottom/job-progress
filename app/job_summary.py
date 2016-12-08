import pyexcel as pe

records = pe.get_records(file_name="jobs.xlsx")
for records in records:
    print("Door: %s Cable Run: %s CR: %s DC: %s Lock: %s" % (records['Door Number'], records["Cable Ran"], records["CR"], records["DC"], records["Lock"]))
