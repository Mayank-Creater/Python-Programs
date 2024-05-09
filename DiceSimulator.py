import random 
import time
x = "y"
while x == "y":
    print("Rolling the dice...")
    time.sleep(0.5)
    n = random.choice([1,2,3,4,5,6])
    if n == 1:
        print ("    ")
        print ("  * ")
        print ("    ")
    elif n == 2:
        print (" * ")
        print ("    ")
        print ("     * ")
    elif n == 3:
        print ("   * ")
        print ("   * ")
        print ("   * ")
    elif n == 4:
        print ("   *    * ")
        print ("           ")
        print ("   *    * ")
    elif n == 5:
        print ("   *    * ")
        print ("      *     ")
        print ("   *    * ")
    elif n == 6:
        print ("   *    * ")
        print ("   *    * ")
        print ("   *    * ")



    x = input("Enter 'y' to roll again : ")
    print ("\n")