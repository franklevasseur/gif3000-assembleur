Pour rouler le programme sur linux: 

\>> python3 ./compilateur.py -f ./programme.txt -o ./programme_comp

Pour le programme suivant:

SD    R2, R1 #15
add   R1, R2
MOvC   R2, R1 -f
SUB   R1, R2
MOVNZ  PC,  R1

L'output est:

9F9
601
9E5
602
155

Pour rouler les tests, il faut installer pytest et lancer la commande suivante à la racine du repo:

\>> pytest

Aucune PR ne sera acceptée si tous les tests ne passent pas.

