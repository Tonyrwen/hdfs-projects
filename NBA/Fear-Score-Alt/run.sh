#!/bin/sh
# Start hadoop
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/sbin/start-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
 
# Remove temp folders
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
 
# Create a new one
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /q1/input/
 
# Copying the file
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../shot_logs.csv /q1/input/
 
 
# First round
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper-1.py -mapper mapper-1.py \
-file reducer-1.py -reducer reducer-1.py \
-input /q1/input/* -output /q1/output/
 
 
# Second Round
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper-2.py -mapper mapper-2.py \
-file reducer-2.py -reducer reducer-2.py \
-input /q1/output/* -output /q1-final/output/
 
 
# Print Output
/usr/local/hadoop/bin/hdfs dfs -cat /q1-final/output/part-00000
 
# Delete temp folders
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1-final/output/
 
 
# Stop Hadoop
/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/stop-yarn.sh
/usr/local/hadoop/sbin/mr-jobhistory-daemon.sh stop historyserver
