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

root=".."

cmd="$root/scripts/predict.sh
  $root/data/test.h5
  --model ./model/model.json ./model/model_weights.h5
  -o predict.h5"

run $cmd
