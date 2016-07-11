dic = {'name' : 'wooseok', 'phone':'123456789', 3 : 'hello'};
print('my information : ', dic)
print(dic[3])
print(dic['name'])
dic['grade']= 1
print('my grade', dic['grade'])
print('delete my phone number')
del dic['phone']
print(dic)
print('is e-mail in my information?')
print('e-mail' in dic)