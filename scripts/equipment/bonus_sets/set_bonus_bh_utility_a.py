import sys
from services.equipment import BonusSetTemplate
from java.util import Vector

def addBonusSet(core):
	bonusSet = BonusSetTemplate("set_bonus_bh_utility_a")
	
	bonusSet.addRequiredItem("item_band_set_bh_utility_a_01_01")
	bonusSet.addRequiredItem("item_ring_set_bh_utility_a_01_01")
	bonusSet.addRequiredItem("item_necklace_set_bh_utility_a_01_01")
	bonusSet.addRequiredItem("item_bracelet_r_set_bh_utility_a_01_01")
	bonusSet.addRequiredItem("item_bracelet_l_set_bh_utility_a_01_01")
	
	core.equipmentService.addBonusSetTemplate(bonusSet)
	
def handleChange(core, creature, set):
	wornItems = set.getWornTemplateCount(creature)
	
	if wornItems == 3:
		core.buffService.addBuffToCreature(creature, "set_bonus_bh_utility_a_1", creature)
	elif wornItems == 4:
		core.buffService.addBuffToCreature(creature, "set_bonus_bh_utility_a_2", creature)
	elif wornItems == 5:
		core.buffService.addBuffToCreature(creature, "set_bonus_bh_utility_a_3", creature)
	else:
		core.buffService.removeBuffFromCreatureByName(creature, "set_bonus_bh_utility_a_1")
		core.buffService.removeBuffFromCreatureByName(creature, "set_bonus_bh_utility_a_2")
		core.buffService.removeBuffFromCreatureByName(creature, "set_bonus_bh_utility_a_3")