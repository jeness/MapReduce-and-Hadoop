# MapReduce course from udacity
Learning materials and progress of Udacity Intro to Hadoop and MapReduce course: https://classroom.udacity.com/courses/ud617
## Part 0: Download & configuration
### 1. Configure VM via: Introduction to Hadoop and Mapreduce- - VM setup.docx
Download VM via: [here](http://content.udacity-data.com/courses/ud617/Cloudera-Udacity-Training-VM-4.1.1.c.zip)
### 2. Dataset is available at:
http://content.udacity-data.com/courses/ud617/access_log.gz
http://content.udacity-data.com/courses/ud617/purchases.txt.gz
### 3. Transfer file between vm and host machine:
https://docs.google.com/document/d/1MZ_rNxJhR4HCU1qJ2-w7xlk2MTHVqa9lnl_uj-zRkzk/pub
### 4. Commends 
#### commend for hdfs
show file ls in hdfs
```
hadoop fs -ls
```
create directory myinput in hdfs 
```
hadoop fs -mkdir myinput    
```
put purchases.txt into hdfs
```
hadoop fs -put purchases.txt
```
put purchases.txt into myinput
```
hadoop fs -put purchases.txt myinput  
```
#### commends for test mapper and reducer code
get first 50 lines from purchases.txt
```
head -50 ../data/purchases.txt > testfile
```
send testfile to mapper
```
cat testfile | ./mapper.py
```
send testfile to mapper, then (shuffle)sort with linux pipe command, then send results to reducer.py
```
cat testfile | ./mapper.py | sort | ./reducer.py
```
Run job!!!
```
hs mapper.py reducer.py myinput output2
```
See result!!! list files in directory output2
```
hadoop fs -ls output2
```
See result content!!!
```
hadoop fs -cat output2/part-00000 | less
hadoop fs -cat output2/part-00000
```

## Part 2: Write mapper and reducer on one's own
refers to directory part1 and part2