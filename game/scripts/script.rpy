label splashscreen:
    show splash_image
    $ renpy.pause()
    return

# The game starts here.
label start:
    
    #relationship_tracking
    $ relationships = {'atv': 0,
                   'katie': 0,
                   'gator': 0,
                   'snake': 0,
                   'brian': 0,
                   'bj': 0,
                   'flareon': 0
                  }

    stop music
    $ day = Day()
    
    call introduction

    while day.dayNum <= 30:
        
        #Say what day it is.
        show rj
        "It was [day.dayString]"

        "We had classes in the morning."

        scene placeholder_lunch
        if day.dayNum == 1:
          call day_1_lunch
        else:
          "Lunch went by like it always does..."
        scene
  

        show rj
        "Then we had afternoon classes, and then I went home and went to bed."      
        #Call anything that happens prior to the day starting. ie. Day planners
        
        
        # Call anything that happens after the day. ie. Day summaries

        if day.weekdayNum == 5:
            "Another week has come and gone."
        
        # Increment to the next day.
        $ day.nextDay()
        
    
    "The game has ended. Time has run out."
    
    return

