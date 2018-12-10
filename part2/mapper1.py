#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
       ip, identity, username, time, zone, method, address, protocol, status_code, data_size = data 
    #    print "{0}\t{1}".format(store, cost)  
    # ==========================
    # every item Category, calculate the total cost
        if address == "/assets/js/the-associates.js":
        print address
    # =========================
