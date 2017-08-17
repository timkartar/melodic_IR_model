#!/bin/bash
for f in piano_right_genome/*.txt
do
s=$(basename -a $f)
s=${s%.txt}
s=$s".csv"
cd rightcsv
> "${s}"
echo motifs,time >> "${s}"
cd ..
cut -f1 $f > temp1
cut -f2 $f | cut -d ' ' -f1 > temp2
paste -d ',' temp1 temp2 >> rightcsv/"${s}"
done

for f in piano_left_genome/*.txt
do
s=$(basename -a $f)
s=${s%.txt}
s=$s".csv"
cd leftcsv
> "${s}"
echo motifs,time >> "${s}"
cd ..
cut -f1 $f > temp1
cut -f2 $f | cut -d ' ' -f1 > temp2
paste -d ',' temp1 temp2 >> leftcsv/"${s}"
done

