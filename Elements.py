#burnt does damage over time, more damage than poison but for a shorter time
#frozen reduces damage delt
#stuck increases damage taken
#Air extends these effects
#Poison does damage, less than fire but more over time

def CheckElementalDamage(checked_list):
	for people in range(len(checked_list)):
		if checked_list[people].BRT > 0:
			checked_list[people].BRT -= 1