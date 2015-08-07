#Installation
_____________________________________________________________________________________________________________

1. Install plugin python for intellij 
2. Download spark-1.4.1-bin-hadoop2.6.tgz at https://spark.apache.org/downloads.html
3. tar -xvzf spark-1.4.1-bin-hadoop2.6.tgz and go in /spark-1.4.1-bin-hadoop2.6/python/lib
4. unzip pyspark.zip and py4j-0.8.2.1-src.zip
5. Put these two packages in site-packages of your python. (In my case: cp -r py4j /usr/lib64/python2.7/site-packages/ )
6. Create a new Project Python
7. Create a SparkPi.py script and run it
8. Do not forget to add SPARK_HOME in environment variable (In my case: SPARK_HOME /home/cbovigny/Documents/Programs/spark-1.4.1-bin-hadoop2.6)

Have fun with SparkPi in python


_____________________________________________________________________________________________________________