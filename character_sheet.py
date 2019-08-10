import edrpg

tasha = edrpg.Character("Tasha Lomendese", "34", "150cm", "65kg")

#sweet = edrpg.Ship("Adder", "Sweet", tasha)

huge = edrpg.Ship("Anaconda", "Huge", tasha)

print(huge.pp_slot.content.name)