from random import *

##exemple fondamental 1

def testinside (c,chaine):
    n=len(chaine)
    for i in range (n):
        if chaine[i]==c:
            return True
    return False






##exercice 1

def retourne(chaine):
    s=0
    l=len(chaine)
    for i in range (l):
        r=chaine[s]
        s=s+2
        chaine=r+chaine
    frag=chaine[0:l]
    print (frag)

##

def majvoyelle(chaine):
    voyelle="aàeéèiouy"
    chaineres=""
    for i in range(len(chaine)):
        lettre=chaine[i]
        if lettre in voyelle:
            chaineres=chaineres+lettre.upper()
        else:
            chaineres=chaineres+lettre
    return chaineres


##

def etoile(chaine):
    ch=" "
    for c in chaine:
        ch+=c+"*"
    return ch

##

def brinadn(n):
    gne=" "
    nucl = 'ATGC'
    for i in range (n):
        k=randint(0,3)
        gne=gne+nucl[k]
    return gne


##

def score(mot):
    result=0
    z=" "
    u="eainorstulEAINORSTUL"
    d="dmgDMG"
    t="bcpBCP"
    q="fhvFHV"
    h="jqJK"
    x="kwxyzKWXYZ"
    for i in range(len(mot)):
        lettre=mot[i]
        if lettre in z:
            result=result
        elif lettre in u:
            result=result+1
        elif lettre in d:
            result=result+2
        elif lettre in t:
            result=result+3
        elif lettre in q:
            result=result+4
        elif lettre in h:
            result=result+8
        elif lettre in x:
            result=result+10
    return result


##



def sommetab(t):
    s=0
    for i in range (len(t)):
        s+=t[i]
    return s

##

def moyennetab(t):
    if len(t)==0:
        return None
    else:
        m=sommetab(t)/len(t)
        return m

##

def maxitab(t):
    if len(t)==0:
            return None
    m=t[0]
    for i in range (len(t)):
        if t[i]>m:
            m=t[i]
        else :
            m=m
    return m

##

def recherchetab(elt, tab):
    l=0
    if elt in tab:
        for i in range (len(tab)):
            if tab[i]==elt:
                return l
            else:
                l+=1
    else:
        return None

##

def swap2(tab, h, j):
    final=""
    u=h
    d=j
    if h or j in tab:
        for i in range (len(tab)):
            nbr=tab[i]
            if tab[i]==u:
                f+=d
            elif tab[h]==j:
                f+=h
            else:
                final=final+nbr
        return final
    return None

##

def frequencevoyelles():
    texte="Anton Voyl n'arrivait pas à dormir. Il alluma. Son Jaz marquait minuit vingt. Il poussa un profond soupir, s'assit dans son lit, s'appuyant sur son polochon. Il prit un roman, il l'ouvrit, il lut; mais il n'y saisissait qu'un imbroglio confus, il butait à tout instant sur un mot dont il ignorait la signification. Il abandonna son roman sur son lit. Il alla à son lavabo; il mouilla un gant qu'il passa sur son front, sur son cou. Son pouls battait trop fort. Il avait chaud. Il ouvrit son vasistas, scruta la nuit. Il faisait doux. Un bruit indistinct montait du faubourg. Un carillon, plus lourd qu'un glas, plus sourd qu'un tocsin, plus profond qu'un bourdon, non loin, sonna trois coups. Du canal Saint-Martin, un clapotis plaintif signalait un chaland qui passait. Sur l'abattant du vasistas, un animal au thorax indigo, à l'aiguillon safran, ni un cafard, ni un charançon, mais plutôt un artison, s'avançait, traînant un brin d'alfa. Il s'approcha, voulant l'aplatir d'un coup vif, mais l'animal prit son vol, disparaissant dans la nuit avant qu'il ait pu l'assaillir."
    voy="aei"
    compteur=0
    for i in range (len(texte)):
        lettre=texte[i]
        if lettre in voy:
            compteur+=1
        else:
            compteur=compteur
    result=compteur/len(texte)*100
    return result

##50 premiers multiples de 3

tab=[i*3 for i in range(50)]
print(tab)

##

mapping(f, tab):
    a=tab
    for i in range (len(tab)):
        caract=tab[i]
        if caract==f:










