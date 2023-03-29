#!/bin/sh
/usr/local/hadoop/sbin/start-all.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Fear-Score/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Fear-Score/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Fear-Score/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../shot_logs.csv /Fear-Score/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Fear-Score/mapper1.py -mapper ../Fear-Score/mapper1.py \
-file ../Fear-Score/reducer1.py -reducer ../Fear-Score/reducer1.py \
-input /Fear-Score/input/* -output /Fear-Score/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
# set key to be till the 3 comma
-D mapred.output.textoutputformat.separator="," \
-D stream.num.map.output.key.fields=3 \
# arrange by player name first, then hit rate ascending, then attempts decending
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options="-k1,1 -k2,2n -k3,3nr"\
# partition by player name only
-D mapred.text.key.partitioner.options=-k1,1 \
-file ../Fear-Score/mapper2.py -mapper ../Fear-Score/mapper2.py \
-file ../Fear-Score/reducer2.py -reducer ../Fear-Score/reducer2.py \
-input /Fear-Score/output/* -output /Fear-Score-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Fear-Score-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Fear-Score/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Fear-Score/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Fear-Score-2/output/
/usr/local/hadoop/sbin/stop-all.sh

