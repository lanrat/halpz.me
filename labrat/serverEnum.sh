#!/usr/bin/env bash
for i in $(seq 200 400);
do
  #echo Checking ieng6-$i
  result=$(host ieng6-$i | grep "address")
  #result=$(host ieng6-$i | grep "not found")
  if [ -n "$result" ];
  then
    echo ieng6-$i
  fi

done
