mystr=input("Enter String: ")
print(mystr)
search_not=mystr.find('not')
search_poor=mystr.find('poor')
if search_not>0 and search_poor>0 and search_poor>search_not:
    print(mystr.replace(mystr[search_not:],'good'))

