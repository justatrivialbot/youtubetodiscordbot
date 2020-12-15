<<<<<<< HEAD
import pickle
# from datetime import timezone
# import datetime

# dt = datetime.datetime.now()
# utc_time = dt.replace(tzinfo=timezone.utc)
ts = 1606089600

channel_ids = [
    ["UClu2e7S8atp6tG2galK9hgg", "Bdoubleo100", ts, "main"],
    ["UC9lJXqw4QZw-HWaZH6sN-xw", "cubfan135", ts, "main"],
    ["UC4O9HKe9Jt5yAhKuNv3LXpQ", "docm77", ts, "main"],
    ["UCuQYHhF6on6EXXO-_i_ClHQ", "falsesymmetry", ts, "main"],
    ["UCR9Gcq0CMm6YgTzsDxAxjOQ", "Grian", ts, "main"],
    ["UChi5MyXJLQuPni3dM19Ar3g", "hypnotizd", ts, "main"],
    ["UCrEtZMErQXaSYy_JDGoU5Qw", "iJevin", ts, "main"],
    ["UCuMJPFqazQI4SofSFEd-5zA", "impulseSV", ts, "main"],
    ["UCZ9x-z3iOnIbJxVpm1rsu2A", "Iskall85", ts, "main"],
    ["UCtWObtiLCNI_BTBHwEOZNqg", "Joe Hills", ts, "main"],
    ["UCcJgOennb0II4a_qi9OMkRA", "Keralis", ts, "main"],
    ["UChFur_NwVSbUozOcF_F2kMg", "Mumbo Jumbo", ts, "main"],
    ["UCDpdtiUfcdUCzokpRWORRqA", "ReNDoG", ts, "main"],
    ["UCodkNmk9oWRTIYZdr_HuSlg", "GoodTimesWithScar", ts, "main"],
    ["UC24lkOxZYna9nlXYBcJ9B8Q", "stressmonster101", ts, "main"],
    ["UC4YUKOBld2PoOLzk0YZ80lw", "Tango Tek", ts, "main"],
    ["UCRatys97ggrXVtQQBGRALkg", "Tinfoil Chef", ts, "main"],
    ["UCu17Sme-KE87ca9OTzP0p7g", "Vintage Beef", ts, "main"],
    ["UCKEJZ-dqIA03evnzEy1_owg", "Welsknight", ts, "main"],
    ["UC_MkjhQr_D_lGlO3uu-GxyA", "xBCrafted", ts, "main"],
    ["UCU9pX8hKcrx06XfOB-VQLdw", "Xisumavoid", ts, "main"],
    ["UCPK5G4jeoVEbUp5crKJl6CQ", "Zedaph", ts, "main"],
    ["UCjI5qxhtyv3srhWr60HemRw", "ZombieCleo", ts, "main"],
    ["UCQgX4qy49zw9-DoHj4aZ6_g", "Cubfan Games", ts, "alt"],
    ["UCpArlUtSgiPGBklMDzwrr2g", "FalseLive", ts, "alt"],
    ["UCDiznUV6dtdB9PQj__XVhnA", "Two Much Grian", ts, "alt"],
    ["UCVX2I3KruzTnDTsKXGwbGkw", "Imp and Skizz", ts, "alt"],
    ["UCbav3eAAnFxnXAkMUjoJ1og", "impulseSV2", ts, "alt"],
    ["UC11OPzwn5Wt0-LN3rARunmg", "Mumbo (Filming)", ts, "alt"],
    ["UCB3SAOiqd2UhXl3g5CpHKXA", "Natalie Arnold (stressmonster101)", ts,
     "alt"],
    ["UCOd7af-2Hzix4ew5TPt-v0Q", "Stressmonster Extra", ts, "alt"],
    ["UCxCEaQ_uUv_okCK_AYg9NaA", "Tango Tek2", ts, "alt"],
    ["UCxHZnaMb3DAwx54S6t_KoUw", "Tinfoil Chef Vlogs", ts, "alt"],
    ["UCuWTX_KZLHXk7TMkfwTeCTQ", "xBToo", ts, "alt"],
    ["UCL5W9kuKIQtXEVAxSadB2BQ", "xisumatwo", ts, "alt"],
    ["UCm6yD26HlafzqNlYaK7uEaA", "xisumasays", ts, "alt"],
    ["UCw3e5HIQiYc7p1bEpOtEkog", "xisumamusic", ts, "alt"],
    ["UCP22ETMgm7zp7b1kpJe4CQA", "ZedaphPlays2", ts, "alt"]
]
pickle.dump(channel_ids, open("channeldata.txt", "wb"))
=======
import pickle
# from datetime import timezone
# import datetime

