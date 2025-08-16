% First Aid Facts
first_aid_advice(bleeding, 'Apply direct pressure to the wound with a clean cloth or bandage to stop the bleeding.').
first_aid_advice(severe_bleeding, 'Call emergency services immediately. Use a tourniquet only if trained.').
first_aid_advice(burn, 'Cool the burn under running water for at least 10 minutes. Do not apply creams or break blisters.').
first_aid_advice(choking, 'Perform the Heimlich maneuver if the person is conscious. If unconscious, call emergency services immediately.').
first_aid_advice(sprain, 'Rest the injured area, apply ice, compress with an elastic bandage, and elevate the limb.').
first_aid_advice(fracture, 'Immobilize the affected area and seek medical attention immediately. Avoid moving the injured limb unnecessarily.').
first_aid_advice(nosebleed, 'Lean forward slightly and pinch the soft part of the nose for 10 minutes. Avoid tilting the head back.').

% Symptom-Specific Advice
first_aid_advice(fever, 'Stay hydrated and rest. Use over-the-counter medications like paracetamol to reduce fever. Consult a doctor if it persists for more than 3 days.').
first_aid_advice(headache, 'Rest in a quiet, dark room. Stay hydrated and take a mild pain reliever like paracetamol if necessary.').
first_aid_advice(allergic_reaction, 'Identify and avoid the allergen. If symptoms include difficulty breathing, seek emergency medical care immediately.').
first_aid_advice(diarrhea, 'Stay hydrated with oral rehydration solutions. Avoid solid foods until symptoms improve. See a doctor if dehydration occurs.').

% Rules for Emergency Situations
emergency(Symptom, 'This requires immediate medical attention. Call emergency services.') :-
    member(Symptom, [severe_bleeding, unconscious, difficulty_breathing, chest_pain, seizure]).

% Rules for First Aid Recommendations
first_aid(Symptom, Advice) :-
    advice(Symptom, Advice).

% Rules for When to See a Doctor
consult_doctor(Symptom, 'Consult a doctor if the symptoms persist or worsen.') :-
    member(Symptom, [fever, headache, diarrhea, minor_cuts]).

% Example Queries
% Query: Get first aid advice for a specific situation
get_first_aid(Symptom, Advice) :-
    first_aid(Symptom, Advice).

% Query: Determine if a situation is an emergency
is_emergency(Symptom, Response) :-
    emergency(Symptom, Response).

% Query: Check if a doctor consultation is recommended
should_consult_doctor(Symptom, Response) :-
    consult_doctor(Symptom,Response).