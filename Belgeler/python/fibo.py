def fibo(n):
    a,b=1,1
    print(a),
    for i in range(0,n):
        a,b=b,a+b
        print(a),
x=int(input("Fiboneccisi hesaplanacak değeri giriniz: "))
fibo(x)