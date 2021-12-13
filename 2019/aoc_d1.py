filepath = 'C:/'
filename = 'input_d01.txt'
complete_filepathname = filepath+filename
print('Opening from '+complete_filepathname)
#Initialize the frequency shifter
def frequency_shifter(suma):
    #suma=0
    with open(complete_filepathname) as f:
        for line in f:
            #Adding the frequency shit
            suma += int(line.strip())
    
    return suma
#The resulting frequency after all of the changes in frequency have been applied
print ('The resulting frequency after all of the changes in frequency have been applied: '+str(frequency_shifter(0)))