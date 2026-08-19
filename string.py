#power=int(input())
#s=input().strip()
#bulb=s.index('B')
#total=0
#current_power=power
#for i in range(bulb-1,-1,-1):
 #   if s[i]=='C':
   #     current_power+=1
  #  elif s[i]=='H':
 #       if current_power>0:
 #           total +=1
#            current_power -=1

#move right
#current_power=power
#for i in range(bulb-1,len(s)):
 #   if s[i]=='C':
  #      current_power+=1
 #   elif s[i]=='H':
 #       if current_power>0:
 #           total += 1
 #           current_power -= 1
#print("Input Power:",power)
#print("Input String:",s)
#print("Total House lit:",total)
moves=2
n=5
petrol=[2,4,5,1,6]
availability=[1,0,1,1,0]
for i in range(n):
    if availability[i]==1:
        for j in range(moves):
            petrol[i]=petrol[i]*2
print(petrol)


