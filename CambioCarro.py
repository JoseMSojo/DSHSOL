# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:13:52 2016

    Función de cambio de carro

@author: Jose Manuel Sojo Gordillo
"""

def CambiarCarro(Tp, wp, wp_Fin, T_amb, wp_0, t):
    
    if (wp[t,0]<=wp_Fin): # El carro ya esta seco
        Cambio = True
        N = len(Tp[1,:])-1
        for n in range(0,N):
            Tp[t,n] = Tp[t,n+1]
            wp[t,n] = wp[t,n+1]
            
        Tp[t,len(Tp[1,:])-1] = T_amb
        wp[t,len(Tp[1,:])-1] = wp_0
        
    else: # Si el carro no está seco, no se hace nada
        Cambio = False
        
    return (Cambio, Tp, wp)
