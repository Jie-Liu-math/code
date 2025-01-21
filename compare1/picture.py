
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
def readFile(path):
    f = open(path)
    first_ele = True
    for data in f.readlines():
        data = data.strip('\n')
        nums = data.split(" ")
        if first_ele:
            nums = [float(x) for x in nums ]
            matrix = np.array(nums)
            first_ele = False
        else:
            nums = [float(x) for x in nums ]
            matrix = np.c_[matrix,nums]
    return matrix
    f.close()


if __name__ == '__main__':
    
    N=30
    print(N)
    n=10
    iter=200
    D1_1=np.transpose(readFile('paper_algorithm2_TAU2.txt'))
    D2_1=np.transpose(readFile('Mitra_et_al_2021b_TAU2.txt'))
    D3_1=np.transpose(readFile('Mitra_et_al_2021a_TAU2.txt'))
     
    k_1=1490
    kk_1=800
    
    BASE1_1=np.zeros(k_1)
    BASE2_1=np.zeros(k_1)
    BASE3_1=np.zeros(kk_1)
    BASE4_1=np.zeros(kk_1)
    
    BASE5_1=np.zeros(k_1)
    BASE6_1=np.zeros(k_1)
    BASE7_1=np.zeros(kk_1)
    BASE8_1=np.zeros(kk_1)
    
    BASE9_1=np.zeros(k_1)
    BASE10_1=np.zeros(k_1)
    BASE11_1=np.zeros(kk_1)
    BASE12_1=np.zeros(kk_1)
     
    for j in range(0,k_1-1):
        BASE1_1[j]=j
        BASE2_1[j]=D1_1[j+1]
        
        
    for j in range(0,k_1-1):
        BASE5_1[j]=j
        BASE6_1[j]=D2_1[j+1]
        
    for j in range(0,k_1-1):
        BASE9_1[j]=j
        BASE10_1[j]=D3_1[j+1]
   
    k0_1=200
    
    for jj in range(0,kk_1):
        BASE3_1[jj]=BASE1_1[k0_1+jj]
        BASE4_1[jj]=BASE2_1[k0_1+jj]     
        
    for jj in range(0,kk_1):
        BASE7_1[jj]=BASE5_1[k0_1+jj]
        BASE8_1[jj]=BASE6_1[k0_1+jj]
     
    for jj in range(0,kk_1):
        BASE11_1[jj]=BASE9_1[k0_1+jj]
        BASE12_1[jj]=BASE10_1[k0_1+jj]
          
    x_1 = BASE3_1
    y_1 = BASE4_1
     
    x2_1=BASE7_1
    y2_1=BASE8_1
    
    x3_1=BASE11_1
    y3_1=BASE12_1
    
    D1_2=np.transpose(readFile('paper_algorithm2_TAU3.txt'))
    D2_2=np.transpose(readFile('Mitra_et_al_2021b_TAU3.txt'))
    D3_2=np.transpose(readFile('Mitra_et_al_2021a_TAU3.txt'))
    
    k_2=1490
    kk_2=800
    
    BASE1_2=np.zeros(k_2)
    BASE2_2=np.zeros(k_2)
    BASE3_2=np.zeros(kk_2)
    BASE4_2=np.zeros(kk_2)
    
    BASE5_2=np.zeros(k_2)
    BASE6_2=np.zeros(k_2)
    BASE7_2=np.zeros(kk_2)
    BASE8_2=np.zeros(kk_2)
    
    BASE9_2=np.zeros(k_2)
    BASE10_2=np.zeros(k_2)
    BASE11_2=np.zeros(kk_2)
    BASE12_2=np.zeros(kk_2)
    
    for j in range(0,k_2-1):
        BASE1_2[j]=j
        BASE2_2[j]=D1_2[j+1]
           
    for j in range(0,k_2-1):
        BASE5_2[j]=j
        BASE6_2[j]=D2_2[j+1]
        
    for j in range(0,k_2-1):
        BASE9_2[j]=j
        BASE10_2[j]=D3_2[j+1]
    
    k0_2=200
    
    for jj in range(0,kk_2):
        BASE3_2[jj]=BASE1_2[k0_2+jj]
        BASE4_2[jj]=BASE2_2[k0_2+jj]
      
        
    for jj in range(0,kk_2):
        BASE7_2[jj]=BASE5_2[k0_2+jj]
        BASE8_2[jj]=BASE6_2[k0_2+jj]
        
    for jj in range(0,kk_2):
        BASE11_2[jj]=BASE9_2[k0_2+jj]
        BASE12_2[jj]=BASE10_2[k0_2+jj]
    
    x_2 = BASE3_2
    y_2 = BASE4_2
    
   
    x2_2=BASE7_2
    y2_2=BASE8_2
    
    x3_2=BASE11_2
    y3_2=BASE12_2
   
    #
    D1_3=np.transpose(readFile('paper_algorithm2_TAU4.txt'))
    D2_3=np.transpose(readFile('Mitra_et_al_2021b_TAU4.txt'))
    D3_3=np.transpose(readFile('Mitra_et_al_2021a_TAU4.txt'))
    
    
    k_3=1490
    kk_3=800
    
    BASE1_3=np.zeros(k_3)
    BASE2_3=np.zeros(k_3)
    BASE3_3=np.zeros(kk_3)
    BASE4_3=np.zeros(kk_3)
    
    BASE5_3=np.zeros(k_3)
    BASE6_3=np.zeros(k_3)
    BASE7_3=np.zeros(kk_3)
    BASE8_3=np.zeros(kk_3)
    
    BASE9_3=np.zeros(k_3)
    BASE10_3=np.zeros(k_3)
    BASE11_3=np.zeros(kk_3)
    BASE12_3=np.zeros(kk_3)
    
    for j in range(0,k_3-1):
        BASE1_3[j]=j
        BASE2_3[j]=D1_3[j+1]
        
        
    for j in range(0,k_3-1):
        BASE5_3[j]=j
        BASE6_3[j]=D2_3[j+1]
        
    for j in range(0,k_3-1):
        BASE9_3[j]=j
        BASE10_3[j]=D3_3[j+1]
    
    k0_3=200
    
    for jj in range(0,kk_3):
        BASE3_3[jj]=BASE1_3[k0_3+jj]
        BASE4_3[jj]=BASE2_3[k0_3+jj]
      
    for jj in range(0,kk_3):
        BASE7_3[jj]=BASE5_3[k0_3+jj]
        BASE8_3[jj]=BASE6_3[k0_3+jj]
        
    for jj in range(0,kk_1):
        BASE11_3[jj]=BASE9_3[k0_3+jj]
        BASE12_3[jj]=BASE10_3[k0_3+jj]
        
    x_3 = BASE3_3
    y_3 = BASE4_3
    
    x2_3=BASE7_3
    y2_3=BASE8_3
    
    x3_3=BASE11_3
    y3_3=BASE12_3
   
   #Next
    
    D1_4=np.transpose(readFile('paper_algorithm2_TAU5.txt'))
    D2_4=np.transpose(readFile('Mitra_et_al_2021b_TAU5.txt'))
    D3_4=np.transpose(readFile('Mitra_et_al_2021a_TAU5.txt'))
   
    k_4=1490
    kk_4=800
   
    BASE1_4=np.zeros(k_4)
    BASE2_4=np.zeros(k_4)
    BASE3_4=np.zeros(kk_4)
    BASE4_4=np.zeros(kk_4)
    
    BASE5_4=np.zeros(k_4)
    BASE6_4=np.zeros(k_4)
    BASE7_4=np.zeros(kk_4)
    BASE8_4=np.zeros(kk_4)
   
    BASE9_4=np.zeros(k_4)
    BASE10_4=np.zeros(k_4)
    BASE11_4=np.zeros(kk_4)
    BASE12_4=np.zeros(kk_4)
   
    for j in range(0,k_4-1):
        BASE1_4[j]=j
        BASE2_4[j]=D1_4[j+1]
       
       
    for j in range(0,k_4-1):
        BASE5_4[j]=j
        BASE6_4[j]=D2_4[j+1]
       
    for j in range(0,k_4-1):
        BASE9_4[j]=j
        BASE10_4[j]=D3_4[j+1]
   
    k0_4=200
   
    for jj in range(0,kk_4):
        BASE3_4[jj]=BASE1_4[k0_4+jj]
        BASE4_4[jj]=BASE2_4[k0_4+jj]
     
    for jj in range(0,kk_1):
        BASE7_4[jj]=BASE5_4[k0_4+jj]
        BASE8_4[jj]=BASE6_4[k0_4+jj]
       
    for jj in range(0,kk_1):
        BASE11_4[jj]=BASE9_4[k0_4+jj]
        BASE12_4[jj]=BASE10_4[k0_4+jj]
       
    x_4 = BASE3_4
    y_4 = BASE4_4
   
    x2_4=BASE7_4
    y2_4=BASE8_4
   
    x3_4=BASE11_4
    y3_4=BASE12_4
   
    D1_5=np.transpose(readFile('paper_algorithm2_TAU6.txt'))
    D2_5=np.transpose(readFile('Mitra_et_al_2021b_TAU6.txt'))
    D3_5=np.transpose(readFile('Mitra_et_al_2021a_TAU6.txt'))
   
    k_5=1490
    kk_5=800
    
    BASE1_5=np.zeros(k_5)
    BASE2_5=np.zeros(k_5)
    BASE3_5=np.zeros(kk_5)
    BASE4_5=np.zeros(kk_5)
    
    BASE5_5=np.zeros(k_5)
    BASE6_5=np.zeros(k_5)
    BASE7_5=np.zeros(kk_5)
    BASE8_5=np.zeros(kk_5)
    
    BASE9_5=np.zeros(k_5)
    BASE10_5=np.zeros(k_5)
    BASE11_5=np.zeros(kk_5)
    BASE12_5=np.zeros(kk_5)
    
    for j in range(0,k_5-1):
        BASE1_5[j]=j
        BASE2_5[j]=D1_5[j+1]
        
        
    for j in range(0,k_5-1):
        BASE5_5[j]=j
        BASE6_5[j]=D2_5[j+1]
        
    for j in range(0,k_5-1):
        BASE9_5[j]=j
        BASE10_5[j]=D3_5[j+1]
    
    k0_5=200
    
    for jj in range(0,kk_5):
        BASE3_5[jj]=BASE1_5[k0_5+jj]
        BASE4_5[jj]=BASE2_5[k0_5+jj]
      
    for jj in range(0,kk_2):
        BASE7_5[jj]=BASE5_5[k0_5+jj]
        BASE8_5[jj]=BASE6_5[k0_5+jj]
        
    for jj in range(0,kk_2):
        BASE11_5[jj]=BASE9_5[k0_5+jj]
        BASE12_5[jj]=BASE10_5[k0_5+jj]
        
    x_5 = BASE3_5
    y_5 = BASE4_5
    
    x2_5=BASE7_5
    y2_5=BASE8_5
    
    x3_5=BASE11_5
    y3_5=BASE12_5
   
    D1_6=np.transpose(readFile('paper_algorithm2_TAU7.txt'))
    D2_6=np.transpose(readFile('Mitra_et_al_2021b_TAU7.txt'))
    D3_6=np.transpose(readFile('Mitra_et_al_2021a_TAU7.txt'))
    
    k_6=1490
    kk_6=800
    
    BASE1_6=np.zeros(k_6)
    BASE2_6=np.zeros(k_6)
    BASE3_6=np.zeros(kk_6)
    BASE4_6=np.zeros(kk_6)
    
    BASE5_6=np.zeros(k_6)
    BASE6_6=np.zeros(k_6)
    BASE7_6=np.zeros(kk_6)
    BASE8_6=np.zeros(kk_6)
    
    BASE9_6=np.zeros(k_6)
    BASE10_6=np.zeros(k_6)
    BASE11_6=np.zeros(kk_6)
    BASE12_6=np.zeros(kk_6)
    
    for j in range(0,k_6-1):
        BASE1_6[j]=j
        BASE2_6[j]=D1_6[j+1]
        
        
    for j in range(0,k_6-1):
        BASE5_6[j]=j
        BASE6_6[j]=D2_6[j+1]
        
    for j in range(0,k_6-1):
        BASE9_6[j]=j
        BASE10_6[j]=D3_6[j+1]
    
    k0_6=200
    
    for jj in range(0,kk_6):
        BASE3_6[jj]=BASE1_6[k0_6+jj]
        BASE4_6[jj]=BASE2_6[k0_6+jj]
      
    for jj in range(0,kk_6):
        BASE7_6[jj]=BASE5_6[k0_6+jj]
        BASE8_6[jj]=BASE6_6[k0_6+jj]
        
    for jj in range(0,kk_6):
        BASE11_6[jj]=BASE9_6[k0_6+jj]
        BASE12_6[jj]=BASE10_6[k0_6+jj]
        
    x_6 = BASE3_6
    y_6 = BASE4_6
    
    x2_6=BASE7_6
    y2_6=BASE8_6
    
    x3_6=BASE11_6
    y3_6=BASE12_6

    
    plt.figure(figsize=(13,20))
    f1=plt.subplot(3, 2, 1)
    plt.semilogy(x3_1,y3_1,label='Mitra et al. (2021a)',color='y',linewidth=1.1,linestyle='--')
    plt.semilogy(x2_1,y2_1,label='Mitra et al. (2021b)',color='r',linewidth=1.1,linestyle='-.')
    plt.semilogy(x_1,y_1,label='Algorithm 2', color='b',linewidth=1.1,linestyle='solid')
    plt.legend(loc = 0, prop = {'size':16})
    plt.grid()
    f1.set_title(r'$\tau=2$',fontsize=20)
    plt.xlabel('Times t',fontsize=15)
    plt.ylabel('Errors',fontsize=15)
    
    
    f2=plt.subplot(3, 2, 2)
    plt.semilogy(x3_2,y3_2,label='Mitra et al. (2021a)',color='y',linewidth=1.1,linestyle='--')
    plt.semilogy(x2_2,y2_2,label='Mitra et al. (2021b)',color='r',linewidth=1.1,linestyle='-.')
    plt.semilogy(x_2,y_2,label='Algorithm 2', color='b',linewidth=1.1,linestyle='solid')
    plt.grid()
    f2.set_title(r'$\tau=3$',fontsize=20)
    plt.xlabel('Times t',fontsize=15)
    plt.ylabel('Errors',fontsize=15)
    
    f3=plt.subplot(3, 2, 3)
    plt.semilogy(x3_3,y3_3,label='Mitra et al. (2021a)',color='y',linewidth=1.1,linestyle='--')
    plt.semilogy(x2_3,y2_3,label='Mitra et al. (2021b)',color='r',linewidth=1.1,linestyle='-.')
    plt.semilogy(x_3,y_3,label='Algorithm 2', color='b',linewidth=1.1,linestyle='solid')
    
    plt.grid()
    
    
    f3.set_title(r'$\tau=4$',fontsize=20)
    plt.xlabel('Times t',fontsize=15)
    plt.ylabel('Errors',fontsize=15)
    
    
    f4=plt.subplot(3, 2, 4)
    
    plt.semilogy(x3_4,y3_4,label='Mitra et al. (2021a)',color='y',linewidth=1.1,linestyle='--')
    plt.semilogy(x2_4,y2_4,label='Mitra et al. (2021b)',color='r',linewidth=1.1,linestyle='-.')
    plt.semilogy(x_4,y_4,label='Algorithm 2', color='b',linewidth=1.1,linestyle='solid')
    

    plt.grid()
    f4.set_title(r'$\tau=5$',fontsize=20)
    plt.xlabel('Times t',fontsize=15)
    plt.ylabel('Errors',fontsize=15)
    
    
    
    
    f5=plt.subplot(3, 2, 5)
    
    plt.semilogy(x3_5,y3_5,label='Mitra et al. (2021a)',color='y',linewidth=1.1,linestyle='--')
    plt.semilogy(x2_5,y2_5,label='Mitra et al. (2021b)',color='r',linewidth=1.1,linestyle='-.')
    plt.semilogy(x_5,y_5,label='Algorithm 2', color='b',linewidth=1.1,linestyle='solid')
    
    plt.grid()
    
    f5.set_title(r'$\tau=6$',fontsize=20)
    plt.xlabel('Times t',fontsize=15)
    plt.ylabel('Errors',fontsize=15)
    
    
    
    f6=plt.subplot(3, 2, 6)
    
    plt.semilogy(x3_6,y3_6,label='Mitra et al. (2021a)',color='y',linewidth=1.1,linestyle='--')
    plt.semilogy(x2_6,y2_6,label='Mitra et al. (2021b)',color='r',linewidth=1.1,linestyle='-.')
    plt.semilogy(x_6,y_6,label='Algorithm 2', color='b',linewidth=1.1,linestyle='solid')
    
    plt.grid()
    
    f6.set_title(r'$\tau=7$',fontsize=20)
    plt.xlabel('Times t',fontsize=15)
    plt.ylabel('Errors',fontsize=15)
    
    
    plt.savefig(fname="compare1_all.eps",format="eps", bbox_inches='tight')
    plt.savefig("compare1_all.jpg")
    plt.show() 
