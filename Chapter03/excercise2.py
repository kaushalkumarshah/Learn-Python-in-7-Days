tup = ('www', 'thapar', 'edu','index','php','about-us','mission')
url1= ".".join(tup[0:3])
url2= ".".join(tup[3:5])
url3= "/".join(tup[5:])
print url1+"/"+url2+"/"+url3
