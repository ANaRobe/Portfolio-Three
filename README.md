# Harap Alb


Harap Alb is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
 
The cult fairytale ["Harap Alb"](https://en.wikipedia.org/wiki/Harap_Alb#:~:text=Harap%20Alb%20in%20Romanian%20signifies,man%2C%20usually%20with%20dark%20features.) by Ion Creanga (Romanian author) had inspired this text-based  game.

A deployed link to the website can be found [here](https://harapalb.herokuapp.com/)


## How To Play

When launching the app the INTRO (resume of the tale's introduction) is displayed. This introduce the user to the theme of the game and inquiers the user if he wants to play.

 If yes the GAME will START with ROUND ONE. If no The GAME OVER will be displayed.
 
The aim of the game is to assist the young prince to go and merry the Green Emperor's daughter in order to inherit his Kingdom. 

The player will first choose the protagonist and then help him to take decisions along the way in order to get to The Other Edge Of The World.

The focus is on the youngest son, therefore he is the right character to choose to play with. He will go through many different challenges in his journey. Our game has for rounds and every wrong choice will lead to the end of the game.

If the user decides that the oldest son of the King should go and merry the princess, he will get on a dead end road where the oldest son will fail the the 'fight with the Bear' test and 'Game Over' will follow. 


## Logic Flow Chart
![alt text](/img/CHART.png)


## Current Features


- Accepts user input

- Reads input 

- Manipulates data

- Input validation 

- Rising errors (including blankspaces inputs):

All answeres are checked to ensure the user inputs information where requested before the game continues and should any incorect data be used, the user is provided with feedback on what has gone wrong and the question is asked again.

- Questions with 2 options to choose from:

There is always a right (which takes the player to the next ROUND) path or a wrong path (which ends with GAME OVER).

- Input of words in a template with the purpose to create a magic phrase:

The first  and third round challenges are the player requesting to add some words to a magic phrase in order to break out a spell.

- Guessing a randomly generated number:

When reaching the final round, the user is asked to guess a number between 1 and 3 which was randomly generated. If the user guesses the number the Gates of the of the Kingdom will open and the protagonist will get to the next level. 


## Technologies Used

### Languages Used
- Python

### Python Packages
- Colorama Text in terminal are shown in different colours.
- Random returns a random integer.
- Time used for print effect delay.

### Tools
- Heroku was used to deploy the live project.
- Patorjk was used to generate Ascii Art.
- PEP8 online was used to validate Python code.
- https://www.lucidchart.com/ was used to create the Flowchart.
- The top screen shot for responsive design was taken from: https://ui.dev/amiresponsive
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- GitHub GitHub is used to store the projects code after being pushed from Git.
- Gitpod An online IDE linked to the GitHub repository used to write my code.