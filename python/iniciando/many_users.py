# CONTINUAÇÃO DO CAPITULO 6 #

users = {
            'aeinstein':{
                            'first': 'Albert',
                            'last':  'Einstein',
                            'location': 'Princeton',
                        },

            'mcurie':   {
                            'first':'Marie',
                            'last': 'Curie',
                            'location': 'Paris',
                        }
        }


for username,user_info in users.items():
    
    print('\nusername: ' + username)
    fullname = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name : " + fullname.title())
    print("\tLocation: " + location.title())
