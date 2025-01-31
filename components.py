from classes import Word, Thing


tSoweli = Thing("soweli")
tSinpin = Thing("sinpin")
tKiwen = Thing("kiwen")
tKon = Thing("kon")
tLen = Thing("len")
tSeli = Thing("seli")
tLupa = Thing("lupa")
tIlo = Thing("ilo")
tSelo = Thing("selo")
tPipi = Thing("pipi")

wLi = Word("li", 0)
wEn = Word("en", 0)
wAla = Word("ala", 0)

wSoweli = Word("soweli", 1, tSoweli) # animal
wSinpin = Word("sinpin", 1, tSinpin) # wall
wKiwen = Word("kiwen", 1, tKiwen) # rock
wKon = Word("kon", 1, tKon) # air (empty)
wLen = Word("len", 1, tLen) # flag
wSeli = Word("seli", 1, tSeli) # fire
wLupa = Word("lupa", 1, tLupa) # door
wIlo = Word("ilo", 1, tIlo) # key
wSelo = Word("selo", 1, tSelo) # barrier
wPipi = Word("pipi", 1, tPipi) # bug

wSina = Word("sina", 2) # you
wPini = Word("pini", 2) # closed
wOpen = Word("open", 2) # open
wAwen = Word("awen", 2) # stop
wTawa = Word("tawa", 2) # push
wPona = Word("pona", 2) # win
wMoli = Word("moli", 2) # kill