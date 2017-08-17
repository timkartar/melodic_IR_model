#!/bin/bash
for f in PianoLeft/*.mid
do
s=$(basename -a $f)
ss='Piano_left_texts/'${s%.mid}'.txt'
> "${ss}"
done
