Pour rouler le programme sur linux: 

\>> python3 ./compilateur.py -f ./programme.txt -o ./programme_comp

Pour le programme suivant:

SD    R2, R1 #15   
add   R1, R2  
MOv   R2, R1  
SUB   R1, R2  
MOV   PC,  R1  

L'output est:

9f9  
601  
905  
602  
105

Ne gère par les bits de drapeau!