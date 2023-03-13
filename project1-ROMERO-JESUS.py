#Jesus Romero
#MCS 260 Spring 2022 Project 1
#I hereby attest that I have adhered to the rules for projects as well as UIC’s Academic Integrity standards while completing this project.

def SplitBinary():
    n = int(input("Enter the starting value: "))
    print(n)

    """At this point in the code, I have used the variable n to store the positive integer input. In order to turn the integer into binary, I used the bin() function and got rid of the 0b using [2:] because we know this is binary format and we dont need it. I then simply added a print function to print out the value of n."""

    List = []
    Counter = []
    List.append(n)

    """Here, I created a list named 'List' and another list named 'Counter'. I then added the input n, the value entered by the user, to the list named 'List'"""

    while (len(List)!=len(set(List)))!=True:

        """Here, I created a loop using the while function where the code continues to be executed as long as there are no duplicates in the the list "List". In order to do this, I had to make a Boolean that would come out true if the length of the list does not equal the length of the set of the list. I made the list into a set because in a set, there cannot be any duplicate elements. Using the "!=", meaning "not equal to", I set it so the code continues to run as long as the Boolean is not equal to True."""

        B = bin(n)[2:]

        """Here, I set B equal to the binary of the integer value n using the bin() function. The way I wanted the code to work, I didn't want the 0b in the beginning of the binary included in the binary numbers themselves. To resolve tis, I used [2:] in order to extract or remove the first two characters of B."""

        if(len(B)%2!=0):
            F = B[:len(B)//2]
            S = B[len(B)//2:]

            """Here, I created an if statement where if the length of the binary number modulo 2 is not equal to 0, then the following code is executed. I set F equal to the first half of B by dividing its length by 2. I then set S equal to the second half of B when diving by 2."""

            T = S[0]
            S = S[1:]
            F = F+T

            """Here, I needed to make it so that when an uneven binary number is divded into two parts, the extra digit goes to the first part. Since by default, the extra digit went to the second half, I set the variable T to the first character of S which has an index of 0. I then removed that first digit of S using [1:]. Lastly, I concatenated F and T and set that value equal to F. So in short, I took the first character from S and added it to T."""

            F = int(F,2)
            S = int(S,2)
            n = (F+1)*(S+1)

            """Here, I had to set the values of F and S back into integers because they had turned intro strings when I used the len() function in the earlier code. I also then set n equal to the product of F+1 and S+1."""

            List.append(n)
            print(n)
            Counter = len(List)

            """Here, I added the new value of n into the list "List" and printed that new value of n. Along with this, I set the value of Counter to the length of the list "List"."""
            
            if (Counter == 20):
                print("20 iterations and no duplicates")

                break

                """Here, when the length of the list reaches 20, that meaks Counter equal to 20 and we want the code to stop running if it has reached 20 iterations without a duplicate. I made an if statement where if the value of Counter was equal to 20, it would print out that there are 20 iterations without duplicates and then added a break in order for the loop to stop."""

        else:
            F = B[:len(B)//2]
            S = B[len(B)//2:]
            F = int(F,2)
            S = int(S,2)
            n = (F+1)*(S+1)
            List.append(n)
            print(n)
            Counter = len(List)
            if (Counter == 20):
                print("20 iterations and no duplicates")
                break

                """All of the above code is executed if the value B modulo 0 is equal to 0. I basically made this to run and do the same thing as the previous code but this takes numbers that the first if line wouldnt take such as 3."""

    else:
        print("Duplicate Found!")

        """This else code is executed if there the previous Boolean is equal to true. The Boolean determined if there was a duplicate in the list of values. This then prints that a duplicate is found and that is the end of the function SplitBinary()."""

SplitBinary()
