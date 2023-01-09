import time
import pandas as pd

csv_filename = 'first_trial_0_path_test.csv'
df = pd.read_csv(csv_filename)
Time =  df['t(s)']
t = 1
for i in range(len(df)):   
    print(df.loc[i])
    time.sleep(Time[t] - Time[t-1])