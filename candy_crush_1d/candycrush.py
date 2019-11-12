
def crush(candy):
    # the unique crushable ones
    uniques = []

    # starting value and index
    last_value, starting_index = candy[0], 0

    # iteration of index and value to get the repeated
    for index, value in enumerate(candy):

        # check for repeating numbers
        if last_value != value:

            # if repeatition is greater and equal to 3
            if index - starting_index >= 3:
                # add to the unique and crushable
                uniques.append((value, starting_index, index))

            # update the starting index
            starting_index = index
        
        # update the last value checked
        last_value = value

    # end quickly if no crushable
    if len(uniques) == 0:
        return candy

    # keep track of the best option at every iteration and recursion
    final_candy = None
    min_candy = len(candy)

    # check all possible crush
    for (value, starting_index, ending_index) in uniques:
        # new candy found
        new_candy = crush(candy[:starting_index] + candy[ending_index:])

        # size of the tryout version
        size_of_current_candy = len(new_candy)

        # if the result is smaller than known minimum
        if size_of_current_candy < min_candy:
            min_candy = size_of_current_candy
            final_candy = new_candy.copy()
    
    # the final minimum result
    return final_candy

def main():
    candy = [1, 1, 3, 3,3, 2,2,2, 3, 1]
    lowest_return = crush(candy)
    print(lowest_return)

if __name__ == "__main__":
    main()
