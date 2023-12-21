import csv
 
def Add():
    try:
        with open("NBATeamDatabase.csv", "r+", newline="") as NTB:
            a = csv.writer(NTB)
            b = csv.reader(NTB)
            c = []
            while True:
                i = int(input("Enter Team Number: "))
                while True:
                    for l in b:
                        if l[0] == i:
                            print("Team Number already taken. Enter different Team Number")
                            i = int(input("Enter Team Number: "))
                            break
                    else:
                        break
                j = input("Enter Team Name: ")
                k = input("Enter Team City: ")
                m = input("Enter Team coach: ")
                c.append([i,j,k,m])
                Q = input("Wanna Continue? ")
                if Q.lower() == "n" or Q.lower() == "no":
                    break
            a.writerows(c)
    except FileNotFoundError:
        with open("NBATeamDatabase.csv", "w") as NTB:
            a = csv.writer(NTB)
            c = []
            while True:
                i = int(input("Enter Team Number: "))
                while True:
                    for l in c:
                        if l[0] == i:
                            print("Team Number already taken. Enter different Team Number")
                            i = int(input("Enter Team Number: "))
                            break
                    else:
                        break
                j = input("Enter Team Name: ")
                k = input("Enter Team City: ")
                m = input("Enter Team Coach: ")
                c.append([i,j,k,m])
                Q = input("Wanna Continue? ")
                if Q.lower() == "n" or Q.lower() == "no":
                    break
            a.writerows(c)
 
