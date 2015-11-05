To simulate mapReduce over inagural data

cat ../../../data/inaugural/*.txt | python wordcount.py | sort | python nReduce.py 1
