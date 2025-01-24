x = "awesome"

def myfunc():
  # Lets access var out of scope
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
