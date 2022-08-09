import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_start = 'python_crash_course/chapter_16_data/'
filename = file_start + 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #getting the max temperature from the file
    dates, highs, lows = [], [], []
    
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(date)    

#Graph settings
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='black', alpha=0.3)

ax.set_title("Highest temperature of the day - 2018", fontsize = 16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()