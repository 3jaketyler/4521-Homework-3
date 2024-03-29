# The program in this file is the individual work of Jake Tyler

#!/bin/bash

python3 input.py

wait

python3 Prepro+map.py > tmp.txt

wait

for ((i=1; i<=200; i++)); do
    python3 Prepro+map.py >> tmp.txt
done

wait

rm data.txt

python3 reducer.py < tmp.txt

rm tmp.txt