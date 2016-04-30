#!/usr/bin/env bash

check=1
function run {
  cmd=$@
  echo
  echo "#################################"
  echo $cmd
  echo "#################################"
  eval $cmd
  if [ $check -ne 0 -a $? -ne 0 ]; then
    1>&2 echo "Command failed!"
    exit 1
  fi
}

cmd="./copy.py $E2d/w501_train.h5 -o train.h5 --nb_sample 10000"
# run $cmd

cmd="./copy.py $E2d/w501_val.h5 -o val.h5 --nb_sample 10000"
# run $cmd

cmd="./copy.py $E2d/w501_all_sorted.h5 -o test.h5 --nb_sample 10000"
# run $cmd
