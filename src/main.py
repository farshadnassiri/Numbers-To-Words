from constants import TENS, UNDER_20, ABOVE_100


def num_to_word(num):
    if num<20:
        return UNDER_20[num]

    if num >= 20 and num < 100:
        if num%10 == 0:
         return TENS[num//10] 
        return TENS[num//10]+(" "+ UNDER_20[num%10])

    if num >= 100:
        pivot=max([key for key in ABOVE_100 if num >= key])
        if num%pivot == 0:
            return  UNDER_20[num//pivot]+" "+ABOVE_100[pivot]
        return UNDER_20[num//pivot]+" "+ABOVE_100[pivot]+" "+num_to_word(num%pivot)  

if __name__ == "__main__":

    while True:
        num=input("Please enter your number:")

        try:

            if num.upper() == "Q":
                print("Good bye!")
                break
            num=int(num)    
            if num >= 0 and num <= 1000000000:
                print(num_to_word(num))
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Numbers Only Please!!!")   

   