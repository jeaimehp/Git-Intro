# Je'aime's Crazy Code
# Test for HPC in the City training  
import os

print("Yes I am ready to do some real work to help solve the worlds problems!\n")
data = []
for i in range(0,50):
  data.append(str("Hello for time # "+str(i)))


print("I can't belive you did that",len(data),"times")

print("Oh now you want to save it too?, Whatever...sigh")

with open('data.txt', 'w') as filehandle:
    for listitem in data:
        filehandle.write('%s\n' % listitem)

print("There it is written")
print(os.listdir())
print("\n\nI'm so done, go away please!")
