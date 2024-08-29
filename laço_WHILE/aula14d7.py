print('sequencia de fibonacci\n ')
n = int(input('digite quantos termos da sequencia de fibonacci você deseja exibir: '))

a = 1
x = 0
y = 0

for c in range(1, (n + 1)):
    y = a + x

    print(y)
    
    x = a 
    a = y       
