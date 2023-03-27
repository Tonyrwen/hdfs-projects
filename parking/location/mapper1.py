#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import sys
import re

for idx, line in enumerate(sys.stdin):
	if idx == 0:
		continue
	
	line = line.strip()
	street = line.split(",")[24]
	
	# Standardize Abbreviation
	street = re.sub("alley", "ALY", street, flags = re.IGNORECASE)
	street = re.sub("avenue", "AVE", street, flags = re.IGNORECASE)
	street = re.sub("boulevard", "BLVD", street, flags = re.IGNORECASE)
	street = re.sub("causeway", "CSWY", street, flags = re.IGNORECASE)
	street = re.sub("center", "CTR", street, flags = re.IGNORECASE)
	street = re.sub("circle", "CIR", street, flags = re.IGNORECASE)
	street = re.sub("court", "CT", street, flags = re.IGNORECASE)
	street = re.sub("cove", "CV", street, flags = re.IGNORECASE)
	street = re.sub("crossing", "XING", street, flags = re.IGNORECASE)
	street = re.sub("drive", "DR", street, flags = re.IGNORECASE)
	street = re.sub("expressway", "EXPY", street, flags = re.IGNORECASE)
	street = re.sub("extension", "EXT", street, flags = re.IGNORECASE)
	street = re.sub("freeway", "FWY", street, flags = re.IGNORECASE)
	street = re.sub("grove", "GRV", street, flags = re.IGNORECASE)
	street = re.sub("highway", "HWY", street, flags = re.IGNORECASE)
	street = re.sub("hollow", "HOLW", street, flags = re.IGNORECASE)
	street = re.sub("junction", "JCT", street, flags = re.IGNORECASE)
	street = re.sub("lane", "LN", street, flags = re.IGNORECASE)
	street = re.sub("motorway", "MTWY", street, flags = re.IGNORECASE)
	street = re.sub("overpass", "OPAS", street, flags = re.IGNORECASE)
	street = re.sub("park", "PARK", street, flags = re.IGNORECASE)
	street = re.sub("pk", "PARK", street, flags = re.IGNORECASE)
	street = re.sub("parkway", "PKWY", street, flags = re.IGNORECASE)
	street = re.sub("pkway", "PKWY", street, flags = re.IGNORECASE)
	street = re.sub("place", "PL", street, flags = re.IGNORECASE)
	street = re.sub("plaza", "PLZ", street, flags = re.IGNORECASE)
	street = re.sub("point", "PT", street, flags = re.IGNORECASE)
	street = re.sub("road", "RD", street, flags = re.IGNORECASE)
	street = re.sub("route", "RTE", street, flags = re.IGNORECASE)
	street = re.sub("skyway", "SKWY", street, flags = re.IGNORECASE)
	street = re.sub("square", "SQ", street, flags = re.IGNORECASE)
	street = re.sub("street", "ST", street, flags = re.IGNORECASE)
	street = re.sub("str", "ST", street, flags = re.IGNORECASE)
	street = re.sub("terrace", "TER", street, flags = re.IGNORECASE)
	street = re.sub("trail", "TRL", street, flags = re.IGNORECASE)

	# remove inconsistent th/st/nd
	street = re.sub(r"(?<=\d)(st|nd|rd|th)\b", "", street, flags = re.IGNORECASE)
	
	# standardize direction
	street = re.sub("west", "W", street, flags = re.IGNORECASE)
	street = re.sub("east", "E", street, flags = re.IGNORECASE)
	street = re.sub("north", "N", street, flags = re.IGNORECASE)
	street = re.sub("south", "S", street, flags = re.IGNORECASE)

	# replace whitespace with underscore
	street = re.sub(" ", "_", street)

	print("%s\t%s" % (street, 1))
