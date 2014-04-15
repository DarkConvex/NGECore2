import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'harvesterDeed')
	object.setConstructorTemplate('object/installation/mining_ore/construction/shared_construction_mining_ore_harvester_style_2.iff')
	object.setStructureTemplate('object/installation/mining_liquid/shared_mining_liquid_harvester_style_2.iff')
	object.setLotRequirement(1)
	object.setBMR(60)
	return