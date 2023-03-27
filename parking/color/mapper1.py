#!/usr/bin/env python
import sys
import re

# list of color codes in the data set
re_BLACK = {x:"BLACK" for x in ["BLACK", "BK", "BLK", "DK", "Black", "LTBK", "DARK", "BLCK", "BLA", "BKBK", "BLAK", "BLAC", "DKBK", "BKL", "BCK", "BLC", "DKDK", "BKX", "BIK", "BKNO", "BLACL", "BACK", "BALCK", "BKACK", "BKL", "NLACK", "BKN", "NBLCK", "NK", "BBLK", "BKB", "BKZ", "BLAAC", "VLK", "VK", "BPK", "DRK", "BKLKK"]}
re_BLUE = {x:"BLUE" for x in ["BL", "BLUE", "BLU", "LTBL", "DBL", "BLBL", "LBL", "BLB", "DKBL", "BLE", "NAVY", "BUE", "BLV", "DARKB", "BRU", "NAVYB", "BBLUE", "BKU", "BKUE", "VLUE", "BLUEB", "BLUER", "BLUR", "BUE", "BUL", "NAVI", "TEAL", "BKUE"]}
re_BROWN = {x:"BROWN" for x in ["BR", "BROWN", "BRO", "BRN", "BRW", "DKBR", "BRWN", "BN", "BROW", "BWN", "BRWON", "BROWM", "LTBR"]}
re_BRONZE = {x:"BRONZE" for x in ["BRZ", "BRONZ", "COPPE", "BX", "BKZ"]}
re_BURGUNDY = {x:"BURGUNDY" for x in ["BURG", "BUR", "BURGU", "BURGA", "BRG", "Maroo", "MA", "MARON", "BURGD", "BURUN", "BGDY", "BGY", "BURGN", "BURGY", "MROON", "MRMR", "MR", "MARRO", "MARO", "MARN", "BURDI", "BURD", "BURND", "DKMR", "M", "DKM", "LTMR", "MRN", "MA"]}
re_CREAM = {x:"CREAM" for x in ["BEI", "Beig", "BRIGE", "BEIGE", "BEGE", "BEG", "BIGE", "BERGE", "BIEG", "CREAM", "CRM", "TAUPE"]}
re_GREY = {x:"GREY" for x in ["GY", "GREY", "GRY", "GRAY", "DKGY", "GYGY", "LTGY", "GYG", "GARY", "GEY", "GYD", "GYN", "GAY", "GYA", "GYJUU", "GYX", "GYII", "GTAY", "FRAY", "GGREY", "GHY", "GRAW", "GRAYY", "GREI", "GRTAY", "GYAY", "GYY", "DGRY", "GGRAY", "GERY", "GRET"]}
re_GREEN = {x:"GREEN" for x in ["GR", "LTGR", "GREEN", "GRN", "DKGR", "GN", "GRGR", "GRE", "GRG", "TEA", "GREN", "GRW", "GREE", "TURQU", "TRQ", "OLIV"]}
re_GOLD = {x:"GOLD" for x in ["GLD", "GL", "LTGL", "GOLD", "GD", "GOL", "SAND"]}
re_RED = {x:"RED" for x in ["RD", "RED", "DKRD", "R", "RDW", "LTRD", "RE", "REDRE", "RDV", "RDK", "YRED", "TRED", "RESD", "REDW", "REDE", "REDB", "RDE"]}
re_RUST = {x:"RUST" for x in ["TN", "TAN", "DKTN", "LTTN", "TNG", "TNTN", "RUST", "TANB"]}
re_WHITE = {x:"WHITE" for x in ["WH", "WHITE", "WHI", "WHT", "WHB", "W", "WT", "WHTE", "WHIT", "WTE", "LIGHT", "WHE", "WHIE", "WHN", "WHHIT", "LTWH", "WI", "WHV", "WHTIE", "WTH", "WHY", "WY", "WHTI", "DKWH", "DKW", "WHU", "WHM", "WHIIT", "HITE", "WWH", "WHJT", "WHIYE", "WHIUT", "WHITW", "WHITR", "WHI", "WHHI", "WBHIT", "YWHT", "QHITE"]}
re_SILVER = {x:"SILVER" for x in ["SILVE", "SIL", "SILV", "SL", "SLV", "SLVR", "ALUMI", "S", "SIV", "SILVR", "SI", "SV", "SLIVE", "SLVER", "SLIV", "SVR", "SIVR", "SIVER", "SLR", "SILER", "SVL", "SLI", "SLVE", "SLIR", "SIVLE", "SILVB", "SLVRE", "SILVV", "SILVI", "SILVA", "SILV"]}
re_YELLOW = {x:"YELLOW" for x in ["YW", "YELLO", "YEL", "YELL", "YL", "YLW", "Y", "YE", "LTYW", "YELLW", "YLL", "YLLW", "YEW", "YELOW", "DKYW"]}
re_ORANGE = {x:"ORANGE" for x in ["OR", "ORANG", "ONG", "ORG", "ORA", "ORAN", "O", "ORN", "ORNG", "ON", "OG", "ARG", "ORGE", "ORAG", "ORNGE", "ORANGE"]}
re_PURPLE = {x:"PURPLE" for x in ["PR", "PURPL", "LAVEN", "DKPR", "PURP", "PUR", "LTPR", "PRPL", "PRPLE", "LAV", "PL", "PRP", "PUPR", "PUPLE", "PRL"]}
re_PINK = {x:"PINK" for x in ["PK", "PINK", "PNK", "DKPK", "LTPK", "PINKW", "PINKT"]}
re_MULTI = {x:"MULTI" for x in ["BKGY", "WHBL", "WHGY", "BLGY", "BKBL", "GYBL", "GYBK", "WHBK", "RDGY", "GYBR", "BKGR", "WHRD", "GRGY", "BLBK", "WHGR", "BKRD", "RDBK", "BLWH", "BLGR", "BKWH", "BKTN", "RDBL", "GYTN", "WHTN", "BRGY", "TNGY", "GYBR", "GYGL", "RDWH", "GYWH", "GLGY", "RDGR", "WHBR", "BLRD", "BKBR", "GRBK", "YWBK", "ORWH", "BLTN", "MRGY", "RDTN", "GRBL", "GRTN", "ORRD", "ORBK", "GRWH", "MULTI", "BKGL", "RDBR", "BLBR", "TNGR", "WHGL", "TNBL", "ORGY", "GRRD", "RDMR", "GYMR", "GYOR", "BRBL", "MRTN", "GLGR", "PRGY", "BKYW", "PRWH", "BRRD", "YWWH", "BKOR", "BRGR", "BLGL", "RDGL", "BKPR", "GLBR", "MRBL", "GLTN", "TNRD", "YWBL", "MRGR", "BLYW", "GRGL", "WHYW", "GLRD", "BRTN", "GLBL", "GYBK", "BKMR", "ORBL", "GRBR", "YWGY", "BLMR", "GLBK", "TNGL", "MRRD", "BLGY", "TNBR", "BRBK", "BRGL", "BKTN", "BLOR", "WHGRN", "BLPR", "WHMR", "TNOR", "WHPI", "GRY", "MRBR", "WHPR", "WHPK", "MRBK", "GLWH", "BLKTAN", "GYYW", "PKWH", "TNBK", "TNWH", "ORPR", "MULT", "GYBL", "RDOR", "MRWH", "PKGL", "YWRD", "TNPR", "ORTN", "GYYA", "GYTN", "BRWH", "BKPK", "GYPK", "YWGR", "BRMR", "RDPR", "RDOR", "GLOR", "PRBL", "PRBK", "PKGY", "BLUGR", "BLUGY", "WHGL", "ORGL", "ORGN", "GLTN", "GRBK", "GROR", "GRPR", "WTGR", "YWTN", "WHTGR", "WHOR", "BROR", "BRYW", "YWGL", "PRWH", "PKPR"]}

re_COLOR = [re_BLACK, re_BLUE, re_BROWN, re_BRONZE, re_BURGUNDY, re_CREAM, re_GREY, re_GREEN, re_GOLD, re_RED, re_RUST, re_WHITE, re_SILVER, re_YELLOW, re_ORANGE, re_PURPLE, re_PINK, re_MULTI]

for idx, line in enumerate(sys.stdin):
    if idx == 0:
        continue
	
    line = line.strip()
    color = re.sub("[^A-Z]", "", line.split(",")[33].upper())

    # Conventionalize Color Names
    for dct in re_COLOR:
        regex = re.compile("^(%s)$" % "|".join(map(re.escape, dct.keys())))
        if regex.search(color):
          color1 = regex.sub(list(dct.values())[0], color)
          continue
        
    print("%s\t%s" % (color1, 1))
