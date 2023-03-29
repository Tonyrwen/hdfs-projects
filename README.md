# hdfs-projects

To make the hdfs mapreduce programs work, do the following set-ups first:
1. `cd /` 
2. `git clone` this repo
3. `mv /hdfs-projects /big-data-project`
4. `cd big-data-project`
5. `chmod +x start.sh`
6. `chmod +x stop.sh`
7. `cd /big-data-project/parking`
8. `wget -O parking-violation-2022.csv https://data.cityofnewyork.us/api/views/pvqr-7yc4/rows.csv?accessType=DOWNLOAD`

Now you can go to any of the subfolders with a test.sh file and bash it to run the mapreduce program
