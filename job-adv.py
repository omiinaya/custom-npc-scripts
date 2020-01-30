if sm.getChr().getLevel() < 10:
    sm.sendSayOkay("You need to be level 10 to job advance.")
if sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 0:
    explorer = sm.sendSayOkay("What would you like to become?: \r\n#L0#Magician \r\n#L1#Thief. \r\n#L2#Warrior. \r\n#L3#Archer. \r\n#L4#Pirate.")
    if explorer == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a magician?")
        if response:
            sm.jobAdvance(200)
            sm.dispose()
    if explorer == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become a thief?")
        if response:
            sm.jobAdvance(400)
            sm.dispose()
    if explorer == 2:
        response = sm.sendAskYesNo("Are you sure you'd like to become a warrior?")
        if response:
            sm.jobAdvance(100)
            sm.dispose()
    if explorer == 3:
        response = sm.sendAskYesNo("Are you sure you'd like to become an archer?")
        if response:
            sm.jobAdvance(300)
            sm.dispose()
    if explorer == 4:
        response = sm.sendAskYesNo("Are you sure you'd like to become a pirate?")
        if response:
            sm.jobAdvance(500)
            sm.dispose()
#second jobs
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 200:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 200:
    magician = sm.sendSayOkay("What would you like to become?: \r\n#L0#Fire/Poison Wizard \r\n#L1#Ice/Lightning Wizard. \r\n#L2#Cleric")
    if magician == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Fire/Poison Wizard?")
        if response:
            sm.jobAdvance(210)
            sm.dispose()
    if magician == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Ice/Lightning Wizard?")
        if response:
            sm.jobAdvance(220)
            sm.dispose()
    if magician == 2:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Cleric?")
        if response:
            sm.jobAdvance(230)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 400:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 400:
    thief = sm.sendSayOkay("What would you like to become?: \r\n#L0#Bandit \r\n#L1#Assassin.")
    if thief == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Bandit?")
        if response:
            sm.jobAdvance(420)
            sm.dispose()
    if thief == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Assassin?")
        if response:
            sm.jobAdvance(410)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 100:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 100:
    warrior = sm.sendSayOkay("What would you like to become?: \r\n#L0#Page \r\n#L1#Fighter. \r\n#L2#Spearman.")
    if warrior == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Page?")
        if response:
            sm.jobAdvance(120)
            sm.dispose()
    if warrior == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Fighter?")
        if response:
            sm.jobAdvance(110)
            sm.dispose()
    if warrior == 2:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Spearman?")
        if response:
            sm.jobAdvance(130)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 300:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 300:
    archer = sm.sendSayOkay("What would you like to become?: \r\n#L0#Hunter \r\n#L1#Crossbowman.")
    if archer == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Hunter?")
        if response:
            sm.jobAdvance(310)
            sm.dispose()
    if archer == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Crossbowman?")
        if response:
            sm.jobAdvance(320)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 500:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 500:
    pirate = sm.sendSayOkay("What would you like to become?: \r\n#L0#Brawler \r\n#L1#Gunslinger.")
    if pirate == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Brawler?")
        if response:
            sm.jobAdvance(510)
            sm.dispose()
    if pirate == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Gunslinger?")
        if response:
            sm.jobAdvance(520)
            sm.dispose()
#third jobs
if 70 > sm.getChr().getLevel() >= 30 and (sm.getChr().getJob() == 210 or sm.getChr().getJob() == 220 or sm.getChr().getJob() == 230):
    sm.sendSayOkay("Come back when you're Lv.70")
if sm.getChr().getLevel() >= 70 and sm.getChr().getJob() == 210:
    response = sm.sendAskYesNo("Are you ready to become a Fire/Poison Mage?")
    if response:
        sm.jobAdvance(211)
        sm.dispose()
if sm.getChr().getLevel() >= 70 and sm.getChr().getJob() == 220:
    response = sm.sendAskYesNo("Are you ready to become a Ice/Lightning Mage?")
    if response:
        sm.jobAdvance(221)
        sm.dispose()
if sm.getChr().getLevel() >= 70 and sm.getChr().getJob() == 230:
    response = sm.sendAskYesNo("Are you ready to become a Priest?")
    if response:
        sm.jobAdvance(231)
        sm.dispose()