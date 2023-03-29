#!/usr/bin/env python
import sys

for idx, line in enumerate(sys.stdin):
  if idx == 0: continue

  line = line.strip().split(",")

  def_last, def_first, player = line[15].lower().strip(), line[16].lower().strip(), line[21].replace(" ", "_") 
  
  made = 1 if line[14] == "made" else 0 if line[14] == "missed" else None
  
  defender = (' '.join((def_first,def_last))).replace('"', "").replace(" ", "_")

  print("%s,%s\t%s,%s"%(player, defender, made, 1))



