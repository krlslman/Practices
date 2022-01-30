# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#- **Mathematical Operations**

print(4**2)

print(46/23) # **division gives float**  [ =2.0 ]

print(7 // 2)  # it gives integer part of division  [ =3 ]

print(9 % 2)  # remainder of this division is 1, so it is an odd number

print(64**(1/2)) # square root


#- **String Operations**

print('smoking', 'is', 'slowly', 'killing me', sep='_')

#print fonksiyonunda sep ayarlamazsak default olarak expression’lar arasına boşluk koyar.

# - \n: means new line,
# - \t: means tab mark,
# - \b: means backspace. It moves the cursor one character to the left.
print("""benim adım ‘kamil’ onun adı “hasan” """) # : Bu şekilde kullanırsak hata vermez
# - 
# - Arithmetic syntax (+,  and =),
# - % operator formatting,
# - string.format() method,
# - f-string formatting.
    
phrase = 'I have %d %s and %.2f brothers' % (4, "children", 5)
    
    # = I have 4 children and 5.00 brothers
    
print('we', '\bare', '\bunited') #  remember, normally print() function separates expressions by spaces [ =weareunited ]
    
   # **⚠️Avoid ! :**
    
   # - Be careful, when using 👉🏻\ in the long string. It may cause error because of its functionality described above. Using 👉🏻\\ guarantees no error.

#💡Tips:

# - In the '%s' syntax : s stands for 'string'.
# - In the '%.2f' syntax : f stands for 'float'. In this example 2 digits after point.
# - In the '%d' syntax : d stands for 'numeric'.
sentence = "apologizing is a virtue"
        
print("%.11s" % sentence) #we get first 11 characters of the string
fruit='banana'
amount=3
print('The amount of {} we bought is {} pounds'.format(fruit, amount))
        

# The formula syntax is : string.method()

# - str.strip() : removes all spaces (or specified characters) from both sides.
# - str.rstrip() : removes spaces (or specified characters) from the right side.
# - str.lstrip() : removes spaces (or specified characters) from the left side.

# - Boolen Operations

# OR ve AND -Boolen Operations’daki detayı;
# OR’ da True  baskın (ör: False OR True  = True  )
# AND’ de False baskın (ör: False AND True  = False)


# - List
empty_list_1=[]
my_list=empty_list_1.append('114')
city = [1,2,3,'New York', 'Stockholm', 'Istanbul']  
city.insert(2, 'Stockholm')
#print(city.sort())
print(len(city))
city[1] = 'Melbourne' # we assign 'Melbourne' to index 2 (this is how we change index 1)
print(my_list,city)
print("pop : ",city.pop(1))   # pop works with index
city.remove('New York')       # remove works with value
print("removed : ", city)
del city[0]                  # del works with index
print("deleted : ", city)

# DATE : 21.01.2022
