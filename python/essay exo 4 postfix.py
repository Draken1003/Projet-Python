def conv_postfixe(chaine):
    pileOp = []
    pileConv = []
    chaine.split() #ne sert a rien
    for c in chaine:
        if c == "(":
            pileOp.append(c)
        elif c in {"+","-" ,"*","/"}:
            pileOp.append(c)
        elif c == ")":
            while pileOp !=  []:
                a = pileOp.pop()
                if a in {"+","-","*","/","**"}:
                    pileConv.append(a)
        else:
            pileConv.append(c)
    return pileOp , pileConv

print(conv_postfixe("((5*3)+4)**2)"))
