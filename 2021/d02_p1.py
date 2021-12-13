##Open file
#File
theInputFile = "2021/d02_data.txt"

instructionSuffix = 2

horizontalPosition = 0
startHorizontalPositionChar = 8
endHorizontalPositionChar = startHorizontalPositionChar + 1

downPosition = 0
startDownPositionChar = 5
endtDownPositionChar = startDownPositionChar + 1

upPosition = 0
startUpPositionChar = 3
endUpPositionChar = startUpPositionChar + 1

depthPosition = 0
finalPosition = 0

f = open(theInputFile, "r")
for instruction in f:
  #print(instruction)
  command = instruction[0:1]
  #print('Command: {}'.format(command))

  if( command == "f" ):
    horizontalPositionVal = instruction[startHorizontalPositionChar:endHorizontalPositionChar]
    horizontalPosition += int(horizontalPositionVal)

    #print('|Command: {} position: {} total H Position: {}|'.format(command, horizontalPositionVal, horizontalPosition))
  elif ( command == "d" ):
    downPositionVal = instruction[startDownPositionChar:endtDownPositionChar]
    #downPosition += int(downPositionVal)
    depthPosition += int(downPositionVal) 
    
    #print('|Command: {} position: {} total D Position: {}|'.format(command, downPositionVal, downPosition))  
  elif ( command == "u" ):
    upPositionVal = instruction[startUpPositionChar:endUpPositionChar]
    #upPosition += int(upPositionVal)
    depthPosition -= int(upPositionVal)
    
    #print('|Command: {} position: {} total U Position: {}|'.format(command, upPositionVal, upPosition))  
  
  #print('|Command: {} Depth Position: {}|'.format(command, depthPosition, depthPosition))
finalPosition = horizontalPosition * depthPosition
print('|Horizontal Position: {} Depth Position: {} Final Position: {}|'.format(horizontalPosition, depthPosition, finalPosition))

f.close()