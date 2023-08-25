from io import StringIO

s = StringIO()
s.write("scabhbjhbcs")
s.write("657652367766732")
a = s.getvalue()
print(a, type(a))