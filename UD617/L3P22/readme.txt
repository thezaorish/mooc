cd L3P22/
sudo chmod +x reducer.py mapper.py
cd ../
cat access_log_100.txt | L3P22/mapper.py > L3P22/testmapper.txt
cat access_log_100.txt | L3P22/mapper.py | sort | L3P22/reducer.py > L3P22/testreducer.txt
cd L3P22/
hs mapper.py reducer.py logs outputP3L22
hadoop fs -get outputP3L22 P3L22result