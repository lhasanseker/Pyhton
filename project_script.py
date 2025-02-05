#!/usr/bin/env python
# coding: utf-8

listofModerator=["Okan Buruk","Mauro Icardi","Erden Timur"]
allPeople="Okan Buruk,Erden Timur,Fernando Muslera, Batuhan Şen, Günay Güvenç, Atakan Nuri Ordu, Ismail Jakobs, Davinson Sánchez, Kaan Ayhan, Elias Jelert, Abdülkerim Bardakcı, Ali Yeşilyurt, Metehan Baltacı, Eyüp Aydın, Roland Sallai, Kerem Demirbay, Lucas Torreira, Efe Akman, Yusuf Demir, Gökdeniz Gürpüz, Barış Alper Yılmaz,Mauro Icardi, Dries Mertens, Yunus Akgün, Berkan Kutlu, Sergio Oliveira, Victor Osimhen, Álvaro Morata"
secondlist=allPeople.split(",")
thirdset=set(secondlist)
listofPeople=list(thirdset)
numberofPeople=0
N=0
for people in listofPeople:
    if (len(people.split())==2):
        name=people.split()[0]
        surname=people.split()[1]
        if (listofModerator[0]==listofPeople[numberofPeople]):
            print("COACH {}".format(listofPeople[numberofPeople]))
            numberofPeople+=1
        elif(listofModerator[1]==listofPeople[numberofPeople]):
            print("CAPTAIN {}".format(listofPeople[numberofPeople]))
            numberofPeople+=1
        elif(listofModerator[2]==listofPeople[numberofPeople]):
            print("EXECUTIVE {}".format(listofPeople[numberofPeople]))
            numberofPeople+=1    
        else:
            numberofPeople+=1
            N+=1
            print("{}. Player Name: {}  Surname: {}".format(N, name, surname))
    else:    
        name=people.split()[0] + " " + people.split()[1]
        surname=people.split()[2]
        if (listofModerator[0]==listofPeople[numberofPeople]):
            print("COACH {}".format(listofPeople[numberofPeople]))
            numberofPeople+=1
        elif(listofModerator[1]==listofPeople[numberofPeople]):
            print("CAPTAIN {}".format(listofPeople[numberofPeople]))
            numberofPeople+=1
        elif(listofModerator[2]==listofPeople[numberofPeople]):
            print("EXECUTIVE {}".format(listofPeople[numberofPeople]))
            numberofPeople+=1    
        else:
            numberofPeople+=1
            N+=1
            print("{}. Player Name: {}  Surname: {}".format(N, name, surname))
