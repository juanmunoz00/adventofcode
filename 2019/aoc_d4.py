from collections import defaultdict
from datetime import datetime
import operator

#Open the file of the input data.
filepath = 'C:/'
filename = 'input_d04.txt'
complete_filepathname = filepath+filename
print('Opening from '+complete_filepathname)

lines = open(complete_filepathname).read().split('\n')
lines.sort()

#Create dictionaries to handle data.
dictguardMinuteswhenfallasleep = defaultdict(int)
dictguardMinutesasleep = defaultdict(int)
def analyze_data():
    totalminutesAsleep = 0
    guardID = 0

    for line in lines:
        #get the date and guard's ID.
        dateTime=line[1:17]
        guardActivity=str(line[19:len(line)])

        #Determine guard's activity to cont the naps (sleep) based on the guard's activity.
        if 'begins shift' in guardActivity:        
            if(guardID>0):
                sleptRpt = str(totalminutesAsleep)
                totalminutesAsleep = 0                           

            guardID = int(line.split()[3][1:])

        #When a guard is sleep, the id and minutes are stored in the dictionaries.
        if 'falls asleep' in guardActivity:
            fallsAsleep = int(dateTime[14:16])
            dictguardMinuteswhenfallasleep[guardID,fallsAsleep] += 1
            dictguardMinutesasleep[guardID] += 1

        if 'wakes up' in guardActivity:
            wakesUp = int(dateTime[14:16])
            totalAsleep = int(wakesUp-fallsAsleep)   

            totalminutesAsleep += totalAsleep

#Determine the minute most asleep per guard ID.        
def minute_most_asleep():       
    minMostasleep = max(dictguardMinuteswhenfallasleep.items(), key=operator.itemgetter(1))[0]
    strbestMin=str(minMostasleep)
    bestMincommachar=strbestMin.find(',')

    minStart=int(bestMincommachar+1)
    minFinish=int(len(strbestMin)-1)
    bestMin=strbestMin[minStart:minFinish]
	
    return bestMin

#Determine the guard with more minutes asleep acumulated.
def guard_with_more_minutes_asleep():
    return int(max(dictguardMinutesasleep.items(), key=operator.itemgetter(1))[0])


#Run analysis
analyze_data()
bestmin = minute_most_asleep()
bestguard = guard_with_more_minutes_asleep()
print('Most minutes asleep of a Guard: '+str(bestmin))    
print('Guard with most minutes asleep: '+str(bestguard))

#The ID of the guard you chose multiplied by the minute.
print('ID of the guard times the most minutes: '+str((int(bestguard))*(int(bestmin))))