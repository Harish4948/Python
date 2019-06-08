n=int(input())
combo=dict()
item=list()
total_final=0
for i in range(n):
      temp=list(map(str,input().split()))    
      temp[2]=int(temp[2])
      temp[1]=int(temp[1])
      if(temp[0] not in combo):
            combo[temp[0]]={temp[1]:temp[2]}
      else:
            combo[temp[0]].update({temp[1]:temp[2]})
            
m=int(input())
for i in range(m):
      temp=list(map(str,input().split()))    
      temp[2]=int(temp[2])
      temp[1]=int(temp[1])
      if(temp[0] not in combo):
            total_final+=temp[1]*temp[2]
            item.append((temp[0],str(temp[1]*temp[2])+".00"))
      else:
            k=list(combo[temp[0]].keys())
            diff=list()
            flag=0
            for i in k:
                  diff.append(abs(i-temp[1]))
##                  if(temp[1]>i):
##                        flag=1
##                  else:
##                        flag=0
##            if(flag):
            inner_key_index=diff.index(min(diff))
            inner_key=k[inner_key_index]
            discount_perc=combo[temp[0]][inner_key]
            total=temp[1] * temp[2]
            discount_value=(total*discount_perc)/100
            final_price=total-discount_value
            total_final+=final_price
            item.append((temp[0],str(final_price)+"0"))

for i in item:
      for j in i:
            print(j,end=" ")
      print("")
print("Total "+str(total_final)+"0")
