#!/bin/bash

LANG=C

for i in {0..100}
do
  s=$(printf "%.2f" $(bc<<<"scale=2; $i/100"))
  f=$(printf "%03d" $i)
  sed "s/fill:#ffffff;fill-opacity:.*;/fill:#ffffff;fill-opacity:$s;/" bulb.svg | rsvg-convert > "bulb/$f.png"
done
