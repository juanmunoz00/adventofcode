##Open file
#File
DEV = 1
PROD = 2
devMode = DEV

if( devMode == DEV ):
  theInputFile = "2021/d03_data_test1.txt"
elif( devMode == PROD ):
  theInputFile = "2021/d03_data.txt"

#firstBitPos = 0
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

bitsPerRow = 11

gammaRate = []
epsilonRate = []

def GetMCbAndLCB(onesInBit, zerosInBit, bit):
  if( onesInBit > zerosInBit ): 
    print("MCb in bit {} is one".format(bit))
    gammaRate.append(1)
    epsilonRate.append(0)
  else:
    print("LCb in bit {} is zero".format(bit))
    gammaRate.append(0)
    epsilonRate.append(1)  

def GetRates():

  GetMCbAndLCB(int(firstBitValue.count("1")),int(firstBitValue.count("0")), 1)
  GetMCbAndLCB(int(secondBitValue.count("1")),int(secondBitValue.count("0")), 2)
  GetMCbAndLCB(int(thirdBitValue.count("1")),int(thirdBitValue.count("0")), 3)  
  GetMCbAndLCB(int(fourthBitValue.count("1")),int(fourthBitValue.count("0")), 4)
  GetMCbAndLCB(int(fifthBitValue.count("1")),int(fifthBitValue.count("0")), 5)
  GetMCbAndLCB(int(sixthBitValue.count("1")),int(sixthBitValue.count("0")), 6)
  GetMCbAndLCB(int(seventhBitValue.count("1")),int(seventhBitValue.count("0")), 7)
  GetMCbAndLCB(int(eigthBitValue.count("1")),int(eigthBitValue.count("0")), 8)
  GetMCbAndLCB(int(ninethBitValue.count("1")),int(ninethBitValue.count("0")), 9)
  GetMCbAndLCB(int(tenthBitValue.count("1")),int(tenthBitValue.count("0")), 10)
  GetMCbAndLCB(int(eleventhBitValue.count("1")),int(eleventhBitValue.count("0")), 11)

  print('-------------------')
  _gammaRate = ""
  for _gammaRateBit in gammaRate:
    _gammaRate = _gammaRate + str(_gammaRateBit).strip()

  print("Gamma Rate: " + _gammaRate)
  decimalGammaRate = int(_gammaRate,2)
  print("Gamma Rate in decimal: {}".format(decimalGammaRate))
  
  _epsilonRate = ""
  for _epsilonRateBit in epsilonRate:
    _epsilonRate = _epsilonRate + str(_epsilonRateBit).strip()

  print("Epsilon Rate: " + _epsilonRate)
  decimalEpsilonRate = int(_epsilonRate,2)
  print("Epsilon Rate in decimal: {}".format(decimalEpsilonRate))

  powerConsumption = decimalGammaRate * decimalEpsilonRate
  print("Power Consumption: {}".format(powerConsumption))
  print('-------------------')

def Main():
  """
  print('-------------------')
  print("MCb = most common bit")
  print("LCb = least common bit")
  print('-------------------')
  """

  f = open(theInputFile, "r")
  for allBits in f:
    strBits = str(allBits).strip()
    print(allBits)
    print('-------------------')

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

  f.close()

  GetRates()

Main()