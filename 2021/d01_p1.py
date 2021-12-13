##Open file
#File
theInputFile = "d01_data.txt"

f = open(theInputFile, "r")
rowCntr = 0 #Helps determine the comparison between measurments
measurementIncrease = 0
for measurementValue in f:
  if ( rowCntr == 0 ): 
    prevValue = int(measurementValue)
  else:
    if ( int(measurementValue) > prevValue ): measurementIncrease += 1

  ##Using format
  #print('measurementValue: {} | prevValue: {} | increase: {}'.format(measurementValue, prevValue, measurementIncrease))

  #Current measurement is now the previous
  prevValue = int(measurementValue)
    
  rowCntr += 1

  #x=input("PAK...")

print('Increases: {}'.format(measurementIncrease))

f.close()

