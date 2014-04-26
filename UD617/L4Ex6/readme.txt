cd L4Ex6/
sudo chmod +x mapper.py reducer.py
cd ../
cat forum_node_100.txt forum_users.tsv | L4Ex6/mapper.py > L4Ex6/testmapper.txt
cat forum_node_100.txt | L4Ex6/mapper.py | sort | L4Ex6/reducer.py > L4Ex6/testreducer.txt