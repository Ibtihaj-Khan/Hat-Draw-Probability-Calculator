import prob_calculator

prob_calculator.random.seed(95)

hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)

probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

