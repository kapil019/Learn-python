#!/usr/bin/python

#start with Number Datatype
x,y,z = 3,5,7
x=-2.4
print("abs method abs(x) = ",abs(x))
x=3
print("abs method x.__abs__() = ", x.__abs__())
x=3
print("add method x+y = "+str(x+y))
x=2.4
print("add method x.__add__(y) = ",x.__add__(y))
x=3
print("and method x__and__(y) = ", x.__and__(y))
#x=2.4
print("and method x&y = ", x&y)
x=3
print("cmp method cmp(x,y) = ", cmp(x,y))
#x=2.4
print("and method x.__cmp__(y) = ", x.__cmp__(y))
x=3
print("coerce method coerce(x,y) = ", coerce(x,y))
x=2.4
print("coerce method x.__cmp__(y) = ", x.__coerce__(y))
x=3
print("div method coerce(x,y) = ", x/y)
x=2.4
print("div method x.__div__(y) = ", x.__div__(y))
x=3
print("divmod method coerce(x,y) = ", divmod(x,y))
x=2.4
print("divmod method x.__divmod__(y) = ", x.__divmod__(y))
x=3
print("float method float(x) = ", float(x))
x=2
print("float method x.__float__() = ", x.__float__())