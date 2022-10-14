# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:14:11 2022

@author: LENOV0
"""
import turtle

# Initially the background colour of graphic canvas is white. It can be changed by using the 
# below function.

turtle.bgcolor("yellow") 
seurat=turtle.Turtle()

width=5
height=7

dot_distance=25

seurat.setpos(-250,250) # when you write (0,0) it means canvas pen start from the center.


def spiral(m,n):
    k=0
    l=0
    f=0
    ''' 
    k= indiex of starting row
    l= index of starting column
    '''
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #printing the first row from the remaining rows
        for i in range(l,n):
            seurat.forward(dot_distance)
            
           # print(a[k][i],end=" ")
        k+=1
        f=1
        
        seurat.right(90)        
        #printing the last column from the remaining column
        for i in range(k,m):
            seurat.forward(dot_distance)
           #print(a[i][n-1],end=" ")
        
        n-=1
        seurat.right(90)
        
        
        if (k<m):
            #printing the last row from remaining rows
            for i in range(n-1,l-1,-1):
                #print(a[m-1][i],end=" ")
                seurat.forward(dot_distance)
                
            m-=1
        seurat.right(90)
        
        if (l<n):
            for i in range(m-1,k-1,-1):
                #print(a[i][l],end=" ")
                seurat.forward(dot_distance)
                
            l+=1
    

spiral(20,20)
turtle.done()
