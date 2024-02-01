def creerPileVide():
    return []

def empiler(element, Pile):
    Pile.append(element)

def depiler(Pile):
    return Pile.pop()

def est_vide(Pile):
    return Pile==[]

def priorite(operateur):
    if operateur == '**':
        return 3
    if operateur in {'*', '/'}:
        return 2
    if operateur in {'+','-'}:
        return 1
    return 0

def conv_postfixe(chaine):
    pileOp = []
    pileConv = []
    chaine = chaine.split(" ") #ne sert a rien
    for c in chaine:
        if c == "(":
            empiler(c,pileOp)
        elif c in {"+","-" ,"*","/","**"}:
            empiler(c,pileOp)
        elif c == ")":
            while pileOp !=  []:
                a = depiler(pileOp)
                if a in {"+","-","*","/","**"}:
                    res = priorite(a)
                    if res == 3:
                        empiler(a,pileConv)
                    elif res == 2:
                        empiler(a,pileConv)
                    elif res == 1:
                        empiler(a,pileConv)
        else:
            empiler(c,pileConv)
    return pileOp , pileConv

print(conv_postfixe("( 1 + ( 2 * 3 )"))

