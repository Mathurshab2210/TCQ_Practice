from time import sleep

def run():
    print('Press enter to continue and ctrl+c to stop the second hand')
    atemp=1
    points=0
    points_table={}
    name=input("Enter name of player")
    while  True:
        try:
            for dig in range(1,13):
                print(dig)
                sleep(0.15)
        except KeyboardInterrupt:
            print(f'stopped at {dig}')
            print("points are added")
            sleep(1.1)
            if dig in [1,5,9,11]:
                points+=10
            elif dig in [4,7,8,10]:
                points+=20
            elif dig in [3,2,6,12]:
                points+=30
            atemp+=1
            if atemp ==4:
                print(f'{name} has scored {points} points')
                points_table[name]=points
                ch=input("Is there any other player(y/n)?").lower()
                if ch =='y':
                    name=input("Enter name of player")
                    atemp=1
                    points=0
                else:
                    print("Final result:",points_table)
                    return
                   
    
run()