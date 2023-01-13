
e = 2.718 #Diketahui nilai e
z = str(input("Masukan Fungsi: "))                      #Input fungsi atau f(x)
batasBawah = float(input("Masukan Batas Bawah: "))      #Input nilai batas bawah
batasAtas = float(input("Masukan Batas Atas: "))        #Input nilai batas atas
sub_interval = int(input("Masukan Banyak Partisi: "))   #Input banyak partisi

def f(n): #Fungsi untuk mengembalikan nilai dari f(x)
    temp = eval(z)
    
    return temp

def simpson13(x0,xn,n):
    h = (xn - x0) / n   #Mencari jarak interval antar titik (delta x)
    
    for i in range(n+1): 
         
        k = x0 + i*h    #Menentukan titik selanjutnya 
         
        #Kondisi untuk mencari nilai integrasi
        if i == 0:    
            integration = f(x0)
            
        elif i == n:
            integration = integration + f(xn)
            
        elif i%2 == 0:
            integration = integration + 2 * f(k)
            
        elif i%2 == 1:
            integration = integration + 4 * f(k)
        print (integration)
        
    #Mencari nilai akhir dari integrasi
    integration = integration * h/3
    
    return integration
    
#Panggil fungsi & Hasil
result = simpson13(batasBawah, batasAtas, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f"%(result))