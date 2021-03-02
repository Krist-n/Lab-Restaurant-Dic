
def creating_dict_restaurant_ratings(file_name):
    """Restaurant rating lister."""
    
    data_file = open(file_name)

    restaurant_ratings = {}

    for line in data_file:
        lines_cleaned = line.rstrip().split(":")
        restaurant_ratings[lines_cleaned[0]] = lines_cleaned[1]
    
    new_restaurant = input("Enter restaurant name: ")
    new_rating = input("Enter restaurant rating: ")

    restaurant_ratings[new_restaurant] = new_rating


        
      
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(f"{restaurant} is rated at {rating}.")

    
   

 
        
creating_dict_restaurant_ratings('scores.txt')
