#Python Lists

color = ['red', 'blue', 'green']
print (color [0]) #red
print (color [2]) #green
print(len(color)) #3


#FOR and IN

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum) #30

#you can set a variable without def
#but you need def for a function

#THE IN CONSTRUCT

list = ["harry", "curly", "moe"]
if 'curly' in list: #is curly in the list or not?
    print("yay") 
    
    
#range

for i in range(100): #for some value in range 0-100
    print(i) 
    
    
list = ['larry', 'curly', 'moe']
list.append('shemp') #adds a single element to a list
list.insert(0, 'xxx') #insert xxx to 1st point in list
list.extend(['yyy', 'xxx']) #adds these values to the end of list
print(list) #xxx, larry, curly, moe, shemp, yyy, xxx
print(list.index('curly')) #2

list.remove('curly') #search and remove
list.pop(1) #removes and return larry
print(list) 


#sorting 
a = [5, 1, 4, 3]
print(sorted(a)) # [1,3, 4, 5]
print(a) #[5, 1, 4, 3]

strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs)) #['BB', 'CC', 'aa', 'zz'] case sensitive
print(sorted(strs,reverse=True)) #['zz', 'aa', 'CC', 'BB']