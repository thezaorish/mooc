cd L4Ex5/
sudo chmod +x reducer.py mapper.py
cd ../
cat purchases_100.txt | L4Ex5/mapper.py > L4Ex5/testmapper.txt
cat purchases_100.txt | L4Ex5/mapper.py | sort | L4Ex5/reducer.py > L4Ex5/testreducer.txt
cd L4Ex5/
hsc mapper.py reducer.py myinput outputL4Ex5