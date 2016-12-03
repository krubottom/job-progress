import pyexcel as pe

records = pe.get_records(file_name="jobs.xlsx")
for records in records:
    DC = "Done" if records["DC"] == 1 else "Not Done"
    print("Door: %s \nDC is %s" % (records['Door Number'], DC))
