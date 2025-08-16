% Prolog facts for First Aid Tips

% First Aid Definition
first_aid('First aid is the initial assistance or treatment given to a person who is injured or suddenly becomes ill, before professional medical help arrives or the person can get to a healthcare facility. It aims to preserve life, prevent further harm, and promote recovery.').

% First Aid Tips for Fracture
fracture_tips([
    'Keep the affected limb as still as possible.',
    'Apply a splint if you are trained to do so.',
    'Elevate the limb to reduce swelling.',
    'Apply ice (wrapped in a cloth) for 15-20 minutes to reduce swelling and pain.',
    'Seek medical attention immediately for a proper diagnosis and treatment.'
]).

% First Aid Tips for Insect Bite
insect_bite_tips([
    'Clean the bite area with soap and water.',
    'Apply an anti-itch cream or an ice pack to reduce swelling and discomfort.',
    'Take over-the-counter antihistamines if you experience itching or swelling.',
    'Watch for signs of severe reactions such as difficulty breathing or swelling around the eyes and lips, and seek medical help if needed.'
]).

% First Aid Tips for Poisoning
poisoning_tips([
    'Call emergency services immediately.',
    'If the person is conscious and alert, try to find out what poison was ingested.',
    'Do not induce vomiting unless directed by a healthcare professional.',
    'If the poison was a chemical or toxin on the skin, remove contaminated clothing and rinse the skin with water for 15-20 minutes.'
]).

% First Aid Tips for Asthma Attack
asthma_attack_tips([
    'Help the person sit up and remain calm.',
    'Encourage them to use their prescribed inhaler or medication.',
    'If the symptoms persist for more than 5-10 minutes, seek emergency medical assistance.',
    'Make sure they are in a well-ventilated space and remove any known triggers if possible.'
]).

% First Aid Tips for Seizures
seizure_tips([
    'Move any nearby objects that could cause injury.',
    'Place a soft cushion or clothing under their head to prevent injury.',
    'Time the duration of the seizure.',
    'Do not hold them down or try to put anything in their mouth.',
    'Stay with them until the seizure ends and they are fully alert.',
    'Seek medical help if the seizure lasts longer than 5 minutes or if another seizure follows immediately.'
]).

% First Aid Tips for Nosebleed (More Detail)
nosebleed_tips([
    'Keep pinching your nostrils together while leaning slightly forward.',
    'If bleeding persists for more than 20 minutes, seek medical attention.',
    'Avoid blowing your nose for several hours after the bleeding stops.',
    'Apply a nasal saline spray or use a humidifier to prevent nosebleeds from recurring.'
]).

% First Aid Tips for Sunburn
sunburn_tips([
    'Drink plenty of fluids to stay hydrated.',
    'Apply aloe vera gel or an over-the-counter hydrocortisone cream to soothe the skin.',
    'Take a cool bath or use a cool compress to reduce discomfort.',
    'Avoid further sun exposure until the skin heals.',
    'If blistering occurs or the pain is severe, consult a doctor.'
]).

% First Aid Tips for Bee Sting
bee_sting_tips([
    'Remove the stinger by scraping it off with a flat object (e.g., a credit card).',
    'Clean the area with soap and water.',
    'Apply an ice pack to reduce swelling and pain.',
    'Take an antihistamine if you experience swelling or itching.',
    'Seek medical attention if you experience difficulty breathing, swelling in the throat, or other severe allergic reactions.'
]).

% General First Aid Reminder
general_first_aid_reminder([
    'Always keep a first aid kit stocked with essential items like bandages, antiseptic wipes, tweezers, and pain relievers.',
    'Wash your hands before and after giving first aid, and make sure to seek medical attention for serious injuries or if symptoms worsen.'
]).

% First Aid Tips for Head Injury
head_injury_tips([
    'If the injury is minor, apply a cold pack to the area to reduce swelling.',
    'Monitor the person for symptoms of a concussion (dizziness, headache, confusion).',
    'Seek medical attention immediately if there is loss of consciousness, vomiting, or severe pain.'
]).

% First Aid Tips for Heart Attack
heart_attack_tips([
    'Call emergency services immediately.',
    'Keep the person calm and help them sit down in a comfortable position.',
    'Have them chew or swallow an aspirin if they are not allergic.',
    'If the person is conscious and alert, encourage them to take slow, deep breaths.',
    'If they lose consciousness, start CPR if you are trained.'
]).

