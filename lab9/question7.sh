#!/bin/bash

mass=1

c=299792458

energy=$(bc << EOF
scale=0
mass = $mass
c = $c
energy =$mass *$c *$c
energy
EOF
)

echo "Energy (Joules) for mass = $mass kg moving at speed of light (c = $c m/s):"
echo "the value is  $energy"

