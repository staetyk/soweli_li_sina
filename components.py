from classes import Word, Thing


tSoweli = Thing("soweli")
tSinpin = Thing("sinpin")
tKiwen = Thing("kiwen")
tKon = Thing("kon")
tLipu = Thing("lipu")
tSeli = Thing("seli")
tLupa = Thing("lupa")
tIlo = Thing("ilo")
tSelo = Thing("selo")

wLi = Word("li", 0)
wEn = Word("en", 0)
wAla = Word("ala", 0)

wSoweli = Word("soweli", 1, tSoweli)
wSinpin = Word("sinpin", 1, tSinpin)
wKiwen = Word("kiwen", 1, tKiwen)
wKon = Word("kon", 1, tKon)
wLipu = Word("lipu", 1, tLipu)
wSeli = Word("seli", 1, tSeli)
wLupa = Word("lupa", 1, tLupa)
wIlo = Word("ilo", 1, tIlo)
wSelo = Word("selo", 1, tSelo)

wSina = Word("sina", 2)
wPini = Word("pini", 2)
wOpen = Word("open", 2)
wAwen = Word("awen", 2)
wTawa = Word("tawa", 2)
wPona = Word("pona", 2)
wMoli = Word("moli", 2)