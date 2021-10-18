array="Hello there!"

for i in array:
    print(i)

print(len(array));

ival=22
sval="I'm Iuliu and I'm "
print(sval+str(ival))

ival2=ival*2
print(ival2)

random_list=["string value",25,True,29.5]

for i in random_list:
    print(isinstance(i,bool))

#the instance checking need to be as a whole in an array,list,tuple etc
print(isinstance(random_list,tuple))



