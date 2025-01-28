print(dir("hi"))
methods = dir("hi")
useful_methods = []
for method in methods:
    if "__" in method:
        continue
    useful_methods.append(method)
print(useful_methods)
print(help("hi".capitalize))  #get help for whatever method you want
print("cat".capitalize())
s="I go to school every day"
print(s.capitalize())

print(help("".casefold))
print("I IKE CAKE!!@gmail.com".casefold())
# print("hello".center(__width=30, __fillchar="x"))
print("bananananana".count("a")) #count is useful

print("ana ana ana banana".find("ana")) #0 because the first "ana" is at position 0

print("abcdefg".index("b"))
words= ["i","like","to","sing"]
print(" ".join(words))

s="I like to go hiking!"
print(s.replace(" ", "! !"))
s= "I like to go hiking!"
# print (s.split())
print(s.replace("!", "").split())
print(s.upper())
punctuation = "!@#$%^&*()_-+={}[]|\:;'<>?,./"
sentence= "How, are, you? I don't like this"
for p in punctuation:
    sentence= sentence.replace(p, "")
print(sentence)