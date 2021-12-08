def sum(x):
 if (x>=1 and x<=2) or x==12:
   return 'Zima'
 elif x>=3 and x<=5:
   return 'Vesna'
 elif x>=6 and x<=8:
   return 'Leto'
 elif x>=9 and x<=11:
   return 'Osen'
 else:
   return 'Error'
x = int(input('Введите число: '))
b=sum(x)
print(b)
