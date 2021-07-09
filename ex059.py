p=float(input('Digite seu peso: '))
a=float(input('Digite sua altura: '))
a1=a**2 
p1=p/a1
print('Esse é o seu IMC {:.2f}'.format(p1))
if p1<18.5:
    print('Abaixo do peso')
elif p1>=18.5 and p1<25:
    print('Peso ideal')
elif p1>=25 and p1<30:
    print('Sobrepeso')
elif p1>30 and p1<40:
    print('Obesidade')
else:
    print('Obesidade morbida')