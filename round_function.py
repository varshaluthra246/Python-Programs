#round function
#round(number, digits(optional))
#round function return by default floor value    --> 1 2.0, 2.1, 2.2, 2.3, 2.5,2.6,2.7 3 4 5 6 

#select round(2.3535);

x = round(2.4535) #--> 2.3  -- 2.0   --> floor <5> ceil

#2.0(floor) 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0(ceil)

y = round(2.3215,2) # <500>
z = round(2.6288,2) #-->
a = round(135.379,2)

b = round(15.123,1)
c = round(57.193,-1) #--> 30 31 32 33 34 35 36 37 38 39 40
d = round(12.58) #12.0 ----- 12.58 12.59 12.60 12.61 -------- 13.00

e = round(12.28)
f = round(12.286754,3)

g = round(12.286354,3)
h = round(12.286554,3)

i = round(12.286554,2)  #21 ------ 25 ----- 12.28 12.28.1 ---- 29
j = round(35.67283,3)  #-->35.673
k = round(12.286554,4) #-->12.2866

l = round(538.72,-1)   #10's place roundoff
m = round(529.72,-2)     #100's place roundoff 500 501. ...529
n = round(533.72,-2)


print("x",x)
print("y",y)
print("z",z)

print("a",a)

print("b",b)

print("c",c)
print("d",d)
print("e",e)

print("f",f)
print("g",g)
print("h",h)

print("i",i)
print("j",j)
print("k",k)

print("l",l)
print("m",m)
print("n",n)