def Search(): #Searches a team by its various attributes
    try:
        with open("NBATeamDatabase.csv") as NTB:
            b = csv.reader(NTB)
            while True:
                i = input("Enter criteria of Search(Team Number/Team Name/City/Coach)")
                if i.lower() == "tno" or i.lower() == "t" or i.lower() == "teamnumber" or i.lower() == "teamno." or i.lower() == "no." or i.lower() == "teamno" or i.lower() == "team number":
                    j = int(input("Enter Team number: ")) 
                    for k in b:
                        if j == k[0]:
                            print(k)
                            break
                elif i.lower() == "team name" or i.lower() == "t" or i.lower() == "teamname" or i.lower() == "name" or i.lower() == "tname":
                    j = input("Enter Team Name: ")
                    for k in b:
                        if j.lower() == k[1].lower():
                            print(k)
                elif i.lower() == "city" or i.lower() == "teamcity" or i.lower() == "team city" or i.lower() == "tcity":
                    j = input("Enter Team City: ")
                    for k in b:
                        if j.lower() == k[2].lower():
                            print(k)
                elif i.lower() == "coach" or i.lower() == "teamcoach" or i.lower() == "team coach" or i.lower() == "tcoach":
                    j = input("Enter Team Coach: ")
                    for k in b:
                        if j.lower() == k[3].lower():
                            print(k)
                else:
                    print("Invalid Option")
                Q = input("Wanna Continue? ")
                if Q.lower() == 'n' or Q.lower() == "no":
                    break
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
def Count(): #Counts and returns the no. of teams playing for the same city
    try:
        with open("NBATeamDatabase.csv") as NTB:
            b = csv.reader(NTB)
            while True:
                i = input("Enter City: ")
                n = 0
                for k in b:
                    if i.lower() == k[2].lower():
                        n += 1
                print("No. of Teams of City",i,"are",n)
                Q = input("Wanna Continue? ")
                if Q.lower() == 'n' or Q.lower() == "no":
                    break
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
def Arrange(): #Sorts the team in the ascending order on the basis of team name
    try:
        a=[]
        with open("NBATeamDatabase.csv", "r") as NTB:
            b = csv.reader(NTB)
            for k in b:
              a.append(k)
            n = len(a)  
            for i in range(n-1):  
                for j in range(0, n-i-1): 
                    if a[j][1] > a[j+1][1]: 
                        a[j], a[j+1] = a[j+1], a[j]
        with open("NBATeamDatabase.csv", "w") as NTB:
          b = csv.writer(NTB)
          b.writerows(a) 
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
def View(): #Displays all teams
    try:
        with open("NBATeamDatabase.csv") as NTB:
            b = csv.reader(NTB)
            for k in b:
                print(k)
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
def Transfer(): #Transfers the teams belonging to a single city in another database
    try:
        c=[]
        with open("NBATeamDatabase.csv") as NTB:
            b = csv.reader(NTB)
            a = input("Enter City Name: ")
            for k in b:
                if k[2].lower == a:
                    c.append(k)
        with open("City having multiple teams.csv", 'a') as F:
            d = csv.writer(F)
            d.writerows(c)
        print("All teams having city",a,"can be found in \"City having multiple teams.csv\" Database")
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
def Modify(): #Allows the user to modify coaches
    try:
        a=[]
        with open("NBATeamDatabase.csv", "r") as NTB:
            b = csv.reader(NTB)
            while True:
                c = 0
                i = int(input("Enter Team Number: "))
                for j in b:
                    if j[0] == i:
                        a.append(j)
                        print("Present Coach:",a[c][3])
                        k = input("Enter New Coach: ")
                        a[c][3] = k
                        print(a[c])
                Q = input("Wanna Continue? ")
                if Q.lower() == "n" or Q.lower() == "no":
                    break
                else:
                    c +=1
        with open("NBATeamDatabase.csv", "w") as NTB:
          b = csv.writer(NTB)
          b.writerows(a)
          
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
def Open(): #Shows the information about players of a particular team and allows the user to perform operations on them
    try:
        with open("NBATeamDatabase.csv", "r") as NTB:
            z = list(csv.reader(NTB))
            w = 0
            print(z)
            while True:
                OPT = None
                y = str(input("Enter Team Number: "))
                try:
                    while True:
                        if z[w][0] == y:
                            x = z[w][1]
                            x += ".csv"
                            def AddPlayers(): #Adds a new player
                                try:
                                    with open(x, "r+", newline="") as NPB:
                                        a = csv.writer(NPB)
                                        b = csv.reader(NPB)
                                        c = []
                                        while True:
                                            i = input("Enter Player ID: ")
                                            while True:
                                                for l in b:
                                                    if l[0] == i:
                                                        print("Player ID already taken. Enter different Player ID")
                                                        i = input("Enter Player ID: ")
                                                        break
                                                else:
                                                    break
                                            j = input("Enter Player Name: ")
                                            k = input("Enter Player Position: ")
                                            m = float(input("Enter Player Skill Level(out of 10): "))
                                            while True:
                                                if m/10 > 1:
                                                    m = float(input("Enter Player Skill Level(out of 10): "))
                                                else:
                                                    break
                                            c.append([i,j,k,m/10])
                                            Q = input("Wanna Continue? ")
                                            if Q.lower() == "n" or Q.lower() == "no":
                                                break
                                        a.writerows(c)
                                except FileNotFoundError:
                                    with open(x, "w") as NPB:
                                        a = csv.writer(NPB)
                                        c = []
                                        while True:
                                            i = input("Enter Player ID: ")
                                            while True:
                                                for l in c:
                                                    if l[0] == i:
                                                        print("Player ID already taken. Enter different Player ID")
                                                        i = input("Enter Player ID: ")
                                                        break
                                                else:
                                                    break
                                            j = input("Enter Player Name: ")
                                            k = input("Enter Player Position: ")
                                            m = float(input("Enter Player Skill Level: "))
                                            c.append([i,j,k,m])
                                            Q = input("Wanna Continue? ")
                                            if Q.lower() == "n" or Q.lower() == "no":
                                                break
                                        a.writerows(c)
 
                            def SearchPlayers(): #Searches and shows players on the basis of the attribute selected by the user
                                try:
                                    with open(x) as NPB:
                                        b = csv.reader(NPB)
                                        while True:
                                            i = input("Enter criteria of Search(Player ID/Player Name/Position/Skill Level)")
                                            if i.lower() == "pid" or i.lower() == "id" or i.lower() == "playerid" or i.lower() == "player id":
                                                j = input("Enter Player ID: ") 
                                                for k in b:
                                                    if j.lower() == k[0].lower():
                                                        print(k)
                                                        break
                                            elif i.lower() == "player name" or i.lower() == "p" or i.lower() == "playername" or i.lower() == "name" or i.lower() == "pn":
                                                j = input("Enter Player Name: ")
                                                for k in b:
                                                    if j.lower() == k[1].lower():
                                                        print(k)
                                            elif i.lower() == "position" or i.lower() == "p" or i.lower() == "playerposition" or i.lower() == "player position" or i.lower() == "pp":
                                                j = input("Enter Player Position: ")
                                                for k in b:
                                                    if j.lower() == k[2].lower():
                                                        print(k)
                                            elif i.lower() == "skill level" or i.lower() == "s" or i.lower() == "playerskill level" or i.lower() == "player Skill level" or i.lower() == "psl" or i.lower() == "skill" or i.lower() == "sl":
                                                j = float(input("Enter Player Skill Level: "))
                                                for k in b:
                                                    if j == k[3]:
                                                        print(k)
                                            else:
                                                print("Invalid Option")
                                            Q = input("Wanna Continue? ")
                                            if Q.lower() == 'n' or Q.lower() == "no":
                                                break
                                except FileNotFoundError:
                                    print(x, "does not exist")
 
                            def CountSkillLevelPlayers(): #Counts the no. of players having the mentioned skill level
                                try:
                                    with open(x) as NPB:
                                        b = csv.reader(NPB)
                                        a = []
                                        while True:
                                            i = float(input("Enter Player Skill Level: "))
                                            n = 0
                                            for k in b:
                                                if i == float(k[3]):
                                                    n += 1
                                                    a.append(k)
                                            print("No. of Players of Skill Level",i,"are",n)
                                            c = input("Want to see their information?")
                                            if c.lower() == "y" or c.lower() == "yes" or c.lower() == "ye":
                                                for d in a:
                                                    print(d)
                                            Q = input("Wanna Continue? ")
                                            if Q.lower() == 'n' or Q.lower() == "no":
                                                break
                                except FileNotFoundError:
                                    print(x, "does not exist")
 
                            def ArrangePlayers(): #Players are arranged on the basis of their Names
                                try:
                                    a=[]
                                    with open(x, "r") as NPB:
                                        b = csv.reader(NPB)
                                        for k in b:
                                            a.append(k)
                                            n = len(a)  
                                            for i in range(n-1):  
                                                for j in range(0, n-i-1): 
                                                    if a[j][1] > a[j+1][1]: 
                                                        a[j], a[j+1] = a[j+1], a[j]
                                    with open(x, "w") as NPB:
                                        b = csv.writer(NPB)
                                        b.writerows(a) 
                                except FileNotFoundError:
                                    print(x, "does not exist")
 
                            def ViewPlayers():
                                try:
                                    with open(x) as NPB:
                                        b = csv.reader(NPB)
                                        for k in b:
                                            print(k)
                                except FileNotFoundError:
                                    print(x, "does not exist")
 
                            def TransferPlayer(): #Transfers the players having skill set above a particular no. to a new csv file
                                try:
                                    c=[]
                                    with open(x) as NPB:
                                        b = csv.reader(NPB)
                                        v = float(input("Enter Skill level: "))
                                        for k in b:
                                            if round(float(k[3]),1) >= v:
                                                c.append(k)
                                    with open("Selected.csv", 'a') as F:
                                        d = csv.writer(F)
                                        d.writerows(c)
                                    print("A new CSV file with name \"Selected.csv\" has been created with players above or equal to skill level of 0.7")
                                except FileNotFoundError:
                                    print(x, "does not exist")
 
                            def ModifyPlayers():  #Allows the user to change skill level for a player
                                try:
                                    a=[]
                                    with open(x, "r") as NPB:
                                        b = csv.reader(NPB)
                                        while True:
                                            c = 0
                                            i = input("Enter Player ID: ")
                                            for j in b:
                                                if j[0] == i:
                                                    a.append(j)
                                                    print("Present", j[1], "Skill Level:",a[c][3])
                                                    k = float(input("Enter New Skill Level for", j[1], "(out of 10): "))
                                                    a[c][3] = k/10
                                                    print(a[c])
                                            Q = input("Wanna Continue? ")
                                            if Q.lower() == "n" or Q.lower() == "no":
                                                break
                                            else:
                                                c +=1
                                    with open(x, "w") as NPB:
                                        b = csv.writer(NPB)
                                        b.writerows(a)
                                    
                                except FileNotFoundError:
                                    print(x, "does not exist")
 
                            while True:
                                OPT=input("You are in "+(x[0:-4])+" Team's Database\n"+"AP: Add Player\nVP: View Players\nSP: Search Players\nTP: Transfer Players\nCP: Count Players above a particular skill level\nARP: Arrange Players:\nMP: Modify Player\nRM: Return to Previous Menu")
                                if OPT.lower() == 'ap':
                                    AddPlayers()
                                elif OPT.lower() == 'vp':
                                    ViewPlayers()
                                elif OPT.lower() == 'sp':
                                    SearchPlayers()
                                elif OPT.lower() == 'tp':
                                    TransferPlayer()
                                elif OPT.lower() == "cp":
                                    CountSkillLevelPlayers()
                                elif OPT.lower() == "arp":
                                    ArrangePlayers()
                                elif OPT.lower() == "mp":
                                    ModifyPlayers()
                                elif OPT.lower() == 'rm':
                                    print("Thanks for visiting",(x[0:-4]),"Database")
                                    break
                                else:
                                    print("Invalid Option... ReTry!!!")
                        w += 1
                        if OPT == "rm":
                           break
                except  IndexError:
                    print("No such Entry exists")
                break
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")
 
