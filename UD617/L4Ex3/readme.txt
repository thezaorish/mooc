cd L4Ex3/
sudo chmod +x reducer_count.py mapper.py reducer_nodes.py
cd ../


cat forum_node_100.txt | L4Ex3/mapper.py > L4Ex3/testmapper.txt
cat forum_node_100.txt | L4Ex3/mapper.py | sort | L4Ex3/reducer_count.py > L4Ex3/testreducer.txt
cd L4Ex3/
hs mapper.py reducer_count.py forum_node outputP4Ex3
hadoop fs -get outputP4Ex3 P4Ex3result


cat forum_node_100.txt | L4Ex3/mapper.py | sort | L4Ex3/reducer_nodes.py > L4Ex3/testreducer.txt
cd L4Ex3/
hs mapper.py reducer_nodes.py forum_node outputP4Ex3_2
hadoop fs -get outputP4Ex3_2 P4Ex3result_2