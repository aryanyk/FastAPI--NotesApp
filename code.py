def addname(fname: str, lname: str = None):
  # in update python version you can use str|list too
  fname = fname.capitalize()
  return fname + " " + lname


fname="aryan"
lname="Khandhadiya"

val=addname(fname,lname)
print(val)