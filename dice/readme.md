Week 3 dice game

I wrote this program twice, once using the incomplete template from BYU Idaho, and once from scratch.

In the template version, I mostly edited the dice.py file. However, I added one line of code in the do_updates function, and I modified do_outputs just a little as well.

These modifications fixed 2 bugs in the template:

-First, the score for each round was not being reset, so essentially the score was compounded and grew faster than it should. This bug was easy to squash.
-Second, the line "self.is_playing == (self.score > 0)" in do_outputs never seemed to do its job. Maybe I have a problem with my interpreter (I use 3.6 or 3.9). Instead I used the logic of if/else to end the game.

I also had some trouble with the Die class. For some reason, the roll method gave me an error if I referenced my dictionary variable from the constructor method without re-declaring it. I'm not sure why this happened, but this quirk did not affect my solution that I wrote from scratch.

My from-scratch solution is not as pretty as the template. The director (or game) class has fewer methods and does not follow best practices for clean code. Nevertheless, I am proud of how it turned out. Working with classes is fun!
