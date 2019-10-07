

def main():
    
    i =0
    firNum = 0
    secNum = 1
    
    startPoint = 0
    
    while(i < 4000000):
        if (i <= 1):
            Next = i
        else: 
            Next = firNum +secNum
            firNum = secNum 
            secNum = Next
        
        if i%2 == 0 :
            startPoint = startPoint + i
        print(startPoint)
        i = i + 1
    
    
    
main()    