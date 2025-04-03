from classes import Word, Thing


# Things
tSoweli = Thing("soweli", sprite = ["Things/tSoweliBack", "Things/tSoweliSide", "Things/tSoweliFront"], facing = 1, p = True) # animal
tSinpin = Thing("sinpin", sprite = "Things/tSinpin") # wall
tKiwen = Thing("kiwen", sprite = "Things/tKiwen") # rock
tKon = Thing("kon") # air (empty cell)
tLen = Thing("len", sprite = "Things/tLen") # flag
tSeli = Thing("seli", sprite = "Things/tSeli") # fire
tLupa = Thing("lupa", sprite = "Things/tLupa") # door
tIlo = Thing("ilo", sprite = "Things/tIlo", facing = 2) # key
tSelo = Thing("selo", sprite = "Things/tSelo") # border
tPipi = Thing("pipi", sprite = "Things/tPipi") # bug

# Particles
wLi = Word("li", 0, sprite = "Words/wLi") # is; and (for predicates only)
wEn = Word("en", 0, sprite = "Words/wEn") # and (for subjects only)
wAla = Word("ala", 0, sprite = "Words/wAla") # not (for subjects and/or predicates)

# Nouns
wSoweli = Word("soweli", 1, tSoweli, sprite = "Words/wSoweli")
wSinpin = Word("sinpin", 1, tSinpin, sprite = "Words/wSinpin")
wKiwen = Word("kiwen", 1, tKiwen, sprite = "Words/wKiwen")
wKon = Word("kon", 1, tKon, sprite = "Words/wKon")
wLen = Word("len", 1, tLen, sprite = "Words/wLen")
wSeli = Word("seli", 1, tSeli, sprite = "Words/wSeli")
wLupa = Word("lupa", 1, tLupa, sprite = "Words/wLupa")
wIlo = Word("ilo", 1, tIlo, sprite = "Words/wIlo")
wSelo = Word("selo", 1, tSelo, sprite = "Words/wSelo")
wPipi = Word("pipi", 1, tPipi, sprite = "Words/wPipi")

# Adjectives
wSina = Word("sina", 2, sprite = "Words/wSina") # you
wPini = Word("pini", 2, sprite = "Words/wPini") # closed
wOpen = Word("open", 2, sprite = "Words/wOpen") # open
wAwen = Word("awen", 2, sprite = "Words/wAwen") # stop
wTawa = Word("tawa", 2, sprite = "Words/wTawa") # push
wPona = Word("pona", 2, sprite = "Words/wPona") # win
wMoli = Word("moli", 2, sprite = "Words/wMoli") # kill
wDummy = Word(" ", 2)