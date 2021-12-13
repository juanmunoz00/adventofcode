##Open file
#File
theInputFile = "d01_data.txt"

rowCntr = 0 #Helps determine the comparison between measurments
measurementIncrease = 0
#list of measurments
Measurments = []
#howManyMeasurments = 0
#list of group of measurments
groupedMeasurments = []

f = open(theInputFile, "r")

for measurementValue in f:
  Measurments.append(int(measurementValue))

f.close()

measVal1 = 0
measVal2 = 0
measVal3 = 0
groupLimit = 0
groupedTotal = 0

prevValue = 0

print(Measurments)

for measurementValue in Measurments:
  groupLimit = rowCntr + 2
  if( groupLimit < len(Measurments) ): 
    #print('Measurments len: {} | Meas limit: {}'.format(len(Measurments), groupLimit))
    groupedTotal = Measurments[rowCntr] + Measurments[rowCntr + 1] + Measurments[rowCntr + 2]
    #print('grouped Sum: {}'.format(groupedTotal))
    
    groupedMeasurments.append(groupedTotal)
    print(groupedMeasurments)
    
    if ( rowCntr == 0 ): 
      prevValue = groupedTotal
    else:
      if ( int(groupedTotal) > prevValue ): measurementIncrease += 1
    print('groupedTotal: {} | prevValue: {} | increase: {}'.format(groupedTotal, prevValue, measurementIncrease))
    #groupOfThree.clear()
  else:
    break
    #print(groupedMeasurments[rowCntr])

  #Current measurement is now the previous
  prevValue = int(groupedTotal)

  print('Element: {}'.format(rowCntr))
  rowCntr +=1
  
  #x = input("PAK")

print("Done! \nQty of grouped increases: {}".format(measurementIncrease))
  

