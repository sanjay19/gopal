def reverse(s):

   return s[::-1]

def ispalindrome(s):

    rev=reverse(s)
  
  if (s==rev):

    	return 1
 
   else:
	
        return -1

s="1221"

y=ispalindrome(s) 
   
if (y==1):
 
   print("yes")

else:
   
 print("No")
		
