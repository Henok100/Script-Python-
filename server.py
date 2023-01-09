import socket
import csv
import time
import pandas as pd

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1456))
s.listen(5)

csv_filename = 'first_trial_0_path_test.csv'
df = pd.read_csv(csv_filename)
Time =  df['t(s)']
t = -1;
while True:
    clientsocket, address = s.accept()
    print("Connection has been established.")
   
    with open(csv_filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            clientsocket.send(bytes(str(row), "utf-8"))
            t = t + 1
            print("Sending at ", Time[t+1] - Time[t], "Second")
            time.sleep(Time[t+1] - Time[t])
           
clientsocket.close()
    