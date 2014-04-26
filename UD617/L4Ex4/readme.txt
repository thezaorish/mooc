cd L4Ex4/
sudo chmod +x reducer.py mapper.py
cd ../
cat purchases_100.txt | L4Ex4/mapper.py > L4Ex4/testmapper.txt
cat purchases_100.txt | L4Ex4/mapper.py | sort | L4Ex4/reducer.py > L4Ex4/testreducer.txt
cd L4Ex4/
hs mapper.py reducer.py myinput outputL4Ex4
hadoop fs -get outputL4Ex4 L4Ex4result