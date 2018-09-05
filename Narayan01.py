
# coding: utf-8

# In[1]:


# lowercase letters to uppercase letters and vice versa.
input = 'This is mE 123'
output =''
for i in input:
    if(ord(i)>=65 and ord(i)<=90):
        output += chr(ord(i)+32)
    elif(ord(i)>=97 and ord(i)<=122):
          output +=chr(ord(i)-32)
    else:
          output +=chr(ord(i))
print(output)


# In[2]:


# print the number of times that the substring occurs in the given string
input = 'ABCDCDC'
sub = 'CDC'
count = 0
a = len(input)
for i in range(0, len(input)):
    if input[i:i+len(sub)]==sub:
        count += 1
print(count)



# In[18]:


# Replace the last element in tuples 
ReplaceList = [(10,20,40),(40,50,60),(70,80,90)]
result = ([i[:-1]+(100,) for i in ReplaceList])
print (result)



# In[17]:


# print odd characters
class Even:

    def __init__(self):
        self.input = ""
        self.output = ""
    
  
    
    def enter_input(self):
        self.input = input('Enter the string...')

        for i in self.input:
            if (self.input.index(i) % 2 == 0):
                self.output +=i 

        return self.output
    

    
    def print_output(self):
        print("The resulted string is:", self.output)

if __name__ == "__main__":
    es = Even()
    es.enter_input()
    es.print_output()

