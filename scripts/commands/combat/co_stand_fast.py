import sys

def setup(core, actor, target, command):
	if actor.getSkillMod('expertise_cooldown_line_co_stand_fast'):
		command.setCooldown(command.getCooldown() - actor.getSkillMod('expertise_cooldown_line_co_stand_fast').getBase())
	return
	
def run(core, actor, target, commandString):
	return