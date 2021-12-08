def sum(k):
  i=1
  s=0
  while i<=k:
    s=s+i
    print (i)
    i=i+1
  return s, 'tekst'
n=int(input('Введите число: '))
x,y=sum(n)
print ('Сумма равно: ',x)
print (y)
