
hdfs dfs -rm -r IPcount/ipcount_res



yarn jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	 -mapper " mapper.py" \
	 -reducer " reducer.py" \
	 -file mapper.py \
	 -file reducer.py \
	 -input "IPcount/access_log" \
	 -output "IPcount/ipcount_res"
  #-mapper "python3 $PWD/mapper.py" \
	 #-reducer "python3 $PWD/reducer.py" \
	
