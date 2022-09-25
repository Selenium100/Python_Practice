name = "nitya is is a good boy"

# I want only Nitya from it
print(name[0:5])

# To know length of this string with len method
print(len(name))

# Reverse the string entirely
print(name[::-1])

#some string methods
print(name.endswith("boy"))
print(name.count("is"))
print(name.capitalize())
print(name.find("boy"))
print(name.upper())
print(name.lower())
print(name.replace("is", "are"))

txt= "My name is {} and my age is {}".format("Nitya", 30)
print(txt)

x = ",".join(name)
print(x)

print(name.split())


