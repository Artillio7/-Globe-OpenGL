# PyOpenGLobe - Projet de Synthèse d'Images

Un rendu OpenGL 3D d'une sphère avec une texture terrestre appliquée dans une fenêtre PyGame. Ce projet personnel vise à explorer les bases d'OpenGL et de PyGame. J'ai choisi d'utiliser PyGame pour afficher la sphère, plutôt que PyOpenGL lui-même, car cela m'a permis de prendre en compte l'entrée de l'utilisateur pour faire pivoter la sphère et effectuer un zoom avant et arrière.

## Utilisation

1. Exécutez la commande suivante dans votre terminal pour installer Pygame :

2. Après l'installation de Pygame, exécutez le fichier "globe.py" de la manière habituelle pour exécuter les fichiers Python.

## Caractéristiques

- Affiche une sphère rendue en OpenGL dans une fenêtre PyGame.
- La sphère a une texture terrestre mappée de manière sphérique.
- Rotation de la sphère avec les touches fléchées ou en cliquant et en faisant glisser avec la souris.
- Zoom avant et arrière avec la molette de la souris.

## Captures d'écran![Capture d'écran](https://user-images.githubusercontent.com/40459599/53302550-80756c00-3857-11e9-9474-9cee0f51d19c.png)

## Prérequis

- Python 3
- PyGame
- PyOpenGL
- PIL ou Pillow
- Numpy

## Points Forts

J'ai appris beaucoup sur le rendu d'objets 3D en OpenGL. La création de la sphère et son affichage dans une fenêtre PyGame était relativement simple. Le défi résidait dans l'application d'une texture à la sphère. J'ai également eu des difficultés avec le code de clic et de glissement qui permet à l'utilisateur de faire pivoter la sphère à l'aide de la souris. Certaines réponses très utiles de StackOverflow m'ont aidé à implémenter ces fonctionnalités.

J'ai appris comment PyGame intercepte les entrées utilisateur sous forme d'événements et comment les utiliser pour contrôler la manière dont la sphère est rendue. Initialement, ce programme s'exécutait très lentement sur mon ordinateur car je n'avais pas correctement optimisé le code et il rendait nécessairement la sphère à chaque trame. Après quelques optimisations, le programme fonctionne maintenant correctement, et la sphère peut être manipulée en douceur chez vous M.

## Sources

- Un excellent tutoriel que j'ai utilisé pour commencer avec PyOpenGL : [Lien vers le tutoriel](https://www.youtube.com/watch?v=R4n4NyDG2hI)
- Texturer une sphère depuis : [Lien vers la source](https://stackoverflow.com/questions/42986754/pyopengl-sphere-with-texture?answertab=oldest#tab-top)
- Clic et glissement depuis : [Lien vers la source](http://goldsequence.blogspot.com/2017/04/using-mouse-for-object-zoom-inzoom.html)
- Image de texture depuis : [Lien vers la source](http://planetpixelemporium.com/earth.html)
