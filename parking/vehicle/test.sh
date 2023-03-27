#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /vehicle/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /vehicle/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /vehicle/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../parking/parking-violation-2022.csv /vehicle/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../parking/vehicle/mapper.py -mapper ../../parking/vehicle/mapper.py \
-file ../../parking/vehicle/reducer.py -reducer ../../parking/vehicle/reducer.py \
-input /vehicle/input/* -output /vehicle/output/

/usr/local/hadoop/bin/hdfs dfs -cat /vehicle/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /vehicle/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /vehicle/output/
../../stop.sh
