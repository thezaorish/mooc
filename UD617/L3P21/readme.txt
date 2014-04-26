hadoop fs -put ~/udacity_training/data/access_log logs

cd L3P21/
sudo chmod +x reducer.py mapper.py
cd ../
cat access_log_100.txt | L3P21/mapper.py > L3P21/testmapper.txt
cat access_log_100.txt | L3P21/mapper.py | sort | L3P21/reducer.py > L3P21/testreducer.txt
cd L3P21/
hs mapper.py reducer.py logs outputP3L21
hadoop fs -get outputP3L21 P3L21result