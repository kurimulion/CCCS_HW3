# Cloud Computing and Cyber Security - Homework 3

### Files
* mapper.py: mapper script for extracting date in access log
* reducer.py: reducer script for counting acessses per hour
* AccessCount.java: source for mapper and reducer in Java
* access_log

### Usage
```
$ hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input access_log \
-output access_output

$ hadoop com.sun.tools.javac.Main AccessCount.java
$ jar cf ac.jar AccessCount*.class
$ hadoop jar ac.jar AccessCount access_log access_output
```