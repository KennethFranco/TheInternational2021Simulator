# Dota 2's The International 2021 Main Event Simulator
![bracket](https://user-images.githubusercontent.com/83637447/136848215-85680693-d41c-4628-a222-1b06be406423.png)

Runs simulations for the entire bracket as seen above, with each simulation producing a winner for the entire tournament.
User can input the number of simulations he/she wishes to see using the first input line of the program.

All matches' winners are determined through Python's built in random module. Both teams acquire a random number and whichever team's number is higher is declared the winner of the match.

A win in the upper bracket sends you one round further than a win in the lower bracket would.
A loss in the upper bracket would send you down to the lower bracket while a loss in the lower bracket would eliminate the team from the tournament.

Each simulation prints out the winner of the tournament and after all simulations are done, the program prints out how many times each team won the entire tournament.
Lastly, the teams with the most and least wins are printed out respectively, showing their win rates out of the total simulations run.
