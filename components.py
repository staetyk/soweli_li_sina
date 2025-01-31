from classes import Word, Thing


# Things
tSoweli = Thing("soweli") # animal
tSinpin = Thing("sinpin") # wall
tKiwen = Thing("kiwen") # rock
tKon = Thing("kon") # air (empty cell)
tLen = Thing("len") # flag
tSeli = Thing("seli") # fire
tLupa = Thing("lupa") # door
tIlo = Thing("ilo") # key
tSelo = Thing("selo") # fire
tPipi = Thing("pipi") # bug
tAle = Thing("ale") # all (everything; used for N. ala li statements)

# Particles
wLi = Word("li", 0) # is; and (for predicates only)
wEn = Word("en", 0) # and (for subjects only)
wAla = Word("ala", 0) # not (for subjects and/or predicates)

# Nouns
wSoweli = Word("soweli", 1, tSoweli)
wSinpin = Word("sinpin", 1, tSinpin)
wKiwen = Word("kiwen", 1, tKiwen)
wKon = Word("kon", 1, tKon)
wLen = Word("len", 1, tLen)
wSeli = Word("seli", 1, tSeli)
wLupa = Word("lupa", 1, tLupa)
wIlo = Word("ilo", 1, tIlo)
wSelo = Word("selo", 1, tSelo)
wPipi = Word("pipi", 1, tPipi)

# Adjectives
wSina = Word("sina", 2) # you
wPini = Word("pini", 2) # closed
wOpen = Word("open", 2) # open
wAwen = Word("awen", 2) # stop
wTawa = Word("tawa", 2) # push
wPona = Word("pona", 2) # win
wMoli = Word("moli", 2) # kill