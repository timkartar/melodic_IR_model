#!/bin/bash
for f in piano_right_genome/*.txt
do
s=$(basename -a $f)
echo "done 1"
cd simple_right_stamp
echo "done 2"
> "${s}"
echo "done 3"
cd ..
echo "done 4"
n=$(grep -c ^ $f)
echo "done 5"
echo $n > input
echo "done 6"
cut -f1 $f > temp1
echo "done 7"
cut -f2 $f | cut -d ' ' -f1 > temp2
echo "done 8"
cat temp2 >> input
echo "done 9"
cat temp1 >> input
echo "done 10"
./timestamp < input > simple_right_stamp/"${s}"
echo "done 11"
done

for f in piano_left_genome/*.txt
do
s=$(basename -a $f)
cd simple_left_stamp
> "${s}"
cd ..
n=$(grep -c ^ $f)
echo $n > input
cut -f1 $f > temp1
cut -f2 $f | cut -d ' ' -f1 > temp2
cat temp2 >> input
cat temp1 >> input
./timestamp < input > simple_left_stamp/"${s}"
done

