# arr = [5,7,8,3]

# def function(arr):
#     i = 0
#     s = 0

#     while int(i) < len(arr):
#         s = int(s) + int(arr[i])
#         i = i + 1

#     print(s)

# function(arr)

# def function(x,a,b,i,j):
#     k = int(j)
#     ct = 0

#     while int(k) > int(i)-1:
#         if int(x[k]) <= b and not (int(x[k]) <= a):
#             ct = int(ct) + 1
        
#         k = int(k) - 1
    
#     return ct

# x = [11,10,10,5,10,15,20,10,7,11]

# print(function(x,8,18,3,6))
# print(function(x,10,20,0,9))
# print(function(x,8,18,6,3))
# print(function(x,20,10,0,9))
# print(function(x,6,7,8,8))

# def g(s):
#     i = 0
#     new_str = ""

#     while int(i) < len(s) - 1:
#         new_str = new_str + s[i+1]
#         i = int(i) + 1
    
#     return new_str

# def f(s):
#     s = str(s)
#     if len(s) == 0:
#         return ""
#     elif len(s) == 1:
#         return s
#     else:
#         return f(g(s)) + s[0]

# def h(n,s):
#     while int(n) != 1:
#         if int(n) % 2 == 0:
#             n = int(n) / 2
#         else:
#             n = 3*int(n) + 1
        
#         s = f(s)
#     return s

# def p(x,y):
#     if int(y) == 0:
#         return 1
#     else:
#         return int(x) * p(int(x),int(y)-1)

# print(h(1, "fruits"))
# print(h(2, "fruits"))
# print(h(5, "fruits"))
# print(h(p(2, 1000000000000000), "fruits"))
# print(h(p(2, 9831050005000007), "fruits"))

import random

simulations = input()
teamWins = {"IG": 0, "Team Spirit": 0, "Secret": 0, "OG": 0, "PSG.LGD": 0, "T1": 0, "VP": 0, "VG": 0, "UND": 0, "Fnatic": 0, "QCY": 0, "Aster": 0, "bc": 0, "Alliance": 0, "EG": 0, "Elephant": 0}

