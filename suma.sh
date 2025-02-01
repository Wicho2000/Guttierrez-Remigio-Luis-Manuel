#!/bin/bash

num1=10
num2=5
num3=2
num4=3  # Nuevo número añadido

suma=$((num1 + num2))
resta=$((suma - num3))
multiplicacion=$((num1 * num4))  # Nueva operación multiplicación
division=$((num2 / num3))  # Nueva operación división

echo "La suma de $num1 y $num2 es $suma"
echo "La resta de $suma y $num3 es $resta"
echo "La multiplicación de $num1 y $num4 es $multiplicacion"
echo "La división de $num2 entre $num3 es $division"