# dt = datetime.datetime.now()
# utc_time = dt.replace(tzinfo=timezone.utc)
ts = 1606089600

channel_ids = [
    ["UClu2e7S8atp6tG2galK9hgg", "Bdoubleo100", ts, "main"],
    ["UC9lJXqw4QZw-HWaZH6sN-xw", "cubfan135", ts, "main"],
    ["UC4O9HKe9Jt5yAhKuNv3LXpQ", "docm77", ts, "main"],
    ["UCuQYHhF6on6EXXO-_i_ClHQ", "falsesymmetry", ts, "main"],
    ["UCR9Gcq0CMm6YgTzsDxAxjOQ", "Grian", ts, "main"],
    ["UChi5MyXJLQuPni3dM19Ar3g", "hypnotizd", ts, "main"],
    ["UCrEtZMErQXaSYy_JDGoU5Qw", "iJevin", ts, "main"],
    ["UCuMJPFqazQI4SofSFEd-5zA", "impulseSV", ts, "main"],
    ["UCZ9x-z3iOnIbJxVpm1rsu2A", "Iskall85", ts, "main"],
    ["UCtWObtiLCNI_BTBHwEOZNqg", "Joe Hills", ts, "main"],
    ["UCcJgOennb0II4a_qi9OMkRA", "Keralis", ts, "main"],
    ["UChFur_NwVSbUozOcF_F2kMg", "Mumbo Jumbo", ts, "main"],
    ["UCDpdtiUfcdUCzokpRWORRqA", "ReNDoG", ts, "main"],
    ["UCodkNmk9oWRTIYZdr_HuSlg", "GoodTimesWithScar", ts, "main"],
    ["UC24lkOxZYna9nlXYBcJ9B8Q", "stressmonster101", ts, "main"],
    ["UC4YUKOBld2PoOLzk0YZ80lw", "Tango Tek", ts, "main"],
    ["UCRatys97ggrXVtQQBGRALkg", "Tinfoil Chef", ts, "main"],
    ["UCu17Sme-KE87ca9OTzP0p7g", "Vintage Beef", ts, "main"],
    ["UCKEJZ-dqIA03evnzEy1_owg", "Welsknight", ts, "main"],
    ["UC_MkjhQr_D_lGlO3uu-GxyA", "xBCrafted", ts, "main"],
    ["UCU9pX8hKcrx06XfOB-VQLdw", "Xisumavoid", ts, "main"],
    ["UCPK5G4jeoVEbUp5crKJl6CQ", "Zedaph", ts, "main"],
    ["UCjI5qxhtyv3srhWr60HemRw", "ZombieCleo", ts, "main"],
    ["UCQgX4qy49zw9-DoHj4aZ6_g", "Cubfan Games", ts, "alt"],
    ["UCpArlUtSgiPGBklMDzwrr2g", "FalseLive", ts, "alt"],
    ["UCDiznUV6dtdB9PQj__XVhnA", "Two Much Grian", ts, "alt"],
    ["UCVX2I3KruzTnDTsKXGwbGkw", "Imp and Skizz", ts, "alt"],
    ["UCbav3eAAnFxnXAkMUjoJ1og", "impulseSV2", ts, "alt"],
    ["UC11OPzwn5Wt0-LN3rARunmg", "Mumbo (Filming)", ts, "alt"],
    ["UCB3SAOiqd2UhXl3g5CpHKXA", "Natalie Arnold (stressmonster101)", ts,
     "alt"],
    ["UCOd7af-2Hzix4ew5TPt-v0Q", "Stressmonster Extra", ts, "alt"],
    ["UCxCEaQ_uUv_okCK_AYg9NaA", "Tango Tek2", ts, "alt"],
    ["UCxHZnaMb3DAwx54S6t_KoUw", "Tinfoil Chef Vlogs", ts, "alt"],
    ["UCuWTX_KZLHXk7TMkfwTeCTQ", "xBToo", ts, "alt"],
    ["UCL5W9kuKIQtXEVAxSadB2BQ", "xisumatwo", ts, "alt"],
    ["UCm6yD26HlafzqNlYaK7uEaA", "xisumasays", ts, "alt"],
    ["UCw3e5HIQiYc7p1bEpOtEkog", "xisumamusic", ts, "alt"],
    ["UCP22ETMgm7zp7b1kpJe4CQA", "ZedaphPlays2", ts, "alt"]
]
pickle.dump(channel_ids, open("channeldata.txt", "wb"))
>>>>>>> 4f4495ec3a8542beb18ca55c279652518c1e7922
