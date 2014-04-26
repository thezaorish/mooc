cd L3P12/
sudo chmod +x reducer.py mapper.py
cd ../
cat purchases_100.txt | L3P12/mapper.py > L3P12/testmapper.txt
cat purchases_100.txt | L3P12/mapper.py | sort | L3P12/reducer.py > L3P12/testreducer.txt
cd L3P12/
hs mapper.py reducer.py myinput outputP3L12
hadoop fs -get outputP3L12 P3L12result