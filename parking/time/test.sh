#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /time/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /time/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /time/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../parking/parking-violation-2022.csv /time/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../parking/time/mapper.py -mapper ../../parking/time/mapper.py \
-file ../../parking/time/reducer.py -reducer ../../parking/time/reducer.py \
-input /time/input/* -output /time/output/

/usr/local/hadoop/bin/hdfs dfs -cat /time/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /time/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /time/output/
../../stop.sh
