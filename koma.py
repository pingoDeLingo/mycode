def koma(lause):
    #lause = input("lause?:")
    #lause = lause.upper()
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace (" aga ", ", aga ")
    lause = lause.replace (" siis ", ", siis ")
    print(lause)


koma("Ta sundis alluvaid et ta saaks midagi sest miks mitte aga ei saanud midagi.")