cd FinalProject/
sudo chmod +x student_times_reducer.py student_times_mapper.py
cd ../

cat forum_node_100.txt | FinalProject/student_times_mapper.py > FinalProject/testmapper.txt
cat forum_node_100.txt | FinalProject/student_times_mapper.py | sort | FinalProject/student_times_reducer.py > FinalProject/student_times_reducer_test.txt