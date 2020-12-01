HOW TO ACCESS AND PERFORM THE CRD OPERATIONS.


#run the MODULE of MAIN FILE and import mainfile as a library 

import code as K
#Here code refers to the code file that i posted here.


K.create("Enjoyment",42)
#it creates a key with key_name,value given and with no time-to-live property


K.create("Issues",70,4500) 
#it creates a key with key_name,value given and with time-to-live property value given(number of seconds)


K.read("Issues")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


K.read("Enjoyment")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


K.create("Issues",70)
#it returns an ERROR since the key_name already exists in the database


 
K.delete("Enjoyment")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(K.create or K.read or K.delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(K.create or K.read or K.delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on upto tn

#the code also returns other errors like 
#"File memory limit reached" if file memory exceeds 1GB
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,