''' 
def OpenInjuriesDatabase():
    try:
        with open(x, "r") as NPB:
            z = list(csv.reader(NPB))
            w = 0
            print(z)
            while True:
                OPT = None
                m = str(input("Enter Team Number: "))
                try:
                    while True:
                        if z[w][0] == m:
                            y = z[w][0]
                            y += ".csv"
                            def AddInjury(): 
                                try:
                                    with open(y, "r+", newline="") as NIB:
                                        a = csv.writer(NIB)
                                        b = csv.reader(NIB)
                                        c = []
                                        while True:
                                            ID = input("Enter Player ID: ")
                                            while True:
                                                for l in b:
                                                    if l[0] == ID:
                                                        print("This Player ID has already been taken please,enter different Player ID")
                                                        ID = input("Enter Player ID: ")
                                                        break
                                                else:
                                                    break
                                        
                                            
                                            Itype = input("Enter type of injury: ")
                                            Rtime= int(input("Enter the recovery time:"))
                                            Cost= int(input("Enter the cost of treatment:"))
                                            c.append([ID,Itype,Rtime, Cost])
                                            Choice=("More?")
                                            if Choice.lower() == "n" or Choice.lower() == "no":
                                                break
                                        a.writerows(c)
                                except FileNotFoundError:
                                    with open(y, "w") as NIB:
                                        a = csv.writer(NIB)
                                        c = []
                                        while True:
                                            i = input("Enter Player ID: ")
                                            while True:
                                                for l in b:
                                                    if l[0] == i:
                                                        print("This Player ID has already been taken please,enter different Player ID")
                                                        i = input("Enter Player ID: ")
                                                        break
                                                else:
                                                    break
 
                                            ID = int(input("Enter Player ID: "))
                                            Itype = input("Enter type of injury: ")
                                            Rtime= int(input("Enter the recovery time:"))
                                            Cost= int(input("Enter the cost of treatment:"))
                                            c.append([ID,Itype,Rtime, Cost])
                                            Choice=("More?")
                                            if Choice.lower() == "n" or Choice.lower() == "no":
                                                break
                                        a.writerows(c)
                            def SearchPlayersInjuries(): 
                                try:
                                    with open(y,"r",newline="") as NIB:
                                        b = csv.reader(NIB)
                                        while True:
                                            i = input("Enter criteria of Search(Player ID/Player Injury)")
                                            if i.lower() == "pid" or i.lower() == "id" or i.lower() == "playerid" or i.lower() == "player id":
                                                j = input("Enter Player ID: ") 
                                                for k in b:
                                                    if j == k[0]:
                                                        print(k)
                                                        break
                                            elif i.lower() == "Player Injury" or i.lower() == "injurytype" or i.lower() == "playerinjury" or i.lower() == "injury" or i.lower() == "in":
                                                j = input("Enter the type of injury: ")
                                                for k in b:
                                                    if j.lower() == k[1].lower():
                                                        print(k)
                                        
                                            else:
                                                print("Invalid Option")
                                            Choice = input("Wanna Continue? ")
                                            if Choice.lower() == 'n' or Choice.lower() == "no":
                                                break
                                except FileNotFoundError:
                                    print("Database or File not found")
                                    
                            def ViewPlayerinjuries():
                                try:
                                    with open(y,"r",newline="") as NIB:
                                        b = csv.reader(NIB)
                                        for k in b:
                                            print(k)
                                except FileNotFoundError:
                                    print("Database or File not found")
 
                            def ArrangeInjuredPlayers():
                                try:
                                    a=[]
                                    with open(y,"r",newline="") as NIB:
                                        b = csv.reader(NIB)
                                        for k in b:
                                            a.append(k)
                                            n = len(a)  
                                            for i in range(n-1):  
                                                for j in range(0, n-i-1): 
                                                    if a[j][1] > a[j+1][1]: 
                                                        a[j], a[j+1] = a[j+1], a[j]
                                    with open(y,"w",newline="") as NIB:
                                        b = csv.writer(NIB)
                                        b.writerows(a) 
                                except FileNotFoundError:
                                    print("Database or File not found")
 
                            def ModifyInjuredPlayers():  
                                try:
                                    a=[]
                                    with open(y,"r",newline="") as NIB:
                                        b = csv.reader(NIB)
                                        while True:
                                            c = 0
                                            i = input("Enter Player ID: ")
                                            for j in b:
                                                if j[0] == i:
                                                    a.append(j)
                                                    print("Present", j[0], "Recovery time",a[c][2])
                                                    k = float(input("Enter new recovery time for", j[0], ": "))
                                                    a[c][2] = k
                                                    print(a[c])
                                            Choice= input("Wanna Continue? ")
                                            if Choice.lower() == "n" or Choice.lower() == "no":
                                                break
                                            else:
                                                c +=1
                                    with open(y, "w", newline="",) as NIB:
                                        b = csv.writer(NIB)
                                        b.writerows(a)
                                    
                                except FileNotFoundError:
                                    print("Database or File not found")
                            def TransferInjuredPlayer(): 
                                try:
                                    c=[]
                                    with open(y,"r",newline="") as NIB:
                                        b = csv.reader(NPB)
                                        for k in b:
                                            if round(k[3],1) >=3500:
                                                c.append(k)
                                    with open("Costly.csv", 'a') as File:
                                        d = csv.writer(File)
                                        d.writerows(c)
                                    print("A new CSV file with name \"Costly.csv\" has been created with players whose injuries cost $3500")
                                except FileNotFoundError:
                                    print("Database or File not found")
 
                        
                            def DeleteInjuredPlayers():
                                try:
                                    with open(y,"r",newline="") as NIB:
                                        b = csv.reader(NIB)
                                        i=int(input("Enter the player ID that needs to be deleted:"))
                                        for k in b:
                                            if i == k[0]:
                                                b.remove(k)
                                            else:
                                                print("Sorry that ID does not exist!")     
                                    with open(y,"w",newline="") as NIB:
                                            c = csv.writer(NIB)
                                            c.writerows(b) 
                                except FileNotFoundError:
                                    print("Database or File not found")
 
                            while True: 
                                OPT=input("You are in "+(y[0:-4])+"A:Add Injury\nV:View Player Injuries\nO:View information About the player injuries\nS:Search Player Injuries\nT:Transfer Injured Player\nAr:Arrange Injured Players\nM:Modify Injured Players\nQ:Quit")
                                if OPT.lower()=='a':
                                    Add()
                                elif OPT.lower()=='v':
                                    View()
                                elif OPT.lower()=='o':
                                    Open()
                                elif OPT.lower()=='s':
                                    Search()
                                elif OPT.lower()=='t':
                                    Transfer()
                                elif OPT.lower()=="ar":
                                    Arrange()
                                elif OPT.lower()=="m":
                                    Modify()
                                elif OPT.lower()=='q':
                                    print("Thanks!")
                                    break
                                else:
                                    print("Invalid Option... ReTry!!!")
                        w += 1
                        if OPT == "rm":
                           break
                except  IndexError:
                    print("No such Entry exists")
                break
    except FileNotFoundError:
        print("NBA Team Database.csv does not exist")   
 
                                 
while True: # Main code
    OPT=input("A:Add Teams\nV:View Teams\nO:View information About the team\nS:Search Team\nT:Transfer Teams\nC:Count Team\nAr:Arrange Teams\nM:Modify Teams\nI:View Injured Players\nQ:Quit ")
    if OPT.lower()=='a':
        Add()
    elif OPT.lower()=='v':
        View()
    elif OPT.lower()=='o':
        Open()
    elif OPT.lower()=='s':
        Search()
    elif OPT.lower()=='t':
        Transfer()
    elif OPT.lower()=="c":
        Count()
    elif OPT.lower()=="ar":
        Arrange()
    elif OPT.lower()=="m":
        Modify()
    elif OPT.lower()=="i":
        OpenInjuriesDatabase()
    elif OPT.lower()=='q':
        print("Thanks!")
        break
    else:
        print("Invalid Option... ReTry!!!")              
'''