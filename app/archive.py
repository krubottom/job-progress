import os
from datetime import datetime

dir = os.listdir("archive")

for files in dir:
    # print files.split("-")[1].split(".")[0]
    date_object = datetime.strptime(files.split("-")[1].split(".")[0], '%m%d%y')
    print(date_object.strftime('%B %d, %Y'))
