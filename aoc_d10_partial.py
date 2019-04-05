filepath = 'C:/'
filename = 'input_d10.txt'
complete_filepathname = filepath+filename
print('Opening from '+complete_filepathname)

def yet_another_position_shift():
    #sec=1#starting from 1st position change
    for sec in range(1,10):
        with open(complete_filepathname) as f:
            for line in f:
                print(line)
                #get position
                #bestMincommachar=strbestMin.find(',')
                posX1=line.find('=<')+2    
                pos1=line[posX1:posY]
                posX2=line.find(',')

                posX=line[posX1:posX2]
                print('Initial position X: '+posX.strip())

                #print(pos.strip())
                posY2=line.find('>')
                posY1=line[posX2+2:posY2]
                print('Initial position Y: '+posY1.strip())

                #get velocity
                mov=line.find('v')+10
                eol=len(line)-2
                line2=line[mov:eol]

                intmovX=line2.find(',')

                movX=line2[0:intmovX]
                print('Velocity X: '+movX)

                movY=line2[intmovX+1:eol]
                print('Velocity Y: '+movY)

                #New coordinates due change in position
                #sec*vx+posx

                newCoordx=sec*int(posX)+int(movX)
                newCoordy=sec*int(posY1)+int(movY)
                print('New coordinates due change in position after '+str(sec)+' seconds: <'+str(newCoordx)+','+str(newCoordy)+'>')

#sec += 1
        
yet_another_position_shift()        