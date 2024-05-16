import numpy as np

#Set the seed
np.random.seed(100)

#Generate and print random float
print(np.random.rand())

# Import numpy and set seed
import numpy as np
np.random.seed(100)

# Use randint() to simulate a dice
dice = np.random.randint(1, 7)
print(dice)
# Use randint() again
dice = np.random.randint(1, 7)
print(dice)

# Starting step
step = 40

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif 3 <=dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)

# Initialize random_walk
random_walk = [0]

# Complete the for loop
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Adding a title to the plot
plt.title("The random walk of one set of 100 steps")

# Adding and styling axis labels
plt.xlabel('The number of steps', fontweight='bold')
plt.ylabel('Accumulated steps taken up Empire State Building', style='italic', loc='bottom')

# Show the plot
plt.show()

# Initialise an empty list to store all the walks
all_walks = []

# Simulate random walk five times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
# print(all_walks)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)

plt.ylabel("Total number of steps after 100 throws")
plt.xlabel("The resultant of 10 walks")

plt.title("The 10 random walks for 100 steps")

plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)

plt.xlabel("Total number of steps taken")
plt.ylabel("The resultant step achieved after 100 throws")

plt.title("The resultant step achieved after 100 throws for 10 random walks")

plt.show()

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)

plt.xlabel("Total number of steps taken")
plt.ylabel("The resultant step achieved after 100 throws")

plt.title("Step achieved after 100 throws for 10 random walks with jeopardy")

plt.show()

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 500 times
all_walks = []
for i in range(10000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)

#Add axis titles and a main title
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.title("Random Walk Simulation")

plt.show()

probability = np.count_nonzero(ends >= 60) / len(ends)

percentage = probability * 100

print(f"The estimated chance of reaching at least 60 steps high (with 1% jeopardy) is approximately{percentage: }%.")
