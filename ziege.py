#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as ra
import argparse


def setra():
    return int(ra.uniform(1, 4))


def main(args):
    print("-----------------------")
    print("   Das Ziegenproblem   ")
    print("-----------------------")

    print("Der Moderator darf weder Auto- noch Wahltuer oeffnen")

    for l in range(0, args.trails):  # zehn versuche
        # counter r und f sind null
        r = 0  # wechseln richtig
        f = 0  # wechseln falsch

        for k in range(0, args.count):  # 1000 durchgaenge pro versuch
            a = setra()  # Zufall der Autotuer A
            w1 = setra()  # Zufaellige erstwahl
            m = setra()  # moderator will tuer m oeffnen

            while m == a or m == w1:  # m darf keine Autotuer oder die vom spieler gewaehlte  tuer sein
                m = setra()  # moderator will tuer m oeffnen

            w2 = 6-m-w1  # w2 ist die tuer, zu der nun gewaechselt wird

            if w2 == a:  # wenn w2 die autotuer ist, ein punkt fuer >>wechseln ist richtig<<
                r += 1
            elif w1 == a:  # wenn w1 die autotuer ist, ein punkt fuer >>wechseln ist falsch<<
                f += 1

        print("Wechseln richtig ", r, "\t Wechseln falsch ", f)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Darstellung des Ziegenbroblems')
    parser.add_argument(
        "-t", "--trails", help="wieviele Versuche sollen durchgefürht werden? Default ist 10", type=int, default=10)
    parser.add_argument(
        "-c", "--count", help="Wieviele durchläufe sind in einem Versuch zu machen? Default ist 1000", type=int, default=1000)

    args = parser.parse_args()

    main(args)
