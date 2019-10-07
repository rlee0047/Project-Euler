By: Ryan Lee
Date: 10/6/19

#nothing to import 

#beginning of the program
def main ():
    
    #setting accumulator 
    startPoint = 0
    
    #Creating for loop to run from 1 to 1000
    for i in range(1,1000) :
        
        #Check vaule for mod 3 or 5 
        if i%3 == 0 or i%5 == 0:
            
            #if mod for 3 or 5 then add to accumilator and reset
            startPoint = startPoint + i
    #prints final total of all multiples of 3 and 5
    print(startPoint)
    
#end transmission 
main()     