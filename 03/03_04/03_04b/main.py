user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

#MY SOLUTION IS NOT WORKING, refer to 03_05e for correct solution
def update_preferences(user_pref):
    for key, value in user_pref.items():
        #print(f'key: {key}, value: {value}')
        if value == None:
            del user_pref[key]
        user_pref[key] = value
        
    return {user_pref}


print(update_preferences(user_preferences))
