# FizzBuzz_Test
A short TDD project, testing a fizzbuzz function in python.

Ce projet consiste en une implémentation simple de la fonction fizzBuzz en utilisant Python. 
Il contient un fichier fizzbuzz.py , contenant la fonction fizzBuzz qui prend en paramètre un int, et un fichier test_fizzbuzz, qui teste cette même fonction.    
Dans le répertoire .github/workflows, vous trouverez un fichier yaml qui paramètre un workflow :
  A chaque push sur la branche main, toutes les actions décrites dans les "steps" du fichier se lanceront automatiquement.
  En l'occurence, j'ai choisi de garder toutes les steps basiques d'un build d'app pour les versions les plus utilisées de Python 3.
  Pour le projet, la step qui nous intéresse est située à "test with pytest" : Cette étape teste la fonction fizzbuzz.
  Il est possible de voir chaque run du workflow en allant dans l'onglet "actions" du projet sur github.                                                           
  Les workflows des branches ThomasChollet-patch-1 et 2 sont inutiles, mais j'ai décidé de les garder pour montrer l'avancement du projet. Les runs ne se faisaient pas automatiquement à chaque push car les fichiers n'étaient pas sur la branche main, mais sur des branches dédiées.

