#!/bin/bash

gawk '$4 == "PHE" && $1 == "ATOM" {print $7 $8 $9}' 1HK0.pdb > PHE_atoms.xyz

