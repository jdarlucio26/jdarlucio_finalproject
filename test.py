import csv, requests, bs4, sqlite3, re, datetime, schedule, time

db = sqlite3.connect('DisneyWorld_Rides.db')
print "Opened database successfully"

cur = db.cursor()

cur.executescript('''DROP TABLE IF EXISTS Rides;
CREATE TABLE IF NOT EXISTS Rides (ID INTEGER PRIMARY KEY AUTOINCREMENT, PARKNAME TEXT NOT NULL, SCRAPTIME TEXT NOT NULL, 
                                  RIDENAME TEXT NOT NULL, LOCATION TEXT NOT NULL,
                                  TIME INTEGER NOT NULL)''')

print ("Table created successfully")=


GoodRidesFile = open('goodRides.csv')
GoodRidesReader = csv.reader(GoodRidesFile)
lst_GoodRides = []

for ride in GoodRidesReader:
    lst_GoodRides.extend(ride)

lst_GoodRides_Epcot = ['Soarin\'', 'Frozen Ever After', 'Spaceship Earth', 'Test Track Presented by Chevrolet', 
                   'Gran Fiesta Tour Starring The Three Caballeros', 'The Seas with Nemo & Friends',
                   'Mission: SPACE', 'Living with the Land', 'The Sum of All Thrills'] #made using a list from internet
lst_GoodRides.extend(lst_GoodRides_Epcot)

def Scrapping(ride):

    WebAddress = "http://www.easywdw.com/waits/?&park="+ride+"&showOther=true"
    myPage = requests.get(WebAddress)
    mysoup = bs4.BeautifulSoup(myPage.content,"lxml")
    lstRides = []
    PageTable = mysoup.find('table')
    RidesRows = PageTable.findAll('tr')
    
    #print RidesRows
    for Rides in RidesRows[1:]:
        RideDetail = Rides.findAll('td')
#        print RideDetail
        RideName = RideDetail[0].getText()
        #print RideName
        if RideName in lst_GoodRides:
            RideLocation = RideDetail[1].getText()
            
            RideTime = re.findall('\d+',RideDetail[2].getText())   
            if not RideTime: #If Ride Time is blank set Time to 0
                RideTime = 0
            else:
                RideTime = int(re.findall('\d+',RideDetail[2].getText())[0])
            
            if ride == "mk":
                RideTuple = ("Magic Kingdom",datetime.datetime.now(),RideName,RideLocation,RideTime)
            else:
                RideTuple = ("Epcot",datetime.datetime.now(),RideName,RideLocation,RideTime)
            
            lstRides.append(RideTuple)
       
    
    cur.executemany(''' INSERT INTO Rides (PARKNAME, SCRAPTIME, RIDENAME, LOCATION, TIME) VALUES (?,?,?,?,?) ''', lstRides)
    db.commit()
    
    print ("Scrapped Rides in: ") + ride
    
    return


schedule.every(15).minutes.do(Scrapping,ride="mk")
schedule.every(15).minutes.do(Scrapping,ride="ep")

while 1:
    schedule.run_pending()
    time.sleep(1)