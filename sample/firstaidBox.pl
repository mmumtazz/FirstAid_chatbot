% Items in a first aid kit
item_in_first_aid_kit(adhesive_bandages).
item_in_first_aid_kit(sterile_gauze_pads).
item_in_first_aid_kit(adhesive_tape).
item_in_first_aid_kit(antiseptic_wipes).
item_in_first_aid_kit(antibiotic_ointment).
item_in_first_aid_kit(pain_relievers).
item_in_first_aid_kit(tweezers).
item_in_first_aid_kit(scissors).
item_in_first_aid_kit(thermometer).
item_in_first_aid_kit(disposable_gloves).
item_in_first_aid_kit(cpr_face_shield).
item_in_first_aid_kit(emergency_blanket).
item_in_first_aid_kit(small_flashlight).

% Items in a travel first aid kit
item_in_travel_first_aid_kit(adhesive_bandages).
item_in_travel_first_aid_kit(antiseptic_wipes).
item_in_travel_first_aid_kit(pain_relievers).
item_in_travel_first_aid_kit(motion_sickness_tablets).
item_in_travel_first_aid_kit(bug_spray).
item_in_travel_first_aid_kit(sunscreen).
item_in_travel_first_aid_kit(aloe_vera_gel).
item_in_travel_first_aid_kit(foldable_emergency_blanket).
item_in_travel_first_aid_kit(tweezers).
item_in_travel_first_aid_kit(scissors).
item_in_travel_first_aid_kit(personal_medications).

% Assembling a first aid kit
assemble_first_aid_kit(Container) :-
    write('1. Start with a sturdy, waterproof container.'), nl,
    write('2. Include basic supplies like bandages, gauze, antiseptics, and pain relievers.'), nl,
    write('3. Add tools such as scissors, tweezers, and a thermometer.'), nl,
    write('4. Include any medications specific to your family or pets.'), nl,
    write('5. Don’t forget an emergency manual for quick reference.'), nl,
    write('6. Check expiration dates periodically and replace items as needed.').

% Maintaining a first aid kit
maintain_first_aid_kit :-
    write('To maintain a first aid kit:'), nl,
    write('- Check the kit every 6 months for expired medications.'), nl,
    write('- Replace used or damaged items immediately.'), nl,
    write('- Keep the kit in a cool, dry place that is easy to access.'), nl,
    write('- Ensure everyone in the household knows where it is and how to use it.').

% When to check a first aid kit
check_first_aid_kit :-
    write('It’s recommended to check your first aid kit every 6 months:'), nl,
    write('- Look for expired medications.'), nl,
    write('- Replenish used items.'), nl,
    write('- Ensure all tools are in good condition.'), nl,
    write('Regular maintenance ensures your kit is ready for emergencies.').

% Facts about items in first aid kits
item_in_first_aid_kit(adhesive_bandages).
item_in_first_aid_kit(sterile_gauze_pads).
item_in_first_aid_kit(adhesive_tape).
item_in_first_aid_kit(antiseptic_wipes).
item_in_first_aid_kit(antibiotic_ointment).
item_in_first_aid_kit(pain_relievers).
item_in_first_aid_kit(tweezers).
item_in_first_aid_kit(scissors).
item_in_first_aid_kit(thermometer).
item_in_first_aid_kit(disposable_gloves).
item_in_first_aid_kit(cpr_face_shield).
item_in_first_aid_kit(emergency_blanket).
item_in_first_aid_kit(small_flashlight).

% Facts about items in travel first aid kits
item_in_travel_first_aid_kit(adhesive_bandages).
item_in_travel_first_aid_kit(antiseptic_wipes).
item_in_travel_first_aid_kit(pain_relievers).
item_in_travel_first_aid_kit(motion_sickness_tablets).
item_in_travel_first_aid_kit(bug_spray).
item_in_travel_first_aid_kit(sunscreen).
item_in_travel_first_aid_kit(aloe_vera_gel).
item_in_travel_first_aid_kit(foldable_emergency_blanket).
item_in_travel_first_aid_kit(tweezers).
item_in_travel_first_aid_kit(scissors).
item_in_travel_first_aid_kit(personal_medications).

% Queries for listing items in a first aid kit
what_should_be_in_first_aid_kit :-
    item_in_first_aid_kit(Item),
    write(Item),
    nl,
    fail.
what_should_be_in_first_aid_kit.

what_should_be_in_travel_first_aid_kit :-
    item_in_travel_first_aid_kit(Item),
    write(Item),
    nl,
    fail.
what_should_be_in_travel_first_aid_kit.
