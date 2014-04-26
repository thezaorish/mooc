cd FinalProject/
sudo chmod +x study_groups_reducer.py study_groups_mapper.py
cd ../

cat forum_node_100.txt | FinalProject/study_groups_mapper.py > FinalProject/study_groups_mapper_test.txt
cat forum_node_100.txt | FinalProject/study_groups_mapper.py | sort | FinalProject/study_groups_reducer.py > FinalProject/study_groups_reducer_test.txt