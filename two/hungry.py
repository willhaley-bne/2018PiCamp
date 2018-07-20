import aiy.voicehat
import random
import json

def main():
    with open('hungry_list.json') as foods:
        lists = json.load(foods)

    food_lists = lists['foods']
    prep_lists = lists['preps']
    
    food_count = len(food_lists)
    prep_count = len(prep_lists)
    
    n = 0
    while n < 4:
      food_random_number = random.randint(0, food_count-1)
      prep_random_number = random.randint(0, prep_count-1)
    
      found_food = food_lists[food_random_number]
      found_prep = prep_lists[prep_random_number]
      
      print(found_prep)
      print(found_food)
      
      n = n + 1
  
if __name__ == '__main__':
    main()
    
    