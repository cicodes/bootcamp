#1.soru
flat = []
def flatten(liste):
    for i in liste:
        if not type(i) is list:
            flat.append(i)
        else: 
            flatten(i)
    return flat

  
#2.soru
def reversy(liste):
    liste = liste[::-1]
    for i in range(len(liste)):
        if type(liste[i]) is list:
            liste[i] = liste[i][::-1]
    return liste
