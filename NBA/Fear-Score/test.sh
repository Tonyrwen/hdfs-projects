#!/bin/sh
/usr/local/hadoop/sbin/start-all.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /fs/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /fs/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /fs/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../shot_logs.csv /fs/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../fs/mapper1.py -mapper ../fs/mapper1.py \
-file ../fs/reducer1.py -reducer ../fs/reducer1.py \
-input /fs/input/* -output /fs/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
# set key to be till the 3 comma
-D mapred.output.textoutputformat.separator="," \
-D stream.num.map.output.key.fields=3 \
# arrange by player name first, then hit rate ascending, then attempts decending
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options="-k1,1 -k2,2n -k3,3nr"\
# partition by player name only
-D mapred.text.key.partitioner.options=-k1,1 \
-file ../fs/mapper2.py -mapper ../fs/mapper2.py \
-file ../fs/reducer2.py -reducer ../fs/reducer2.py \
-input /fs/output/* -output /fs-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /fs-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /fs/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /fs/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /fs-2/output/
/usr/local/hadoop/sbin/stop-all.sh

