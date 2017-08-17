#!/bin/bash
for f in rightcsv/*.csv
do
s=$(basename -a $f)
cd rightmodel
> "${s}"
echo timestamp,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P > "${s}"
cd ..
python model.py < pianofrench.txt >> rightmodel/"${s}"
done 
