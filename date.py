from datetime import datetime, timedelta
import sys

try:
    start_date = sys.argv[1]
    end_date = sys.argv[2]
except:
    print("python3 {} 2022-12-01 2022-12-31".format(sys.argv[0]))
    exit()

start_date = datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.strptime(end_date, "%Y-%m-%d")

date = start_date
while date <= end_date:
  print(date.strftime("%Y-%m-%d"))
  date += timedelta(days=1)
sys.exit()