% First Aid Tips for CPR
cpr_tips([
    'Check responsiveness: Tap and shout to see if they respond.',
    'Call for help: Call 911 or your local emergency number.',
    'Start chest compressions: Place your hands, one on top of the other, in the center of the chest and press down hard and fast (at least 2 inches deep at a rate of 100-120 compressions per minute).',
    'Provide rescue breaths: Give 2 breaths after every 30 compressions.',
    'Continue CPR until professional help arrives or the person starts breathing.'
]).

% First Aid Safety Reminder
first_aid_safety_reminder([
    'Always stay calm and assess the situation before taking action.',
    'Keep a first aid kit with essential items readily available and know how to use its contents.',
    'Seek professional medical assistance for serious injuries or conditions.'
]).

% First Aid Tips for Drowning
drowning_tips([
    'Call emergency services immediately.',
    'If the person is not breathing, start CPR immediately.',
    'Check the airway for obstruction and remove any debris.',
    'If the person is breathing, keep them warm and monitor their condition until help arrives.'
]).

% First Aid Tips for Diabetic Emergency (Low Blood Sugar)
diabetic_emergency_tips([
    'If the person is conscious, give them a fast-acting carbohydrate (e.g., fruit juice, glucose tablet).',
    'If the person is unconscious, do not attempt to give them anything by mouth.',
    'Call emergency services immediately if the person does not improve or loses consciousness.',
    'Monitor their condition and be prepared to assist with CPR if necessary.'
]).

% First Aid Tips for Severe Allergic Reaction (Anaphylaxis)
severe_allergic_reaction_tips([
    'Call emergency services immediately.',
    'If available, administer an epinephrine injection (EpiPen).',
    'Keep the person calm and help them lie down with their legs elevated.',
    'If the person has difficulty breathing, assist them in using an inhaler if they have one.',
    'Monitor for signs of shock and perform CPR if the person stops breathing.'
]).

% First Aid Tips for Choking
choking_tips([
    'If the person can cough, encourage them to cough forcefully.',
    'If they cannot cough or speak, perform the Heimlich maneuver (abdominal thrusts).',
    'For infants, use back blows and chest thrusts.',
    'If the person becomes unconscious, begin CPR and call for emergency help immediately.'
]).

% Rule to get first aid tips for choking
get_first_aid_tips('what should i do if someone is choking', Tips) :-
    choking_tips(Tips).

% First Aid Tips for Heat Stroke
heat_stroke_tips([
    'Move the person to a cooler place, preferably an air-conditioned environment.',
    'Remove excess clothing and try to cool the body with cool (not cold) water.',
    'Offer cool water or electrolytes if the person is conscious and able to drink.',
    'Seek immediate medical help, especially if the person becomes confused or loses consciousness.'
]).

% Rule to get first aid tips for heat stroke
get_first_aid_tips('what should i do for heat stroke', Tips) :-
    heat_stroke_tips(Tips).


% Rule to get first aid tips for a severe allergic reaction
get_first_aid_tips('what should i do for a severe allergic reaction', Tips) :-
    severe_allergic_reaction_tips(Tips).


% Rule to get first aid tips for a diabetic emergency
get_first_aid_tips('what should i do for a diabetic emergency', Tips) :-
    diabetic_emergency_tips(Tips).

% Rule to get first aid tips for drowning
get_first_aid_tips('what should i do if someone is drowning', Tips) :-
    drowning_tips(Tips).

% Rule to get first aid tips for a given question
get_first_aid_tips('what should i do for a fracture', Tips) :-
    fracture_tips(Tips).

get_first_aid_tips('what should i do for an insect bite', Tips) :-
    insect_bite_tips(Tips).

get_first_aid_tips('what should i do for poisoning', Tips) :-
    poisoning_tips(Tips).

get_first_aid_tips('what should i do for an asthma attack', Tips) :-
    asthma_attack_tips(Tips).

get_first_aid_tips('what should i do for seizures', Tips) :-
    seizure_tips(Tips).

get_first_aid_tips('what should i do for a nosebleed', Tips) :-
    nosebleed_tips(Tips).

get_first_aid_tips('what should i do for a sunburn', Tips) :-
    sunburn_tips(Tips).

get_first_aid_tips('what should i do for a bee sting', Tips) :-
    bee_sting_tips(Tips).

get_first_aid_tips('what is first aid', Tips) :-
    first_aid(Tips).

% Other queries can be added in a similar fashion for different first aid topics
