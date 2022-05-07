from wsgiref.handlers import read_environ
hotels={
    "Lakewood":{
        "prices":{
            "Regular":{
                "week":110,
                "weekend":90
            },
            "Rewards":
            {
               "week":80,
               "weekend":80 
            }

        },
        "class":3
    },
      "Bridgewood":{
        "prices":{
            "Regular":{
                "week":160,
                "weekend":60
            },
            "Rewards":
            {
               "week":110,
               "weekend":50 
            }

        },
        "class":4
    },
      "Ridgewood":{
        "prices":{
            "Regular":{
                "week":220,
                "weekend":150
            },
            "Rewards":
            {
               "week":100,
               "weekend":40 
            }

        },
        "class":5
    },
}

def week_or_weekend(day):
  if(day=='sat' or day=='sun'):
    return "weekend"
  else:
    return "week"

def get_price(name_of_hotel,client_type,days_of_week):
    cost=0

    for day in days_of_week:
        cost+=hotels[name_of_hotel]['prices'][client_type][day]
    return cost
def get_cheapest_hotel(number):   #DO NOT change the function's name
    
   
    
    name_of_hotels=["Lakewood","Bridgewood","Ridgewood"]
    cheapest_hotel = "cheapest_hotel_name"
    class_cheapest_hotel=0
    
    #getting the client type 
    client_type=number.split(':')[0]
    
    #getting reservation days list 
    reservations_dates= number.split(':')[1].split(',')
    days_of_week= list(map(lambda day: day.split('(')[1].split(')')[0],reservations_dates))
    
    # define if it is a day week or a weekend
    days_of_week=list(map(week_or_weekend,days_of_week))
    
    cost=0
    
    for i,hotel in enumerate(name_of_hotels):
        aux=get_price(hotel,client_type,days_of_week)
        class_hotel=hotels[hotel]['class']
        if(i==0):
            cost=aux
            cheapest_hotel=hotel
            class_cheapest_hotel=class_hotel
        else:
            if(aux<cost):
                cost==aux
                cheapest_hotel=hotel
                class_cheapest_hotel=class_hotel
            elif (cost==aux):
                if(class_hotel>class_cheapest_hotel):
                    class_cheapest_hotel=class_hotel
                    cheapest_hotel=hotel

                

        

    
    return cheapest_hotel
