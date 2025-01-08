import pandas as pd 
screen_time = [1,2,3,4,5,6,7,8]
sleep_hours = [7,8,9,10,11,12,13,14]
study_hours = [2,3,4,5,6,8,9,11]
dict = {
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "study_hours":study_hours
}
print(dict)
df = pd.DataFrame(dict)
print(df)
