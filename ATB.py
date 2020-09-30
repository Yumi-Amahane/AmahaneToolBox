import numpy as np
import matplotlib.pyplot as plt
import math

import random

def matT(A,B):
    R=[]
    for x in (range(len(A))):
        RD=[]
        for y in range(len(A)):
            S=0
            for r in range (len(A)):
                S+=A[x][r]*B[r][y]
            RD.append(S)
        R.append(RD)
    return(R)

def matPow(A,n):
    M=scipy.linalg.eig(A)
    R=scipy.linalg.eig(A)[1]
    for i in range(len(M[0])):
        for j in range(len(M[0])):
            R[i][j]*=M[0][j]**n
    return(matT(R,np.linalg.inv(scipy.linalg.eig(A)[1])))
    
from io import BytesIO
from PIL import Image
def PR_Phasor(Re,Im="None",point="P",Colo="blue"):
    if Im=="None":
        Im=Re
    fig=plt.figure()
    #丸点線
    maru=plt.subplot()
    x=np.arange(-100,101)
    yp=[]
    yn=[]

    maru.set_aspect("equal")
    plt.xlabel("Re")
    plt.ylabel("Im")

    #for R,I,K in  zip(Re,Im,np.arange(len(Re))):
    for R,I in  zip(Re,Im):
        if point=="L":
            PRST=int((R.real**2+I.imag**2)**0.5*0.2)
            for i in range(PRST):
                PH=plt.scatter(R.real*i/PRST,I.imag*i/PRST,color=Colo)
        else:
            PH=plt.scatter(R.real,I.imag,color=Colo)
    
    LIM=0
    for i in range (len(Re)):
        LIMD=max([abs(Re[i].real),abs(Im[i].imag)])
        if LIM<LIMD:
            LIM=LIMD
    plt.xlim(-LIM,LIM)
    plt.ylim(-LIM,LIM)
    
    return(PH)
    
    buf=BytesIO()
    fig.savefig(buf,bbox_inches='tight',pad_inchas=0.0)
    return Image.open(buf)
    
def Shuffle(L):
    R=[]
    Res=[]
    for i in range(len(L)):
        k=random.randint(0,len(L)-1)
        while k in Res:
            k=random.randint(0,len(L)-1)
            
        Res.append(k)
        R.append(L[k])
    return(R)