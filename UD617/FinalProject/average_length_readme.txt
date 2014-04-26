cd FinalProject/
sudo chmod +x average_length_mapper.py average_length_reducer.py
cd ../

cat forum_node_100.txt | FinalProject/average_length_mapper.py > FinalProject/average_length_mapper_test.txt
cat forum_node_12.txt | FinalProject/average_length_mapper.py | sort | FinalProject/average_length_reducer.py > FinalProject/average_length_reducer_test.txt