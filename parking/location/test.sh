#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /location/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /location/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /location/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../parking/parking-violation-2022.csv /location/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../parking/location/mapper1.py -mapper ../../parking/location/mapper1.py \
-file ../../parking/location/reducer1.py -reducer ../../parking/location/reducer1.py \
-input /location/input/* -output /location/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-file ../../parking/location/mapper2.py -mapper ../../parking/location/mapper2.py \
-file ../../parking/location/reducer2.py -reducer ../../parking/location/reducer2.py \
-input /location/output/* -output /location-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /location-2/output/part-00000 | head -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /location/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /location/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /location-2/output/
../../stop.sh
