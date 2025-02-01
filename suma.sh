#!/bin/bash

echo -n "Ingresa el primer numero: "
read num1

<<<<<<< HEAD
echo -n "Ingresa el segundo numero: "
read num2

suma=$((num1 + num2))
resta=$((num1 - num2))

echo "La suma de $num1 y $num2 es: $suma"
echo "La resta de $num1 menos $num2 es : $resta"
=======
suma=$((num1 + num2))
resta=$(($suma - num3))
echo "La suma de $num1 y $num2 es $suma"
echo "La resta de $suma y $num3 es $resta"

>>>>>>> cf55386 (Guardando cambios antes de hacer pull)
