def read_score_data(filename):
    # return a dictionary where each key is a resturant name 
    # and each corresponding value is the combined average score for that resturant.
    
    # The input file is a txt file with the following format:
    # resturant_name, score
    
    # If we have any errors reading the data we should raise an exception.

    # open the file and make sure it has the right format and data, or else we throw an exception
    try:
        with open(filename, 'r') as f:
            # create a dictionary to store the data
            scores = {}
            # loop through the file
            for line in f:
                # split the line on the comma
                line = line.split(',')
                # add the data to the dictionary
                scores[line[0]] = float(line[1])
            # return the dictionary
            return scores
    except:
        raise Exception('Error reading data. Each line of scores.txt should contain a restaurant name, followed by a comma, followed by a valid score, and no restaurant should appear more than once in the file.')

def top_n_restaurants(scores , n):
    # return a list of n tuples, each containing a single restaurant name and it's combined score, 
    # sorted by the combined score in descending order.

    # create a list to store the data
    top_n = []
    # loop through the scores dictionary
    for key, value in scores.items():
        # add the key and value to the list
        top_n.append((key, value))
    # sort the list by the value
    top_n.sort(key=lambda x: x[1], reverse=True)
    # return the top n items
    return top_n[:n]

print("Welcome to ReviewMe!\n\n1. Find the rating of a restaurant.\n2. List top n restaurants.\n3. Exit")

# get the users input
choice = input("What would you like to do? (Enter 1, 2 or 3): ")

# read the data
restaurant_scores = read_score_data("scores.txt")

# if the user wants to find the rating of a restaurant
if choice == "1":
    # get the restaurant name
    restaurant = input("Enter the name of the restaurant: ")
    # if the restaurant is in the dictionary, print the score
    if restaurant in restaurant_scores:
        print("Rating of " + restaurant + " is " + str(restaurant_scores[restaurant]))
    # otherwise, print an error
    else:
        print("We don't have a rating for " + restaurant)

# if the user wants to list the top n restaurants
elif choice == "2":
    # get the number of restaurants to list from the user
    print("How many restaurants would you like to list? ")
    # if the user inputs a non-integer or a negative, print an error
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            raise Exception
    except:
        print("Invalid value. Non-negative integer required.")
    # otherwise, print the top n restaurants
    else:
        # get the top n restaurants
        top_number = top_n_restaurants(restaurant_scores, n)
        # print the top n restaurants if the number of restaurants is more than the number in the dictonary, print the number of restaurants in the dictionary
        if n > len(restaurant_scores):
            print("The top " + str(len(restaurant_scores)) + " restaurants and their ratings are:")
            for item in top_number:
                # for every restaurant in the list, print the restaurant rank, name and the score
                print(str(top_number.index(item) + 1) + ". " + item[0] + " - " + str(item[1]))
        else:
            print("The top " + str(n) + " restaurants and their ratings are:")
            for item in top_number:
                # for every restaurant in the list, print the restaurant rank, name and the score
                print(str(top_number.index(item) + 1) + ". " + item[0] + " - " + str(item[1]))

# if the user wants to exit
elif choice == "3":
    # exit
    print("Goodbye!")
    exit()

# if the user inputs something that isn't 1, 2 or 3, print an error message
else:
    print("Invalid value. 1, 2 or 3 required.")