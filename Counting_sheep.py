#Counting sheep...

#For example,
#[True,  True,  True,  False,
  #True,  True,  True,  True ,
  #True,  False, True,  False,
  #True,  False, False, True ,
  #True,  True,  True,  True ,
  #False, False, True,  True]

#The correct answer would be 17.
#Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    count = 0
    for num in sheep:
        if num == True:
            count +=1
    return count
