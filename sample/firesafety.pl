% Fire Safety Facts

% General Fire Safety Tips
fire_safety_tips(general, [
    'Install smoke detectors in every room and test them monthly.',
    'Never leave cooking unattended, and keep flammable items away from the stove.',
    'Keep matches and lighters out of reach of children.',
    'Don\'t overload electrical outlets and use extension cords safely.',
    'Have an escape plan and practice fire drills with your family regularly.'
]).

% Kitchen Fire Safety
fire_safety_tips(kitchen, [
    'Never leave cooking unattended.',
    'Keep flammable items away from the stove, oven, and grill.',
    'Clean cooking surfaces regularly to avoid grease buildup.',
    'Ensure electrical cords and wires are not near heat sources.'
]).

% Electrical Fire Safety
fire_safety_tips(electrical, [
    'Do not overload electrical outlets.',
    'Unplug electrical appliances when not in use.',
    'Use extension cords sparingly and safely.',
    'Ensure wiring is in good condition, and repair or replace damaged cords.'
]).

% Home Heating Fire Safety
fire_safety_tips(heating, [
    'Keep heating equipment like space heaters and fireplaces at least 3 feet away from flammable materials.',
    'Never leave a space heater running unattended.',
    'Ensure chimneys are cleaned and maintained regularly.'
]).

% Smoking Fire Safety
fire_safety_tips(smoking, [
    'Never smoke in bed or when drowsy.',
    'Always extinguish cigarettes in a proper container, not a trash can.',
    'Keep matches and lighters away from children.'
]).

% Pet Fire Safety
fire_safety_tips(pets, [
    'Keep pets away from cooking areas and open flames.',
    'Ensure electrical cords are out of their reach.',
    'Have a plan to evacuate your pets in case of fire.'
]).

% Fire Escape Plan Tips
fire_safety_tips(escape_plan, [
    'Create a fire escape plan with at least two exits from each room.',
    'Practice your fire escape plan regularly with all family members.',
    'Make sure everyone knows how to use fire alarms and extinguishers.'
]).

% Dealing with Fire in the Home
fire_safety_tips(dealing_with_fire, [
    'If you are trapped, stay low to the ground to avoid smoke inhalation.',
    'Stop, drop, and roll if your clothes catch fire.',
    'Use a fire extinguisher only if the fire is small and manageable.'
]).

% High-Risk Areas Fire Safety
fire_safety_tips(high_risk_areas, [
    'Avoid storing flammable materials in areas with high fire risk.',
    'Ensure fire extinguishers and fire alarms are easily accessible.',
    'Check for local fire safety regulations in high-risk areas.'
]).

% Camping Fire Safety
fire_safety_tips(camping, [
    'Always extinguish campfires completely before leaving or sleeping.',
    'Never leave a fire unattended while camping.',
    'Make sure campfires are away from tents and flammable materials.'
]).

% Fire Safety for the Elderly
fire_safety_tips(elderly, [
    'Install smoke detectors in their homes.',
    'Ensure they have a clear path to exit in case of fire.',
    'Regularly check that their fire extinguishers and alarms are in working order.'
]).

% Fire Safety for Children
fire_safety_tips(children, [
    'Teach children about fire safety, including stop, drop, and roll.',
    'Keep matches, lighters, and candles out of reach.',
    'Create a fire escape plan and practice it with children.'
]).

% After a Fire
fire_safety_tips(after_fire, [
    'Ensure the fire is completely out before re-entering the building.',
    'Check for structural damage or hazards before returning.',
    'Contact the fire department to assess the safety of the area.'
]).

% Fire Safety for Businesses
fire_safety_tips(businesses, [
    'Have an emergency evacuation plan in place.',
    'Ensure all employees are trained on fire safety.',
    'Regularly check fire extinguishers and alarms.'
]).

% Holiday Season Fire Safety
fire_safety_tips(holidays, [
    'Ensure Christmas trees are watered regularly and away from heat sources.',
    'Check holiday lights for damaged cords before using them.',
    'Keep candles away from decorations and unattended.'
]).

% Outdoor Grilling Fire Safety
fire_safety_tips(grilling, [
    'Never grill indoors or in an enclosed space.',
    'Keep the grill away from flammable materials.',
    'Never leave a hot grill unattended.'
]).

% Emergency Contact Tips
fire_safety_tips(emergency_contact, [
    'Have emergency contact numbers clearly visible.',
    'Ensure all family members know the number for the fire department.',
    'Provide emergency contact information to caregivers, teachers, and others.'
]).

% Types of Fires
fire_safety_tips(fire_types, [
    'Class A: Ordinary combustibles like wood and paper.',
    'Class B: Flammable liquids such as gasoline and oil.',
    'Class C: Electrical fires.',
    'Class D: Combustible metals like magnesium and sodium.'
]).

% Fire Extinguisher Types
fire_safety_tips(extinguisher_types, [
    'Water (Class A fires)',
    'Foam (Class A and B fires)',
    'Dry Chemical (Class A, B, and C fires)',
    'CO2 (Class B and C fires)',
    'Wet Chemical (Class K fires)'
]).

% Using Fire Extinguishers
fire_safety_tips(using_extinguisher, [
    'Pull the pin, aim at the base of the fire, squeeze the handle, and sweep from side to side.'
]).

% Maintaining Fire Extinguishers
fire_safety_tips(maintaining_extinguisher, [
    'Check pressure regularly and ensure the pin is intact.',
    'Inspect for any visible damage and ensure it is easily accessible.',
    'Have it serviced annually.'
]).

% Choosing the Right Fire Extinguisher
fire_safety_tips(choosing_extinguisher, [
    'Choose the appropriate fire extinguisher based on the fire type.',
    'Ensure the fire extinguisher is large enough for the area and hazards.',
    'Check that the extinguisher is easy to access and operate.'
]).

% Rule to get fire safety tips based on category
get_fire_safety_tips(Category, Response) :-
    fire_safety_tips(Category, Response).

