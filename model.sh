#!/bin/bash
for f in leftcsv/*.csv
do
s=$(basename -a $f)
cd leftmodel
> "${s}"
echo timestamp,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P > "${s}"
cd ..
done
python model.py < pianofrench.txt

