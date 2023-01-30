# LemkeHowson_Algorithm
Cet Algorithme n'est qu'une methode pour resoudre un jeu bimatriciel somme nulle sous forme strategique.
C'est un variant de la méthode LCP (linear complementarity problems), il sert a trouver un  equilibre de nash dans des jeux à plusieurs strategies.

# Pseudo Algorithme 
  - L'algorithme prend en entrée un jeu bimatriciel
  - retourne en sortie un equilibre de nash du jeu
  
![algorithme](https://user-images.githubusercontent.com/100075994/215502200-26c1ba75-3b17-4cad-a1d8-6bdea51ab37d.PNG)

# Explication du Code 
  - Dans notre code nous avons commencer par calculer les polytopes par resoudre un systèm d'équation à 2 inconnus (Dans ce cas nous avons traiter le jeu de matching pennies), 
  - puis nous avons afficher les deux graphes P et Q, en labelisant toute arc du graphe 
  - par la suite nous avons étiqueter chaque point d'intersection et stocker ces dernier dans des dictionnaires, contenant les coordonnées et les labels partagé
entre ces points. 
  -Nous avons initialiser l'etat de depart aux deux point avec les coordonnées (0,0) et commencer par supprimer le label 1
  - faire une première itteration.
  - repeter jusqu'a ce qu'on trouve le fully labeled vertex.
  
# Resultat 
  ### les graphe labelisé de P et Q 
  
![Figure_1](https://user-images.githubusercontent.com/100075994/215508268-f6f2eeb9-d3ed-481d-8664-4877ceae4993.png)
![Figure_Q](https://user-images.githubusercontent.com/100075994/215508358-048c8477-423c-4725-a964-85b51dfe3dd4.png)

  ### le premier resultat consiste a un affichage de polytopes et les etapes des itterations 
  
![Result1](https://user-images.githubusercontent.com/100075994/215507276-a4906c11-d8d0-43f0-ba04-52c6116ac9ed.PNG)

  ### deuxieme Resultat nous montre l'equilibre de nash obtenu par notre code et le test sur l'algorithme de la librairie nashpy
  
![Result2](https://user-images.githubusercontent.com/100075994/215507911-470cf495-5195-42a7-9bd8-fe3800ed86e0.PNG)
