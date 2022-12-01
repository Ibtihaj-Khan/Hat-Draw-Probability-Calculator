FreeCodeCamp Probability calculator project.

The ask:
Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? 

There could be any given set of data for Hat Object or expected draw, and number of balls drawn per experimental run.

Definitions and Approach:
#Hat Class
    -Initializes with any number of args (the balls and number of balls in hat)
        *We iterate over this and create a list of all the ball colors, so we have one list element for each ball.
    -Has a draw method which builds a new list of drawn balls, and removes those balls from from the list.
        *Approach here was to pick random index, append that index's value to output, pop that index from the inputs list.

#Experiments Functions
    **We create Vars outside of the experiments loop to track total runs and successes in loop.
    -Takes in a hat object, and creates a Deep Clone of it so it is unique reference.
    -Run the draw method for the clone, then build a histogram for this returned list.
    -Start iterating over the expected balls dictionary:
        -If any of the keys in the expected output arent in out experimental histo, break out of this cycle (this key,value pair of expected balls).
        -If the value of the expected draw is greater than the value from our experiment, break out of this cycle.
        -If neither of the conditions above are met, this means we completed the loop with all expected keys existing in our experiment histogram, and each value was less than or equal our experimental histogram.
            -This means that our histogram had all the keys, and each key value was more than what we are predicting for, and by extension that means the expected draw is within the actual draw.
            -In this case, we increment our success Variable M 

    -Finally, we return total probability Successes / Total draws or M/N

