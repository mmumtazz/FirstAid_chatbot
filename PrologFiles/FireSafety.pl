% Fire Safety Facts
fire_safety('Install smoke detectors in every room and test them monthly.').
fire_safety('Never leave cooking unattended, and keep flammable items away from the stove.').
fire_safety('Keep matches and lighters out of reach of children.').
fire_safety('Don\'t overload electrical outlets and use extension cords safely.').
fire_safety('Have an escape plan and practice fire drills with your family regularly.').

% Kitchen Fire Safety Facts
kitchen_fire('Stay in the kitchen while cooking, especially when using high heat.').
kitchen_fire('Keep flammable items like paper towels and dish cloths away from the stove.').
kitchen_fire('Turn pot handles inward to prevent them from being knocked over.').
kitchen_fire('Never use water to put out grease fires; use a lid or baking soda instead.').
kitchen_fire('Keep a fire extinguisher nearby and know how to use it.').
kitchen_fire('Call 16 in case the fire is big or uncontrolled.').

% Fire Escape Plan Facts
escape_fire('Stay calm and do not panic.').
escape_fire('If possible, immediately call emergency services 16.').
escape_fire('Use a cloth to cover your nose and mouth to avoid inhaling smoke.').
escape_fire('If there is smoke, crouch low to the ground where the air is clearer.').
escape_fire('Do not use elevators during a fire; always use stairs to evacuate.').
escape_fire('Close doors behind you to slow the spread of the fire.').
escape_fire('Once outside, move away from the building and go to a designated safe area.').
escape_fire('Do not go back inside until it is declared safe by fire officials.').

% After Fire Facts
fire_aftermath('Contact 16 Immediately.').
fire_aftermath('Do not enter a fire-damaged building until it has been declared safe by authorities.').
fire_aftermath('Wear protective clothing and a mask if you need to enter a smoky or damaged area.').
fire_aftermath('Remove and clean items that have been affected by smoke or water damage.').
fire_aftermath('Seek support from local disaster relief services or community organizations.').
fire_aftermath('If trapped by the fire, enter a safe room and cover the bottom gap of the door with a blanket or rug.').
fire_aftermath('If you have access to a phone, call 995 and inform the operator of your location.').
fire_aftermath('If no phone is available, shout for help from the window and wait for help.').

% Types of Fires Facts
fire_types('Class A: Fires involving ordinary combustibles like wood, paper, or cloth.').
fire_types('Class B: Fires caused by flammable liquids such as gasoline, oil, or grease.').
fire_types('Class C: Electrical fires involving energized electrical equipment.').
fire_types('Class D: Fires involving combustible metals like magnesium, titanium, or sodium.').
fire_types('Class K: Fires that occur in cooking oils and fats, often found in commercial kitchens.').

% Fire Extinguisher Types Facts
fire_extinguisher('Water Extinguishers: Effective for Class A fires. They cool the burning material and prevent re-ignition.').
fire_extinguisher('Foam Extinguishers: Suitable for Class A and Class B fires. They create a barrier to smother the fire and prevent oxygen from fueling it.').
fire_extinguisher('Dry Chemical Extinguishers: Versatile for Class A, B, and C fires. They interrupt the chemical reaction that fuels the fire.').
fire_extinguisher('Carbon Dioxide (CO2) Extinguishers: Best for Class B and Class C fires. They displace oxygen and cool the fire by removing heat.').
fire_extinguisher('Wet Chemical Extinguishers: Designed for Class K fires. They create a soapy layer on top of the oil to cool it and prevent re-ignition.').
fire_extinguisher('Dry Powder Extinguishers: Used for Class D fires involving metals. They coat the burning metal and prevent oxygen from reaching it.').

% Proper Use of Fire Extinguishers
use_fire_extinguisher('Pull the pin to break the tamper seal.').
use_fire_extinguisher('Aim the nozzle at the base of the fire.').
use_fire_extinguisher('Squeeze the handle to release the extinguishing agent.').
use_fire_extinguisher('Sweep the nozzle from side to side until the fire is out.').

% General Query to Retrieve Fire Safety Tips
get_fire_safety_advice(Advice) :-
    fire_safety(Advice).

% General Query to Retrieve Kitchen Fire Safety Tips
get_kitchen_fire_advice(Advice) :-
    kitchen_fire(Advice).

% General Query to Retrieve Fire Escape Plan Tips
get_escape_fire_advice(Advice) :-
    escape_fire(Advice).

% General Query to Retrieve After Fire Tips
get_after_fire_advice(Advice) :-
    fire_aftermath(Advice).

% General Query to Retrieve Types of Fires
get_fire_types(FireType) :-
    fire_types(FireType).

% General Query to Retrieve Fire Extinguisher Types
get_fire_extinguisher_types(ExtinguisherType) :-
    fire_extinguisher(ExtinguisherType).

% General Query to Retrieve Fire Extinguisher Usage Instructions
get_fire_extinguisher_usage(Instruction) :-
    use_fire_extinguisher(Instruction).
