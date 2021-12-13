import re
import matplotlib.pyplot as plt

filepath = 'C:/'
filename = 'input_d10.txt'
complete_filepathname = filepath+filename
print('Opening from '+complete_filepathname)

def yet_another_position_shift():
    #sec=1#starting from 1st position change
    msgToplot=[]    

    sec = 12345
    #for sec in range(1,10):
    with open(complete_filepathname) as f:
        for line in f:
            #print(line)
            #get position
            posX1=line.find('=<')+2 
            posX2=line.find(',')
            posX=line[posX1:posX2]

            posY2=line.find('>')
            posY1=line[posX2+2:posY2]

            #get velocity
            mov=line.find('v')+10
            eol=len(line)-1

            line2=line[mov:eol]

            intmovX=line2.find(',')

            movX=line2[0:intmovX]

            movY=line2[intmovX+1:eol]
            movY=re.sub('>', '', movY)

            #New coordinates due change in position
            #sec*vx+posx

            newCoordx=sec*int(posX)+int(movX)
            newCoordy=sec*int(posY1)+int(movY)
            #print('New coordinates due change in position after '+str(sec)+' seconds: <'+str(newCoordx)+','+str(newCoordy)+'>')
            coords = tuple([newCoordx,newCoordy])
            msgToplot.append(coords)
    
    print('Plotting...')
    plt.plot(msgToplot)
    plt.show()
      
yet_another_position_shift()    
print('Done!')