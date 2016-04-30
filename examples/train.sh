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

cmd="$root/scripts/train.py
  $root/data/train.h5
  --val_file $root/data/val.h5
  --params ./configs.yaml
  --targets 'ESC_Ser3.*'
  --nb_epoch 5
  --early_stop 4
  --lr_schedule 3
  --out_dir ./model"

run $cmd
