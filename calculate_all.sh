#!/bin/bash

for file in data/*
do
  python3 calculate_gender_gap.py "$file"
done