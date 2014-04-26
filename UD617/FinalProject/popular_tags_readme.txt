cd FinalProject/
sudo chmod +x popular_tags_mapper.py popular_tags_reducer.py
cd ../

cat forum_node_100.txt | FinalProject/popular_tags_mapper.py > FinalProject/popular_tags_mapper_test.txt
cat forum_node_100.txt | FinalProject/popular_tags_mapper.py | sort | FinalProject/popular_tags_reducer.py > FinalProject/popular_tags_reducer_test.txt