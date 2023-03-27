#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /color/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /color/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /color/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../parking/parking-violation-2022.csv /color/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../parking/color/mapper1.py -mapper ../../parking/color/mapper1.py \
-file ../../parking/color/reducer1.py -reducer ../../parking/color/reducer1.py \
-input /color/input/* -output /color/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-file ../../parking/color/mapper2.py -mapper ../../parking/color/mapper2.py \
-file ../../parking/color/reducer2.py -reducer ../../parking/color/reducer2.py \
-input /color/output/* -output /color-2/output/


/usr/local/hadoop/bin/hdfs dfs -cat /color-2/output/part-00000 | head -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /color/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /color/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /color-2/output/
../../stop.sh
