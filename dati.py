def ierakstit (teksts):
    fails = open("teksts.txt", "w", encoding="utf-8")  # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()
    return

# ierakstit_klat ("Mani sauc Toms")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="itf-8")
    fails.write(teksts)+"\n"
    fails.close
    return

# pierakstit_klat ("Man garso banani")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

#print(nolasit_visu())

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()

for i in range(len(rindas)):
    rindas[i] = rindas[i].strip()

    return rindas

saraksts = dabut_rindinas
    print(saraksts)