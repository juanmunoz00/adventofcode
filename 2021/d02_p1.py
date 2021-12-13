##Open file
#File
theInputFile = "d02_data_test.txt"

f = open(theInputFile, "r")

for instruction in f:
  print(instruction)

f.close()