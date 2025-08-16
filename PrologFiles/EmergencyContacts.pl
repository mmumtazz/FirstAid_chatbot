% The fact name now directly matches the Python query.
get_emergency_number('police', 15).
get_emergency_number('fire', 16).
get_emergency_number('medical', 1122).
get_emergency_number('crime', 15).
get_emergency_number('fire_house', 16).
get_emergency_number('house_fire', 16).
get_emergency_number('emergency_remote', 1122).
get_emergency_number('road_accident', 1122).
get_emergency_number('fire_building', 16).
get_emergency_number('building_fire', 16).

% The fact name now directly matches the Python query.
get_emergency_advice('emergency', 'Dial 1122 for all emergency services in Pakistan.').
get_emergency_advice('police', 'The emergency number for the police in Pakistan is 15.').
get_emergency_advice('fire', 'Call 16 immediately and provide your exact location.').
get_emergency_advice('road_accident', 'Call 1122 and report the accident location.').