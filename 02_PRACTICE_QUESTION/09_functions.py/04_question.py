'''Number of Rounds of Lift'''

def number_of_rounds(total_height,height_per_round):
    if total_height % height_per_round == 0:
        return (total_height // height_per_round)
    else:
        return(total_height //height_per_round)+1
number_of_rounds(8,9)
print(number_of_rounds(20,4))