import edrpg

tasha = edrpg.Character("Tasha", "34", "160", "65")

tasha.nav.update(50, tasha.skillcap)

print(tasha.nav.bonus)

