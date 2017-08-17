#!/bin/bash
for f in *.mid
do
s=$(basename -a $f)
echo ${s%.mid} >> ../leftfrench.txt
done
