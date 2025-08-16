% Prolog facts for Bleeding-related First Aid Advice

% General advice for bleeding
advice(bleeding, 'Apply direct pressure with a clean cloth or bandage to stop the bleeding. If the bleeding doesn\'t stop, or is severe, call 1122 to seek medical help.').
advice(puncture_wound, 'Do not remove the object if it is still in place; stabilize it with cloths or bandages and seek medical help.').

% Advice for stopping bleeding
advice(stop_bleeding, 'Apply direct pressure to the wound. Seek medical help if the bleeding is severe, does not stop after 10 minutes of pressure, or if the wound shows signs of infection (redness, swelling, pus).').

% Advice for bleeding infection
advice(bleeding_infection, 'Cover the wound with a clean dressing or bandage, avoid direct contact with the wound, and seek medical attention to ensure proper wound care.').

% Advice for using a tourniquet
advice(use_tourniquet, [
    'Ensure Safety: Make sure the scene is safe for both you and the injured person.',
    'Apply Above the Wound: Place the tourniquet 2-4 inches above the injury site, but not directly over a joint.',
    'Tighten the Tourniquet: Tighten the tourniquet until the bleeding stops. You should be able to stop the bleeding without causing excessive pain or injury.',
    'Note the Time: Mark the time when the tourniquet was applied. Prolonged use may cause tissue damage.',
    'Monitor the Person: Keep the person calm and still while waiting for medical help to arrive.',
    'Seek Immediate Help: Call emergency services as soon as possible for advanced care.'
]).

% Advice for multiple bleeding wounds
advice(multiple_bleeding, 'Apply pressure to the most serious wound first, then move to the other wounds. Use tourniquets for life-threatening bleeding, and control bleeding with pressure and dressing.').

% Advice for shock related to bleeding
advice(shock_bleeding, 'If the person shows symptoms of shock like rapid heartbeat, low blood pressure, confusion, pale or cold skin, and shallow breathing, call 1122 immediately.').

% Advice for bleeding with fractures
advice(bleeding_fractures, 'Apply pressure to control bleeding, immobilize the fractured bone, and treat for shock.').

% Advice for bleeding from glass wounds
advice(bleeding_glass, 'Apply direct pressure to control bleeding, avoid removing any visible glass or debris, and cover the wound with a sterile dressing. Keep the person calm and seek medical attention for proper wound care and potential tetanus shots.').

% Queries to check for advice
get_advice(Symptom, Advice) :-
    advice(Symptom, Advice).

% Example usage:
% Query: Get advice for bleeding
% ?- get_advice(bleeding, Advice).
