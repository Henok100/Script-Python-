import socket
import csv
import time
import pickle

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1334))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print("Connection has been established.")
    print("Sending...")
    csv_filename = 'first_trial_0_path_test.csv'
    with open(csv_filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            #print(row)
            clientsocket.send(bytes(str(row), "utf-8"))
            time.sleep(2)
            
clientsocket.close()
    