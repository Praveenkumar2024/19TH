x=int(input("enter the x value=")
for i in range(1,x+1):
    for j in range(1,x+1):
         if(i>=j):
            print(i );
     print(end=" ");
#completed

1
22
333
4444
555555
         
 #palindome number
      num=int(input("entre the number ="))
      x=num;
      rev=0;
      while(num!=0):
             r=num%10;
             rev=rev*10+r;
             num=num/10;
      if(x==rev):
           print("it is palindrome")
      else:
           print("it iis not pallindrome") 
  #armstan number
      num= int(input("enter the number="))
      sum=0;
      while(num!=0):
         r=nnum%10;
         sum=sum+r*r*r;
         num=num/10;
      print(sum);
      