for i in range(int(simulations)):
    ubRound1 = ["IG", "Team Spirit", "Secret", "OG", "PSG.LGD", "T1", "VP", "VG"]
    ubRound2 = []
    ubFinals = []
    grandFinals = []

    lbRound1 = ["UND", "Fnatic", "QCY", "Aster", "bc", "Alliance", "EG", "Elephant"]
    lbRound2 = []
    lbRound3= []
    lbRound4 = []
    lbRound5 = []
    lbFinals = []

    allTeams = ["IG", "Team Spirit", "Secret", "OG", "PSG.LGD", "T1", "VP", "VG", "UND", "Fnatic", "QCY", "Aster", "bc", "Alliance", "EG", "Elephant"]



    def match(team1, team2):
        print("")
        print(team1 + " vs " + team2)
        a = random.random()
        b = random.random()

        print(a)
        print(b)

        if a > b:
            if team1 in grandFinals:
                for i in allTeams:
                    if i == team1:
                        teamWins[i] += 1
                print(team1 + " has won the International 2021!")
            elif team1 in ubFinals:
                grandFinals.append(team1)
                print(team1 + " proceeds to the Grand Finals!")
                lbFinals.append(team2)
                print(team2 + " has been knocked down to the Lower Bracket Finals!")
            elif team1 in ubRound2:
                ubFinals.append(team1)
                print(team1 + " proceeds to the Upper Bracket Finals!")
                lbRound4.append(team2)
                print(team2 + " has been knocked down to Lower Bracket Round 4!")
            elif team1 in ubRound1:
                ubRound2.append(team1)
                print(team1 + " proceeds to Upper Bracket Round 2!")
                lbRound2.append(team2)
                print(team2 + " has been knocked down to Lower Bracket Round 2!")
            elif team1 in lbFinals:
                grandFinals.append(team1)
                print(team1 + " proceeds to the Grand Finals!")
            elif team1 in lbRound5:
                lbFinals.append(team1)
                print(team1 + " proceeds to the Lower Bracket Finals!")
            elif team1 in lbRound4:
                lbRound5.append(team1)
                print(team1 + " proceeds to Lower Bracket Round 5!")
            elif team1 in lbRound3:
                lbRound4.append(team1)
                print(team1 + " proceeds to Lower Bracket Round 4!")
            elif team1 in lbRound2:
                lbRound3.append(team1)
                print(team1 + " proceeds to Lower Bracket Round 3!")
            elif team1 in lbRound1:
                lbRound2.append(team1)
                print(team1 + " proceeds to Lower Bracket Round 2!")
            print(team1 + " wins!")
        else:
            if team2 in grandFinals:
                for i in allTeams:
                    if i == team2:
                        teamWins[i] += 1
                print(team2 + " has won the International 2021!")
            elif team2 in ubFinals:
                grandFinals.append(team2)
                print(team2 + " proceeds to the Grand Finals!")
                lbFinals.append(team1)
                print(team1 + " has been knocked down to the Lower Bracket Finals!")
            elif team2 in ubRound2:
                ubFinals.append(team2)
                print(team2 + " proceeds to the Upper Bracket Finals!")
                lbRound4.append(team1)
                print(team1 + " has been knocked down to Lower Bracket Round 4!")
            elif team2 in ubRound1:
                ubRound2.append(team2)
                print(team2 + " proceeds to Upper Bracket Round 2!")
                lbRound2.append(team1)
                print(team1 + " has been knocked down to Lower Bracket Round 2!")
            elif team2 in lbFinals:
                grandFinals.append(team2)
                print(team1 + " proceeds to the Grand Finals!")
            elif team2 in lbRound5:
                lbFinals.append(team2)
                print(team2 + " proceeds to the Lower Bracket Finals!")
            elif team2 in lbRound4:
                lbRound5.append(team2)
                print(team1 + " proceeds to Lower Bracket Round 5!")
            elif team2 in lbRound3:
                lbRound4.append(team2)
                print(team2 + " proceeds to Lower Bracket Round 4!")
            elif team2 in lbRound2:
                lbRound3.append(team2)
                print(team2 + " proceeds to Lower Bracket Round 3!")
            elif team2 in lbRound1:
                lbRound2.append(team2)
                print(team2 + " proceeds to Lower Bracket Round 2!")
            print(team2 + " wins!")

    print("--------------------------------------------------------------------")
    print("Simulation #" + str(int(i+1)))
    # ub
    # round 1
    match("IG","Team Spirit")
    match("Secret", "OG")
    match("PSG.LGD", "T1")
    match("VP", "VG")
    ubRound1 = []
    print("UB Round 2:")
    print(ubRound2)

    # round 2
    match(ubRound2[0], ubRound2[1])
    match(ubRound2[2], ubRound2[3])
    ubRound2 = []
    print("UB Finals:")
    print(ubFinals)

    # grand finals from ub
    match(ubFinals[0], ubFinals[1])
    ubFinals = []
    print("UB Finalist: ")
    print(grandFinals[0])

    # lb
    # round 1
    match("UND", "Fnatic")
    match("QCY", "Aster")
    match("bc", "Alliance")
    match("EG", "Elephant")
    lbRound1 = []
    print("LB Round 2:")
    print(lbRound2)

    # round 2
    match(lbRound2[0], lbRound2[4])
    match(lbRound2[1], lbRound2[5])
    match(lbRound2[2], lbRound2[6])
    match(lbRound2[3], lbRound2[7])
    print("LB Round 3:")
    print(lbRound3)

    # round 3
    match(lbRound3[0], lbRound3[1])
    match(lbRound3[2], lbRound3[3])
    lbRound3 = []
    print("LB Round 4:")
    print(lbRound4)

    # round4
    match(lbRound4[0], lbRound4[2])
    match(lbRound4[1], lbRound4[3])
    lbRound4 = []
    print("LB Round 5:")
    print(lbRound5)

    # round5
    match(lbRound5[0], lbRound5[1])
    lbRound5 = []
    print("LB Finals:")
    print(lbFinals)

    # lb finals
    match(lbFinals[0], lbFinals[1])
    lbFinals = []
    print("LB Finalist: ")
    print(grandFinals[1])

    # grand finals
    print("Grand Finals:")
    print(grandFinals)
    match(grandFinals[0], grandFinals[1])
    grandFinals = []

    print(teamWins)

finalList = []
counter = 0
print("---------------------------")
print("END OF SIMULATIONS.")
# print(teamWins)
values = list(teamWins.values())
keys =  list(teamWins.keys())

for value in values:
    finalList.append(str(keys[counter]) + " Wins:" + str(value))
    counter = int(counter) + 1

# print(finalList)

mostWins = max(values)
winPercentage = int(mostWins)/int(simulations)*100
counter2 = 0

for i in finalList:
    print(i)
print("")
for value in values:
    if value == mostWins:
        print("Team with the most wins: " + str(keys[counter2]) + " with " + str(value) + " wins out of " + simulations + "\n" + str(winPercentage) + " % win rate")
    counter2 = int(counter2) + 1

leastWins = min(values)
leastWinPercentage = int(leastWins)/int(simulations) * 100
counter3 = 0
for value in values:
    if value == leastWins:
        print("Team with the least wins: " + str(keys[counter3]) + " with " + str(value) + " wins out of " + simulations + "\n" + str(leastWinPercentage) + " % win rate")
    counter3 = int(counter3) + 1