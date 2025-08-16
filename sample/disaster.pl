% Disaster preparedness facts

% General disaster preparedness
disaster_preparedness('disaster_preparedness', ['Create an emergency kit with essential items like water, food, first aid supplies, flashlight, batteries, and important documents.',
                                               'Have a family emergency plan that includes meeting places and contact information.',
                                               'Stay informed about potential disasters in your area by monitoring weather forecasts and alerts.',
                                               'Practice evacuation routes and emergency procedures regularly.',
                                               'Ensure all family members know how to respond during different types of disasters (e.g., earthquake, fire, flood).']).

% Earthquake preparedness
earthquake_preparedness('earthquake_preparedness', ['Secure heavy furniture and objects to the wall to prevent them from falling.',
                                                    'Identify safe spots in your home such as under sturdy tables or against interior walls.',
                                                    'Have an emergency kit with water, non-perishable food, first aid supplies, and a flashlight.',
                                                    'Practice "Drop, Cover, and Hold On" drills with your family.',
                                                    'Keep important documents and medications in an easy-to-access location.']).

% Fire preparedness
fire_preparedness('fire_preparedness', ['Install smoke alarms in key areas of your home and test them monthly.',
                                         'Create and practice a fire escape plan, including multiple routes out of the home.',
                                         'Keep fire extinguishers in accessible locations and know how to use them.',
                                         'Keep flammable items away from heat sources and never leave cooking unattended.',
                                         'Teach family members how to stop, drop, and roll if their clothes catch fire.']).

% Flood preparedness
flood_preparedness('flood_preparedness', ['Know if you live in a flood-prone area and have a plan to evacuate if necessary.',
                                           'Keep important documents, medications, and emergency supplies in a waterproof container.',
                                           'Raise electrical appliances and furniture above potential flood levels.',
                                           'Avoid driving or walking through flooded areas as water can be deeper than it appears.',
                                           'Listen to weather alerts and follow evacuation orders promptly.']).

% Tornado preparedness
tornado_preparedness('tornado_preparedness', ['Identify the safest room in your home, such as a basement or an interior room without windows.',
                                               'Have a weather radio and stay informed about tornado warnings and updates.',
                                               'Keep an emergency kit with food, water, first aid, flashlight, and battery-operated radio in your safe room.',
                                               'Practice tornado drills with your family so everyone knows what to do.',
                                               'Protect your head and neck with a sturdy object or pillow during a tornado.']).

% Hurricane preparedness
hurricane_preparedness('hurricane_preparedness', ['Stock up on water, non-perishable food, batteries, and medical supplies at least a week in advance.',
                                                  'Know your evacuation routes and have a plan in place to leave early if necessary.',
                                                  'Secure outdoor objects that could become projectiles in high winds.',
                                                  'Protect your windows with storm shutters or heavy-duty tape.',
                                                  'Keep important documents and valuables in a waterproof container.']).

% Power outage preparedness
power_outage_preparedness('power_outage_preparedness', ['Have a supply of batteries, flashlights, and candles on hand.',
                                                         'Keep a stock of non-perishable food and water for at least three days.',
                                                         'Charge essential electronics ahead of time, such as phones and power banks.',
                                                         'Know how to manually open electric garage doors and keep warm blankets available.',
                                                         'Avoid opening the refrigerator and freezer to keep food cold longer.']).

% Pandemic preparedness
pandemic_preparedness('pandemic_preparedness', ['Stock up on essential supplies such as food, water, medications, and hygiene items.',
                                                 'Maintain good hygiene practices, such as washing hands regularly and wearing masks if needed.',
                                                 'Have a communication plan to stay in touch with family and friends.',
                                                 'Follow public health guidelines and be prepared to work or study from home if necessary.',
                                                 'Stay informed with updates from reliable health sources.']).

% Grandparents' preparedness tips
grandparents_preparedness('grandparents_preparedness', ['Ensure your home is safe by checking for hazards like loose rugs and electrical cords.',
                                                        'Keep a phone with emergency contacts programmed.',
                                                        'Stock up on medications and have an extra set of glasses or hearing aids.',
                                                        'Have a list of important medical information and allergies.',
                                                        'Practice emergency drills with your family members to ensure everyone knows how to help you if needed.']).

% General safety tips for disasters
safety_tips('safety_tips', ['Always be prepared for emergencies by keeping an emergency kit, having a plan, and staying informed.',
                            'Ensure all family members know what to do and practice drills for different types of disasters.']).

% Prolog rules for querying disaster preparedness
prepare_for_disaster(X):- disaster_preparedness(X,_).
prepare_for_earthquake(X):- earthquake_preparedness(X,_).
prepare_for_fire(X):- fire_preparedness(X,_).
prepare_for_flood(X):- flood_preparedness(X,_).
prepare_for_tornado(X):- tornado_preparedness(X,_).
prepare_for_hurricane(X):- hurricane_preparedness(X,_).
prepare_for_power_outage(X):- power_outage_preparedness(X,_).
prepare_for_pandemic(X):- pandemic_preparedness(X,_).
prepare_for_grandparents(X):- grandparents_preparedness(X,_).
prepare_for_safety(X):- safety_tips(X,_).
