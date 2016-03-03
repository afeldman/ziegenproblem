#!/usr/bin/python

import random as ra


def setra():
    #ra.seed()
    #return int(3 * ra.random() + 1.0)
    return int(ra.uniform(1,4))

def main():
    print("-----------------------")
    print("   Das Ziegenproblem   ")
    print("-----------------------")

    print("Der Moderator darf weder Auto- noch Wahltuer oeffnen")

    for l in range(0, 10):#zehn versuche
        #counter r und f sind null
        r = 0 #wechseln richtig
        f = 0 #wechseln falsch

        for k in range(0,1000): #1000 durchgaenge pro versuch
            a=setra() #Zufall der Autotuer A
            w1=setra() #Zufaellige erstwahl
            m=setra() #moderator will tuer m oeffnen 

            while m == a or m == w1: #m darf keine Autotuer oder die vom spieler gewaehlte  tuer sein
                m=setra() #moderator will tuer m oeffnen            
        
            w2=6-m-w1 #w2 ist die tuer, zu der nun gewaechselt wird
                    
            if w2 == a: #wenn w2 die autotuer ist, ein punkt fuer >>wechseln ist richtig<<
                r += 1
            elif w1 == a: #wenn w1 die autotuer ist, ein punkt fuer >>wechseln ist falsch<<
                f += 1

        print "Wechseln richtig " ,r, "\t Wechseln falsch " ,f


if __name__ == "__main__":
    main()
