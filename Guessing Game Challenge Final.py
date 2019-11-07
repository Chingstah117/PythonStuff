
# coding: utf-8

# In[1]:


from random import randint


# In[2]:


val = randint(1, 100)


# In[3]:


print("Welcome to the Guessing Game Challenge!\nThe Point of This Game is to Guess the Number in as Few Tries as Possible.")
print("The Number Will be Between 1 and 100. If Your First Guess is Within 10 of the Number, You Will be Told Warm. You will be Told Cold if More Than 10 Away.")
print("If Your Guess is Closer to the Number from Your Previous Guess, You Will be Told Warmer. You will be Told Colder if Not.")


# In[4]:


guesses = []
guess = int(input("Now, What is Your First Guess? "))
while 1 > guess or 100 < guess:
    print("OUT OF BOUNDS")
    guess = int(input("Try Again: "))
guesses.append(guess)
if guesses[-1] != val:
    if abs(val - guesses[-1]) <= 10:
        print("WARM!")
    else:
        print("COLD!")
dif = abs(val - guesses[-1])


# In[5]:


step = 1
while dif != 0:
    guess = int(input("What is Your Next Guess? "))
    while 1 > guess or 100 < guess:
        print("OUT OF BOUNDS")
        guess = int(input("Try Again: "))
    guesses.append(guess)
    step += 1
    temp = abs(val - guesses[-1])
    if temp != 0:
        if temp - dif < 0:
            print("WARMER!")
        else:
            print("COLDER!")
        dif = temp
    else:    
        dif = 0


# In[6]:


"You Guessed the Right Number! It Took You {} Guesses".format(step)

