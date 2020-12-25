#!/bin/bash

for i in {01..25}; do
    echo "Day $i"
    cd $i
    echo -ne "Part 1: "
    ./p1.py
    echo -ne "Part 2: "
    ./p2.py
    echo
    cd ..
done
