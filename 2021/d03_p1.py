##Open file
#File
DEV = 1
PROD = 2
devMode = PROD

if( devMode == DEV ):
  theInputFile = "2021/d03_data_test.txt"
elif( devMode == PROD ):
  theInputFile = "2021/d03_data.txt"

firstBitPos = 0
#SecondBitPos = 0

firstBitValue = []
secondBitValue = []
thirdBitValue = []
fourthBitValue = []
fifthBitValue = []
sixthBitValue = []
seventhBitValue = []
eigthBitValue = []
ninethBitValue = []
tenthBitValue = []
eleventhBitValue = []

gammaRate = []
epsilonRate = []

#print('-------------------')
#print("MCb = most common bit")
#print('-------------------')

f = open(theInputFile, "r")
for allBits in f:
  strBits = str(allBits).strip()
  #print(allBits)

  msb = 0
  for strBit in strBits:
    bits = strBit.strip()
    #print(strBit)
    
    #0 1 2 3 4 5 6 7 8 9 A B
    #1 1 0 0 0 1 1 0 1 0 0 0
    if( msb == 0 ): firstBitValue.append(bits)
    if( msb == 1 ): secondBitValue.append(bits)
    if( msb == 2 ): thirdBitValue.append(bits)
    if( msb == 3 ): fourthBitValue.append(bits)
    if( msb == 4 ): fifthBitValue.append(bits)
    if( msb == 5 ): sixthBitValue.append(bits)
    if( msb == 6 ): seventhBitValue.append(bits)
    if( msb == 7 ): eigthBitValue.append(bits)
    if( msb == 8 ): ninethBitValue.append(bits)
    if( msb == 9 ): tenthBitValue.append(bits)
    if( msb == 10 ): eleventhBitValue.append(bits)

    msb += 1

zerosInFirstBit = int(firstBitValue.count("0"))
onesInFirstBit = int(firstBitValue.count("1"))

#print("Zeros in Bit 1: {}".format(zerosInFirstBit))
#print("Ones in Bit 1: {}".format(onesInFirstBit))
if( onesInFirstBit > zerosInFirstBit ): 
  #print("MCb in first bit is one")
  gammaRate.append(1)
  epsilonRate.append(0)
else:
  #print("MCb in first bit is zero")
  gammaRate.append(0)
  epsilonRate.append(1)
#print('-------------------')
zerosInSecondBit = int(secondBitValue.count("0"))
onesInSecondBit = int(secondBitValue.count("1"))
#print("Zeros in Bit 2: {}".format(zerosInSecondBit))
#print("Ones in Bit 2: {}".format(onesInSecondBit))
if( onesInSecondBit > zerosInSecondBit ): 
  #print("MCb in second bit is one")
  gammaRate.append(1)
  epsilonRate.append(0)
else:
  #print("MCb in second bit is zero")
  gammaRate.append(0)
  epsilonRate.append(1)
#print('-------------------')
zerosInThirdBit = int(thirdBitValue.count("0"))
onesInThirdBit = int(thirdBitValue.count("1"))
#print("Zeros in Bit 3: {}".format(zerosInThirdBit))
#print("Ones in Bit 3: {}".format(onesInThirdBit))
if( onesInThirdBit > zerosInThirdBit ): 
  #print("MCb in third bit is one")
  gammaRate.append(1)
  epsilonRate.append(0)
else:
  #print("MCb in third bit is zero")
  gammaRate.append(0)
  epsilonRate.append(1)
#print('-------------------')
zerosInFourthBit = int(fourthBitValue.count("0"))
onesInFourthBit = int(fourthBitValue.count("1"))
#print("Zeros in Bit 4: {}".format(zerosInFourthBit))
#print("Ones in Bit 4: {}".format(onesInFourthBit))
if( onesInFourthBit > zerosInFourthBit ): 
  #print("MCb in fourth bit is one")
  gammaRate.append(1)
  epsilonRate.append(0)
else:
  #print("MCb in fourth bit is zero")
  gammaRate.append(0)
  epsilonRate.append(1)
#print('-------------------')
zerosInFifthBit = int(fifthBitValue.count("0"))
onesInFifthBit = int(fifthBitValue.count("1"))
#print("Zeros in Bit 5: {}".format(zerosInFifthBit))
#print("Ones in Bit 5: {}".format(onesInFifthBit))
if( onesInFifthBit > zerosInFifthBit ): 
  #print("MCb in fifth bit is one")
  gammaRate.append(1)
  epsilonRate.append(0)
else:
  #print("MCb in fifth bit is zero")
  gammaRate.append(0)
  epsilonRate.append(1)
#print('-------------------')
#print("Gamma Rate: " + str(gammaRate))
_gammaRate = (str(gammaRate[0]) + str(gammaRate[1]) + str(gammaRate[2]) + str(gammaRate[3]) + str(gammaRate[4]).strip())
print("Gamma Rate: " + _gammaRate)
decimalGammaRate = int(_gammaRate,2)
print("Gamma Rate in decimal: {}".format(decimalGammaRate))

_epsilonRate = (str(epsilonRate[0]) + str(epsilonRate[1]) + str(epsilonRate[2]) + str(epsilonRate[3]) + str(epsilonRate[4]).strip())
print("Epsilon Rate: " + _epsilonRate)
decimalEpsilonRate = int(_epsilonRate,2)
print("Epsilon Rate in decimal: {}".format(decimalEpsilonRate))

powerConsumption = decimalGammaRate * decimalEpsilonRate
print("Power Consumption: {}".format(powerConsumption))

f.close()