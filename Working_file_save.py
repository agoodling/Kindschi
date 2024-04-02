#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021-2022 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
import random
import asyncio
import re
import time


robot = Create3(Bluetooth()) 

 
ready = True
timer = True
running = True
battery_levels = []

gx_min = -80.0
gx_max = 80.0
gy_min = -80.0
gy_max = 80.0


oob_x = False
oob_y = False

count = 0

async def run(robot):
    IB = True
    oob_x = False
    oob_y = False
    restart = 0
    global count
    
    await robot.reset_navigation()
    randomStartAngle = random.randint(-180,180)
    await robot.turn_left(randomStartAngle)
    while True:
        restart = 0
        while IB == True:
            restart += 1
            await robot.move(3)
            battery = await robot.get_battery_level()
            x,y = get_x_y(robot)
            count += 1
            oob_x,oob_y = out_of_bounds(x, y ,oob_x,oob_y)
           
            if ((oob_x == True or oob_y == True) and restart > 4):
                IB = False 
                  
            print(x,y)

        await robot.turn_left(180)
        await robot.move(7)
        randomAngle = random.randint(-75,75)
        await robot.turn_left(randomAngle)
        oob_x = False
        oob_y = False
        IB = True
    
    print("completed with a count of:", count)
        
        

def get_x_y(robot):
    pose = str(robot.pose)
    pose_list = re.split(r'[(),\s°]+', pose)
    temp_x = pose_list[1]
    temp_y = pose_list[2]
    x = float(temp_x)
    y = float(temp_y)
    return x,y


def out_of_bounds(x,y,oob_x,oob_y):
    if not(gx_min <= x <= gx_max):
        oob_x = True
       
    if not (gy_min <= y <= gy_max):
        oob_y = True    

    return oob_x,oob_y


async def main(robot):
    global running
    try:
        await asyncio.wait_for(run(robot), timeout=600)
    except asyncio.TimeoutError:
        running = False

    print("program complete")

loop = asyncio.get_event_loop()
loop.run_until_complete(main(robot))


@event(robot.when_play)
async def play(robot):
    global running
    global battery_levels
    global count
    control = 0
    take = 100000
    while running:
        if(control ==take):
            battery = await robot.get_battery_level()
            battery_levels.append(battery[1])
            control = 0
        else:control +=1
        #print(control)
    
    print(battery_levels)
    print(count)
   

robot.play()
