from typing import List

def Clouser (LHS: List[str], RHS: List[str], At: str, list1: List[str], Atts: List[str],M_S: int) -> List[str]:

    #cheking first of all if the attribute or the set of attributes separited by a comma,
    #is already in the list1(closure list) and then add it to the list1 if it's not
    list3 = At.split(",")
    for k in range(0,len(list3)):
        if list3[k] not in list1:
            list1.append(list3[k])

    if At in LHS:
        index = LHS.index(At)
        list2 = RHS[index].split(",")
        if (RHS[index] in Atts) or (all(elem in Atts for elem in list2)):
            n = RHS[index].count(",")
            for i in range(0,n+1):
                if list2[i] not in list1:
                    list1.append(list2[i])
                    M_S =1

                list1 = Clouser(LHS, RHS, list2[i], list1, Atts, 2)
                x = len(list1)
                if (M_S == 1):
                    M_S = 2
                    for j in range(0,x):
                        if list1[j] != list2[i]:
                            if x == 1:
                                if ((list1[j] + "," + list2[i] != Atts) and (RHS, list2[i] + "," + list1[j])):
                                    list1 = Clouser(LHS, RHS, list1[j] + "," + list2[i], list1, Atts, 2)
                                    list1 = Clouser(LHS, RHS, list2[i] + "," + list1[j], list1, Atts, 2)

                            else:
                                if ((list1[j] + "," + list2[i] != Atts) and (RHS, list2[i] + "," + list1[j])):
                                    list1 = Clouser(LHS, RHS, list1[j] + "," + list2[i], list1, Atts, 2)
                                    list1 = Clouser(LHS, RHS, list2[i] + "," + list1[j], list1, Atts, 2)
                                    if j == 0:
                                        list1 = Clouser(LHS, RHS, list1[0] + "," + list2[i] + "," + list1[1], list1,
                                                        Atts, 2)
                                        list1 = Clouser(LHS, RHS, list1[0] + "," + list1[1] + "," + list2[i], list1,
                                                        Atts, 2)






    if At.find(",") != -1:
        n = At.count(",")
        tmp = At.split(",")
        for i in range(0,n+1):
            list1 = Clouser(LHS, RHS, tmp[i], list1, Atts, 2)

    if At.count(",")>1:
        n = At.count(",")
        tmp = At.split(",")
        for i in range(0,n+1):
            for j in range(0,n+1):
                if tmp[i] != tmp[j]:
                    list1 = Clouser(LHS, RHS, tmp[i] + "," + tmp[j], list1, Atts, 2)

    return list1


def keyCounter(LHS: List[str], RHS: List[str], list1: List[str], Atts: List[str]) -> List[str]:

    if len(Atts)==1:
        return Atts

    for i in range(0, len(Atts)):
        list1.clear()
        list_L = Clouser(LHS, RHS, Atts[i], list1, Atts, 1)
        if sorted(list_L) == sorted(Atts):
            return Atts[i].split(",")

    for i in range(0, len(Atts)):
        for j in range(0, len(Atts)):
            if Atts[i] != Atts[j]:
                list1.clear()
                list_L = Clouser(LHS, RHS, Atts[i] + "," + Atts[j], list1, Atts, 1)
                if sorted(list_L) == sorted(Atts):
                    return (Atts[i] + "," + Atts[j]).split(",")

    if len(Atts)>2:
        for i in range(0, len(Atts)):
            for j in range(0, len(Atts) - 2):
                list1.clear()
                if Atts[i] != Atts[j + 1] and Atts[i] != Atts[j + 2]:
                    list_L = Clouser(LHS, RHS, Atts[i] + "," + Atts[j + 1] + "," + Atts[j + 2], list1, Atts, 1)
                    if sorted(list_L) == sorted(Atts):
                        return (Atts[i] + "," + Atts[j + 1] + "," + Atts[j + 2]).split(",")

        for i in range(0, len(Atts)):
            for j in range(len(Atts)-1,-1,-1):
                for k in range(0,len(Atts)):
                    list1.clear()
                    if Atts[i] != Atts[j] and Atts[i] != Atts[k]:
                        list_L = Clouser(LHS, RHS, Atts[i] + "," + Atts[k] + "," + Atts[j], list1, Atts, 1)
                        if sorted(list_L) == sorted(Atts):
                            return (Atts[i] + "," + Atts[k] + "," + Atts[j]).split(",")

def BCNF_Dec (LHS: List[str],RHS: List[str],List_Key: List[str],Atts: List[str], i:int) :
    R = Atts

    ats1 = LHS[i].split(",")
    if sorted(List_Key) == sorted(ats1):
        if i+1 < len(LHS):
            return BCNF_Dec(LHS, RHS, List_Key, Atts, i + 1)
        else:
            return R
    else:
        ats2 = RHS[i].split(",")
        r1 = ats1 + ats2
        print("r:",r1)
        r2 = [x for x in R if x not in r1]
        r2.extend(ats1)
        print("r:",r2)
        if i + 1 < len(LHS):
            return BCNF_Dec(LHS,RHS,List_Key,r2, i + 1)
        else:
            return r2



#The main function ---------------------------------------------------------------------------------------

print("\t\t\t\t\t\t\t\t________________________________\n")
print(
        "______________________________________________ | Hello dear user | _______________________________________________")
print("\n\t\t\t\t\t\t\t\t\t\t\t     ________________________________")


while True :
    Nrelation = str(input("\nPlease enter the name of your relation : "))

    Atts = (input("\nEnter the attributes of your relation separated by a comma (,) : "))
    Atts = Atts.split(",")

    LHS = list(())
    RHS = list(())

    N = int(input("\nHow many functional dependencies are there in your relation? "))

    print("\nEnter the functional dependencies of your relationship in the form (X->Y): ")
    print("if there are 2 attributes on the same hand side please separate them with a comma (,)")
    for i in range(0, N):
        fds = input("\n\t\t\t\t\t\t\t\t")
        fds = fds.split("->")
        LHS.append(fds[0])
        RHS.append(fds[1])
        fds.clear()

    list7 = list(())
    list_key = keyCounter(LHS, RHS, list7, Atts)

    print("The key is :",list_key,"\n")

    print("The BCNF decomposition of the relation ","{",Nrelation,"}",":\n")
    BCNF_Dec(LHS,RHS,list_key,Atts,0)


    '''At = (input("\nEnter the specific attribute you want to calculate its closure: "))

    listX = list(())

    print(function(LHS, RHS, At, listX, Atts,1))
    print(
        "\n__________________________________________________________________________________________________________________")'''
    liiist = list(())
    print(keyCounter(LHS,RHS,liiist,Atts))
    choice = input("Do you want to repeat? (y/n) ")
    if choice.lower() == 'n':
        break