cd L3P13/
sudo chmod +x reducer1.py mapper1.py mapper2.py
cd ../
cat purchases_100.txt | L3P13/mapper1.py > L3P12/testmapper1.txt
cat purchases_100.txt | L3P13/mapper1.py > L3P13/testmapper1.txt
cat purchases_100.txt | L3P13/mapper2.py > L3P13/testmapper2.txt
cat purchases_100.txt | L3P13/mapper2.py | sort | L3P13/reducer1.py > L3P13/testreducer1.txt
cd L3P13/
hs mapper1.py reducer1.py myinput outputP3L131
hadoop fs -get outputP3L131 P3L131result
hs mapper2.py reducer1.py myinput outputP3L132
hadoop fs -get outputP3L132 P3L132result