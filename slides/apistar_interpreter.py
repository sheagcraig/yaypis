>>> import requests
>>> import json
>>> response = requests.get('http://localhost:8080/games/')
>>> print(json.dumps(response.json(), indent=4)
... )
[
    {
        "id": 1,
        "title": "10-Yard Fight",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 2,
        "title": "1942",
        "release_date": "November 1986",
        "publisher": "Capcom"
    },
    {
        "id": 3,
        "title": "1943: The Battle of Midway",
        "release_date": "October 1988",
        "publisher": "Capcom"
    },
    {
        "id": 4,
        "title": "The 3-D Battles of WorldRunner",
        "release_date": "September 1987",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 5,
        "title": "720\u00b0",
        "release_date": "November 1989",
        "publisher": "Mindscape"
    },
    {
        "id": 6,
        "title": "8 Eyes",
        "release_date": "January 1990",
        "publisher": "Taxan"
    },
    {
        "id": 7,
        "title": "Abadox",
        "release_date": "March 1990",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 8,
        "title": "The Addams Family",
        "release_date": "January 1992",
        "publisher": "Ocean Software"
    },
    {
        "id": 9,
        "title": "The Addams Family: Pugsley's Scavenger Hunt",
        "release_date": "August 1993",
        "publisher": "Ocean Software"
    },
    {
        "id": 10,
        "title": "Advanced Dungeons & Dragons: DragonStrike",
        "release_date": "July 1992",
        "publisher": "FCI"
    },
    {
        "id": 11,
        "title": "Advanced Dungeons & Dragons: Heroes of the Lance",
        "release_date": "January 1991",
        "publisher": "FCI"
    },
    {
        "id": 12,
        "title": "Advanced Dungeons & Dragons: Hillsfar",
        "release_date": "February 1993",
        "publisher": "FCI"
    },
    {
        "id": 13,
        "title": "Advanced Dungeons & Dragons: Pool of Radiance",
        "release_date": "April 1992",
        "publisher": "FCI"
    },
    {
        "id": 14,
        "title": "Adventure Island",
        "release_date": "September 1988",
        "publisher": "Hudson Soft"
    },
    {
        "id": 15,
        "title": "Adventure Island II",
        "release_date": "February 1991",
        "publisher": null
    },
    {
        "id": 16,
        "title": "Adventure Island 3",
        "release_date": "September 1992",
        "publisher": "Hudson Soft"
    },
    {
        "id": 17,
        "title": "Adventures in the Magic Kingdom",
        "release_date": "June 1990",
        "publisher": "Capcom"
    },
    {
        "id": 18,
        "title": "The Adventures of Bayou Billy",
        "release_date": "June 1989",
        "publisher": "Konami"
    },
    {
        "id": 19,
        "title": "Adventures of Dino Riki",
        "release_date": "September 1989",
        "publisher": "Hudson Soft"
    },
    {
        "id": 20,
        "title": "The Adventures of Gilligan's Island",
        "release_date": "July 1990",
        "publisher": "Bandai"
    },
    {
        "id": 21,
        "title": "Adventures of Lolo",
        "release_date": "April 1989",
        "publisher": "HAL America"
    },
    {
        "id": 22,
        "title": "Adventures of Lolo 2",
        "release_date": "March 1990",
        "publisher": "HAL America"
    },
    {
        "id": 23,
        "title": "Adventures of Lolo 3",
        "release_date": "September 1991",
        "publisher": "HAL America"
    },
    {
        "id": 24,
        "title": "The Adventures of Rad Gravity",
        "release_date": "December 1990",
        "publisher": null
    },
    {
        "id": 25,
        "title": "The Adventures of Rocky and Bullwinkle and Friends",
        "release_date": "December 1992",
        "publisher": "THQ"
    },
    {
        "id": 26,
        "title": "The Adventures of Tom Sawyer",
        "release_date": "August 1989",
        "publisher": "SETA"
    },
    {
        "id": 27,
        "title": "Air Fortress",
        "release_date": "September 1989",
        "publisher": "HAL America"
    },
    {
        "id": 28,
        "title": "Airwolf",
        "release_date": "June 1989",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 29,
        "title": null,
        "release_date": null,
        "publisher": "Data East"
    },
    {
        "id": 30,
        "title": "Alfred Chicken",
        "release_date": "February 1994",
        "publisher": "Mindscape"
    },
    {
        "id": 31,
        "title": "Alien3",
        "release_date": "March 1993",
        "publisher": "LJN"
    },
    {
        "id": 32,
        "title": "All-Pro Basketball",
        "release_date": "December 1989",
        "publisher": "Vic Tokai"
    },
    {
        "id": 33,
        "title": "Alpha Mission",
        "release_date": "October 1987",
        "publisher": "SNK"
    },
    {
        "id": 34,
        "title": "Amagon",
        "release_date": "April 1989",
        "publisher": "American Sammy"
    },
    {
        "id": 35,
        "title": "American Gladiators",
        "release_date": "October 1991",
        "publisher": "GameTek"
    },
    {
        "id": 36,
        "title": "Anticipation",
        "release_date": "November 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 37,
        "title": "Arch Rivals",
        "release_date": "November 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 38,
        "title": "Archon",
        "release_date": "December 1989",
        "publisher": "Activision"
    },
    {
        "id": 39,
        "title": "Arkanoid",
        "release_date": "August 1987",
        "publisher": "Taito"
    },
    {
        "id": 40,
        "title": "Arkista's Ring",
        "release_date": "June 1990",
        "publisher": "American Sammy"
    },
    {
        "id": 41,
        "title": "Asterix",
        "release_date": "1993",
        "publisher": null
    },
    {
        "id": 42,
        "title": "Astyanax",
        "release_date": "March 1990",
        "publisher": "Jaleco"
    },
    {
        "id": 43,
        "title": "Athena",
        "release_date": "August 1987",
        "publisher": "SNK"
    },
    {
        "id": 44,
        "title": "Athletic World",
        "release_date": "June 18, 1987",
        "publisher": null
    },
    {
        "id": 45,
        "title": "Attack of the Killer Tomatoes",
        "release_date": "January 1992",
        "publisher": "THQ"
    },
    {
        "id": 46,
        "title": "Aussie Rules Footy",
        "release_date": "1991",
        "publisher": null
    },
    {
        "id": 47,
        "title": "Back to the Future",
        "release_date": "September 1989",
        "publisher": "LJN"
    },
    {
        "id": 48,
        "title": "Back to the Future Part II & III",
        "release_date": "September 1990",
        "publisher": "LJN"
    },
    {
        "id": 49,
        "title": null,
        "release_date": null,
        "publisher": null
    },
    {
        "id": 50,
        "title": "Bad News Baseball",
        "release_date": "June 1990",
        "publisher": "Tecmo"
    },
    {
        "id": 51,
        "title": "Bad Street Brawler",
        "release_date": "September 1989",
        "publisher": "Mattel"
    },
    {
        "id": 52,
        "title": "Balloon Fight",
        "release_date": "August 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 53,
        "title": "Banana Prince",
        "release_date": "February 1992",
        "publisher": null
    },
    {
        "id": 54,
        "title": "Bandai Golf: Challenge Pebble Beach",
        "release_date": "February 1989",
        "publisher": "Bandai"
    },
    {
        "id": 55,
        "title": "Bandit Kings of Ancient China",
        "release_date": "December 1990",
        "publisher": "Koei"
    },
    {
        "id": 56,
        "title": "Barbie",
        "release_date": "November 1991",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 57,
        "title": "The Bard's Tale",
        "release_date": "November 1991",
        "publisher": "FCI"
    },
    {
        "id": 58,
        "title": "Barker Bill's Trick Shooting",
        "release_date": "August 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 59,
        "title": "Base Wars",
        "release_date": "June 1991",
        "publisher": "Ultra Games"
    },
    {
        "id": 60,
        "title": "Baseball",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 61,
        "title": "Baseball Simulator 1.000",
        "release_date": "March 1990",
        "publisher": "Culture Brain"
    },
    {
        "id": 62,
        "title": "Baseball Stars",
        "release_date": "July 1989",
        "publisher": "SNK"
    },
    {
        "id": 63,
        "title": "Baseball Stars 2",
        "release_date": "July 1992",
        "publisher": "Romstar"
    },
    {
        "id": 64,
        "title": "Bases Loaded",
        "release_date": "July 1988",
        "publisher": "Jaleco"
    },
    {
        "id": 65,
        "title": "Bases Loaded II: Second Season",
        "release_date": "January 1990",
        "publisher": "Jaleco"
    },
    {
        "id": 66,
        "title": "Bases Loaded 3",
        "release_date": "September 1991",
        "publisher": "Jaleco"
    },
    {
        "id": 67,
        "title": "Bases Loaded 4",
        "release_date": "April 1993",
        "publisher": "Jaleco"
    },
    {
        "id": 68,
        "title": "Batman",
        "release_date": "February 1990",
        "publisher": "Sunsoft"
    },
    {
        "id": 69,
        "title": "Batman Returns",
        "release_date": "January 1993",
        "publisher": "Konami"
    },
    {
        "id": 70,
        "title": "Batman: Return of the Joker",
        "release_date": "December 1991",
        "publisher": "Sunsoft"
    },
    {
        "id": 71,
        "title": "Battle Chess",
        "release_date": "July 1990",
        "publisher": "Data East"
    },
    {
        "id": 72,
        "title": "The Battle of Olympus",
        "release_date": "December 1989",
        "publisher": null
    },
    {
        "id": 73,
        "title": "Battle Tank",
        "release_date": "September 1990",
        "publisher": "Absolute Entertainment"
    },
    {
        "id": 74,
        "title": "Battleship",
        "release_date": "September 1993",
        "publisher": "Mindscape"
    },
    {
        "id": 75,
        "title": "Battletoads",
        "release_date": "June 1991",
        "publisher": "Tradewest"
    },
    {
        "id": 76,
        "title": "Battletoads & Double Dragon",
        "release_date": "June 1993",
        "publisher": "Tradewest"
    },
    {
        "id": 77,
        "title": "Beetlejuice",
        "release_date": "May 1991",
        "publisher": "LJN"
    },
    {
        "id": 78,
        "title": "Best of the Best: Championship Karate",
        "release_date": "December 1992",
        "publisher": null
    },
    {
        "id": 79,
        "title": "Bigfoot",
        "release_date": "August 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 80,
        "title": "Bill & Ted's Excellent Video Game Adventure",
        "release_date": "April 1991",
        "publisher": "LJN"
    },
    {
        "id": 81,
        "title": "Bill Elliott's NASCAR Challenge",
        "release_date": "December 1991",
        "publisher": "Konami"
    },
    {
        "id": 82,
        "title": "Bionic Commando",
        "release_date": "December 1988",
        "publisher": "Capcom"
    },
    {
        "id": 83,
        "title": "The Black Bass",
        "release_date": "September 1989",
        "publisher": "Hot B"
    },
    {
        "id": 84,
        "title": "Blades of Steel",
        "release_date": "December 1988",
        "publisher": null
    },
    {
        "id": 85,
        "title": "Blaster Master",
        "release_date": "November 1988",
        "publisher": "Sunsoft"
    },
    {
        "id": 86,
        "title": "The Blue Marlin",
        "release_date": "July 1992",
        "publisher": "Hot-B"
    },
    {
        "id": 87,
        "title": "The Blues Brothers",
        "release_date": "September 1992",
        "publisher": "Titus Software"
    },
    {
        "id": 88,
        "title": "Bo Jackson Baseball",
        "release_date": "October 1991",
        "publisher": "Data East"
    },
    {
        "id": 89,
        "title": "Bomberman",
        "release_date": "January 1989",
        "publisher": "Hudson Soft"
    },
    {
        "id": 90,
        "title": "Bomberman II",
        "release_date": "March 1992",
        "publisher": "Hudson Soft"
    },
    {
        "id": 91,
        "title": "Bonk's Adventure",
        "release_date": "January 1994",
        "publisher": "Hudson Soft"
    },
    {
        "id": 92,
        "title": "Boulder Dash",
        "release_date": "June 1990",
        "publisher": null
    },
    {
        "id": 93,
        "title": "A Boy and His Blob: Trouble on Blobolonia",
        "release_date": "January 1990",
        "publisher": "Absolute Entertainment"
    },
    {
        "id": 94,
        "title": "Bram Stoker's Dracula",
        "release_date": "September 1993",
        "publisher": "Sony Imagesoft"
    },
    {
        "id": 95,
        "title": "Break Time: The National Pool Tour",
        "release_date": "January 1993",
        "publisher": "FCI"
    },
    {
        "id": 96,
        "title": "BreakThru",
        "release_date": "November 1987",
        "publisher": "Data East"
    },
    {
        "id": 97,
        "title": "Bubble Bobble",
        "release_date": "November 1988",
        "publisher": null
    },
    {
        "id": 98,
        "title": "Bubble Bobble Part 2",
        "release_date": "August 1993",
        "publisher": "Taito"
    },
    {
        "id": 99,
        "title": "Bucky O'Hare",
        "release_date": "January 1992",
        "publisher": null
    },
    {
        "id": 100,
        "title": "The Bugs Bunny Birthday Blowout",
        "release_date": "September 1990",
        "publisher": "Kemco"
    },
    {
        "id": 101,
        "title": "The Bugs Bunny Crazy Castle",
        "release_date": "August 1989",
        "publisher": "Kemco"
    },
    {
        "id": 102,
        "title": "Bump 'n' Jump",
        "release_date": "December 1988",
        "publisher": "Vic Tokai"
    },
    {
        "id": 103,
        "title": "Burai Fighter",
        "release_date": "March 1990",
        "publisher": "Taxan"
    },
    {
        "id": 104,
        "title": "BurgerTime",
        "release_date": "May 1987",
        "publisher": "Data East"
    },
    {
        "id": 105,
        "title": "Cabal",
        "release_date": "June 1990",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 106,
        "title": "Caesars Palace",
        "release_date": "December 1992",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 107,
        "title": "California Games",
        "release_date": "June 1989",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 108,
        "title": "Capcom's Gold Medal Challenge '92",
        "release_date": "August 1992",
        "publisher": "Capcom"
    },
    {
        "id": 109,
        "title": "Captain America and The Avengers",
        "release_date": "December 1991",
        "publisher": "Data East"
    },
    {
        "id": 110,
        "title": "Captain Planet and the Planeteers",
        "release_date": "September 1991",
        "publisher": "Mindscape"
    },
    {
        "id": 111,
        "title": "Captain Skyhawk",
        "release_date": "June 1990",
        "publisher": null
    },
    {
        "id": 112,
        "title": "Casino Kid",
        "release_date": "October 1989",
        "publisher": "SOFEL"
    },
    {
        "id": 113,
        "title": "Casino Kid 2",
        "release_date": "April 1993",
        "publisher": "SOFEL"
    },
    {
        "id": 114,
        "title": "Castelian",
        "release_date": "June 1991",
        "publisher": null
    },
    {
        "id": 115,
        "title": "Castle of Dragon",
        "release_date": "June 1990",
        "publisher": "SETA"
    },
    {
        "id": 116,
        "title": "Castlequest",
        "release_date": "September 1989",
        "publisher": "ASCII"
    },
    {
        "id": 117,
        "title": "Castlevania",
        "release_date": "May 1987",
        "publisher": "Konami"
    },
    {
        "id": 118,
        "title": "Castlevania II: Simon's Quest",
        "release_date": "December 1988",
        "publisher": "Konami"
    },
    {
        "id": 119,
        "title": "Castlevania III: Dracula's Curse",
        "release_date": "September 1990",
        "publisher": null
    },
    {
        "id": 120,
        "title": "Caveman Games",
        "release_date": "October 1990",
        "publisher": "Data East"
    },
    {
        "id": 121,
        "title": "Championship Bowling",
        "release_date": "December 1989",
        "publisher": "Romstar"
    },
    {
        "id": 122,
        "title": "Championship Pool",
        "release_date": "October 1993",
        "publisher": "Mindscape"
    },
    {
        "id": 123,
        "title": "Championship Rally",
        "release_date": "1991",
        "publisher": null
    },
    {
        "id": 124,
        "title": "Chessmaster",
        "release_date": "January 1990",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 125,
        "title": "Chip 'n Dale: Rescue Rangers",
        "release_date": "June 1990",
        "publisher": "Capcom"
    },
    {
        "id": 126,
        "title": "Chip 'n Dale Rescue Rangers 2",
        "release_date": "January 1994",
        "publisher": "Capcom"
    },
    {
        "id": 127,
        "title": "Chubby Cherub",
        "release_date": "October 29, 1986",
        "publisher": "Bandai"
    },
    {
        "id": 128,
        "title": "Circus Caper",
        "release_date": "July 1990",
        "publisher": "Toho"
    },
    {
        "id": 129,
        "title": "City Connection",
        "release_date": "May 1988",
        "publisher": "Jaleco"
    },
    {
        "id": 130,
        "title": "Clash at Demonhead",
        "release_date": "January 1990",
        "publisher": "Vic Tokai"
    },
    {
        "id": 131,
        "title": "Classic Concentration",
        "release_date": "September 1990",
        "publisher": "GameTek"
    },
    {
        "id": 132,
        "title": "Cliffhanger",
        "release_date": "November 1993",
        "publisher": "Sony Imagesoft"
    },
    {
        "id": 133,
        "title": "Clu Clu Land",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 134,
        "title": "Cobra Command",
        "release_date": "November 1988",
        "publisher": "Data East"
    },
    {
        "id": 135,
        "title": "Cobra Triangle",
        "release_date": "July 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 136,
        "title": "Code Name: Viper",
        "release_date": "March 1990",
        "publisher": "Capcom"
    },
    {
        "id": 137,
        "title": "Color a Dinosaur",
        "release_date": "July 1993",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 138,
        "title": "Commando",
        "release_date": "November 1986",
        "publisher": "Capcom"
    },
    {
        "id": 139,
        "title": "Conan: The Mysteries of Time",
        "release_date": "February 1991",
        "publisher": "Mindscape"
    },
    {
        "id": 140,
        "title": "Conflict",
        "release_date": "March 1990",
        "publisher": "Vic Tokai"
    },
    {
        "id": 141,
        "title": "Conquest of the Crystal Palace",
        "release_date": "November 1990",
        "publisher": "Asmik"
    },
    {
        "id": 142,
        "title": "Contra",
        "release_date": "February 1988",
        "publisher": "Konami"
    },
    {
        "id": 143,
        "title": "Contra Force",
        "release_date": "September 1992",
        "publisher": "Konami"
    },
    {
        "id": 144,
        "title": "Cool World",
        "release_date": "June 1993",
        "publisher": "Ocean Software"
    },
    {
        "id": 145,
        "title": "Cowboy Kid",
        "release_date": "January 1992",
        "publisher": "Romstar"
    },
    {
        "id": 146,
        "title": "Crackout",
        "release_date": "1991",
        "publisher": "Palcom"
    },
    {
        "id": 147,
        "title": "Crash 'n the Boys: Street Challenge",
        "release_date": "October 1992",
        "publisher": "Techn\u014ds Japan"
    },
    {
        "id": 148,
        "title": "Crystalis",
        "release_date": "July 1990",
        "publisher": "SNK"
    },
    {
        "id": 149,
        "title": "Cyberball",
        "release_date": "January 1992",
        "publisher": "Jaleco"
    },
    {
        "id": 150,
        "title": "Cybernoid: The Fighting Machine",
        "release_date": "December 1989",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 151,
        "title": "Dance Aerobics",
        "release_date": "March 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 152,
        "title": "Danny Sullivan's Indy Heat",
        "release_date": "August 1992",
        "publisher": "Tradewest"
    },
    {
        "id": 153,
        "title": "Darkman",
        "release_date": "October 1991",
        "publisher": "Ocean Software"
    },
    {
        "id": 154,
        "title": "Dash Galaxy in the Alien Asylum",
        "release_date": "February 1990",
        "publisher": "Data East"
    },
    {
        "id": 155,
        "title": "Day Dreamin' Davey",
        "release_date": "June 1992",
        "publisher": "HAL America"
    },
    {
        "id": 156,
        "title": "Days of Thunder",
        "release_date": "October 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 157,
        "title": "Deadly Towers",
        "release_date": "September 1987",
        "publisher": "Br\u00f8derbund"
    },
    {
        "id": 158,
        "title": "Defender II",
        "release_date": "July 1988",
        "publisher": "HAL America"
    },
    {
        "id": 159,
        "title": "Defender of the Crown",
        "release_date": "July 1989",
        "publisher": "Ultra Games"
    },
    {
        "id": 160,
        "title": "Defenders of Dynatron City",
        "release_date": "July 1992",
        "publisher": "JVC"
    },
    {
        "id": 161,
        "title": "D\u00e9j\u00e0 Vu",
        "release_date": "December 1990",
        "publisher": "Seika"
    },
    {
        "id": 162,
        "title": "Demon Sword",
        "release_date": "January 1990",
        "publisher": "Taito"
    },
    {
        "id": 163,
        "title": "Desert Commander",
        "release_date": "June 1989",
        "publisher": "Seika"
    },
    {
        "id": 164,
        "title": "Destination Earthstar",
        "release_date": "February 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 165,
        "title": "Destiny of an Emperor",
        "release_date": "September 1990",
        "publisher": "Capcom"
    },
    {
        "id": 166,
        "title": "Devil World",
        "release_date": "July 15, 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 167,
        "title": "Dick Tracy",
        "release_date": "August 1990",
        "publisher": "Bandai"
    },
    {
        "id": 168,
        "title": "Die Hard",
        "release_date": "January 1992",
        "publisher": "Activision"
    },
    {
        "id": 169,
        "title": "Dig Dug II",
        "release_date": "December 1989",
        "publisher": "Bandai"
    },
    {
        "id": 170,
        "title": "Digger T. Rock: Legend of the Lost City",
        "release_date": "December 1990",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 171,
        "title": "Dirty Harry",
        "release_date": "December 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 172,
        "title": "Disney's Aladdin",
        "release_date": "February 23, 1995",
        "publisher": null
    },
    {
        "id": 173,
        "title": "Disney's Beauty and the Beast",
        "release_date": "1994",
        "publisher": null
    },
    {
        "id": 174,
        "title": "Disney's Darkwing Duck",
        "release_date": "June 1992",
        "publisher": "Capcom"
    },
    {
        "id": 175,
        "title": "Disney's The Jungle Book",
        "release_date": "August 1994",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 176,
        "title": "Disney's The Lion King",
        "release_date": "May 25, 1995",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 177,
        "title": "Disney's The Little Mermaid",
        "release_date": "July 1991",
        "publisher": "Capcom"
    },
    {
        "id": 178,
        "title": "Donkey Kong",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 179,
        "title": "Donkey Kong 3",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 180,
        "title": "Donkey Kong Classics",
        "release_date": "October 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 181,
        "title": "Donkey Kong Jr.",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 182,
        "title": "Donkey Kong Jr. Math",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 183,
        "title": "Double Dare",
        "release_date": "April 1990",
        "publisher": "GameTek"
    },
    {
        "id": 184,
        "title": "Double Dragon",
        "release_date": "June 1988",
        "publisher": "Tradewest"
    },
    {
        "id": 185,
        "title": "Double Dragon II: The Revenge",
        "release_date": "January 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 186,
        "title": "Double Dragon III: The Sacred Stones",
        "release_date": "February 1991",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 187,
        "title": "Double Dribble",
        "release_date": "September 1987",
        "publisher": "Konami"
    },
    {
        "id": 188,
        "title": "Dr. Chaos",
        "release_date": "November 1988",
        "publisher": "FCI"
    },
    {
        "id": 189,
        "title": "Dr. Jekyll and Mr. Hyde",
        "release_date": "April 1989",
        "publisher": "Bandai"
    },
    {
        "id": 190,
        "title": "Dr. Mario",
        "release_date": "October 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 191,
        "title": "Dragon Fighter",
        "release_date": "January 1992",
        "publisher": "SOFEL"
    },
    {
        "id": 192,
        "title": "Dragon Power",
        "release_date": "March 1988",
        "publisher": "Bandai"
    },
    {
        "id": 193,
        "title": "Dragon Spirit",
        "release_date": "June 1990",
        "publisher": "Bandai"
    },
    {
        "id": 194,
        "title": "Dragon Warrior",
        "release_date": "August 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 195,
        "title": "Dragon Warrior II",
        "release_date": "September 1990",
        "publisher": "Enix"
    },
    {
        "id": 196,
        "title": "Dragon Warrior III",
        "release_date": "March 1992",
        "publisher": "Enix"
    },
    {
        "id": 197,
        "title": "Dragon Warrior IV",
        "release_date": "October 1992",
        "publisher": "Enix"
    },
    {
        "id": 198,
        "title": "Dragon's Lair",
        "release_date": "December 1990",
        "publisher": null
    },
    {
        "id": 199,
        "title": "Dropzone",
        "release_date": "1992",
        "publisher": "Mindscape"
    },
    {
        "id": 200,
        "title": "Duck Hunt",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 201,
        "title": "DuckTales",
        "release_date": "September 1989",
        "publisher": "Capcom"
    },
    {
        "id": 202,
        "title": "DuckTales 2",
        "release_date": "June 1993",
        "publisher": "Capcom"
    },
    {
        "id": 203,
        "title": "Dungeon Magic: Sword of the Elements",
        "release_date": "July 1990",
        "publisher": "Taito"
    },
    {
        "id": 204,
        "title": "Dusty Diamond's All-Star Softball",
        "release_date": "July 1990",
        "publisher": "Br\u00f8derbund"
    },
    {
        "id": 205,
        "title": "Dynowarz: Destruction of Spondylus",
        "release_date": "April 1989",
        "publisher": "Bandai"
    },
    {
        "id": 206,
        "title": "Elevator Action",
        "release_date": "August 1987",
        "publisher": "Taito"
    },
    {
        "id": 207,
        "title": "Eliminator Boat Duel",
        "release_date": "November 1991",
        "publisher": "Electro Brain"
    },
    {
        "id": 208,
        "title": "Elite",
        "release_date": "1991",
        "publisher": "Imagineer"
    },
    {
        "id": 209,
        "title": "Excitebike",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 210,
        "title": "F-117A Stealth Fighter",
        "release_date": "December 1992",
        "publisher": "MicroProse"
    },
    {
        "id": 211,
        "title": "F-15 Strike Eagle",
        "release_date": "February 1992",
        "publisher": "MicroProse"
    },
    {
        "id": 212,
        "title": "Family Feud",
        "release_date": "May 1991",
        "publisher": "GameTek"
    },
    {
        "id": 213,
        "title": "Faria: A World of Mystery and Danger",
        "release_date": "June 1991",
        "publisher": "ASCII"
    },
    {
        "id": 214,
        "title": "Faxanadu",
        "release_date": "August 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 215,
        "title": "Felix the Cat",
        "release_date": "October 1992",
        "publisher": "Hudson Soft"
    },
    {
        "id": 216,
        "title": "Ferrari Grand Prix Challenge",
        "release_date": "June 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 217,
        "title": "Fester's Quest",
        "release_date": "September 1989",
        "publisher": "Sunsoft"
    },
    {
        "id": 218,
        "title": "Final Fantasy",
        "release_date": "May 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 219,
        "title": "Fire 'n Ice",
        "release_date": "March 1993",
        "publisher": "Tecmo"
    },
    {
        "id": 220,
        "title": "Fisher-Price: Firehouse Rescue",
        "release_date": "March 1992",
        "publisher": "GameTek"
    },
    {
        "id": 221,
        "title": "Fisher-Price: I Can Remember",
        "release_date": "March 1990",
        "publisher": "GameTek"
    },
    {
        "id": 222,
        "title": "Fisher-Price: Perfect Fit",
        "release_date": "March 1990",
        "publisher": "GameTek"
    },
    {
        "id": 223,
        "title": "Fist of the North Star",
        "release_date": "April 1989",
        "publisher": "Taxan"
    },
    {
        "id": 224,
        "title": "Flight of the Intruder",
        "release_date": "May 1991",
        "publisher": "Mindscape"
    },
    {
        "id": 225,
        "title": "The Flintstones: The Rescue of Dino & Hoppy",
        "release_date": "December 1991",
        "publisher": null
    },
    {
        "id": 226,
        "title": "The Flintstones: Surprise at Dinosaur Peak",
        "release_date": "August 1994",
        "publisher": "Taito"
    },
    {
        "id": 227,
        "title": "Flying Dragon: The Secret Scroll",
        "release_date": "August 1989",
        "publisher": "Culture Brain"
    },
    {
        "id": 228,
        "title": "Flying Warriors",
        "release_date": "February 1991",
        "publisher": "Culture Brain"
    },
    {
        "id": 229,
        "title": "Formula One: Built to Win",
        "release_date": "November 1990",
        "publisher": "SETA"
    },
    {
        "id": 230,
        "title": "Formula One Sensation",
        "release_date": "1993",
        "publisher": "Palcom"
    },
    {
        "id": 231,
        "title": "Frankenstein: The Monster Returns",
        "release_date": "July 1991",
        "publisher": "Bandai"
    },
    {
        "id": 232,
        "title": "Freedom Force",
        "release_date": "April 1988",
        "publisher": "Sunsoft"
    },
    {
        "id": 233,
        "title": "Friday the 13th",
        "release_date": "February 1989",
        "publisher": "LJN"
    },
    {
        "id": 234,
        "title": "Fun House",
        "release_date": "January 1991",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 235,
        "title": "G.I. Joe: A Real American Hero",
        "release_date": "January 1991",
        "publisher": "Taxan"
    },
    {
        "id": 236,
        "title": "G.I. Joe: The Atlantis Factor",
        "release_date": "March 1992",
        "publisher": "Capcom"
    },
    {
        "id": 237,
        "title": "Galaga",
        "release_date": "September 1988",
        "publisher": "Bandai"
    },
    {
        "id": 238,
        "title": "Galaxy 5000",
        "release_date": "February 1991",
        "publisher": "Activision"
    },
    {
        "id": 239,
        "title": "Gargoyle's Quest II",
        "release_date": "October 1992",
        "publisher": "Capcom"
    },
    {
        "id": 240,
        "title": "Gauntlet",
        "release_date": "July 1988",
        "publisher": "Tengen"
    },
    {
        "id": 241,
        "title": "Gauntlet II",
        "release_date": "September 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 242,
        "title": "Gemfire",
        "release_date": "March 1992",
        "publisher": "Koei"
    },
    {
        "id": 243,
        "title": "Genghis Khan",
        "release_date": "January 1990",
        "publisher": "Koei"
    },
    {
        "id": 244,
        "title": "George Foreman's KO Boxing",
        "release_date": "December 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 245,
        "title": "Ghostbusters",
        "release_date": "October 1988",
        "publisher": "Activision"
    },
    {
        "id": 246,
        "title": "Ghostbusters II",
        "release_date": "April 1990",
        "publisher": "Activision"
    },
    {
        "id": 247,
        "title": "Ghost Lion",
        "release_date": "October 1992",
        "publisher": "Kemco"
    },
    {
        "id": 248,
        "title": "Ghosts 'n Goblins",
        "release_date": "November 1986",
        "publisher": "Capcom"
    },
    {
        "id": 249,
        "title": "Ghoul School",
        "release_date": "March 1992",
        "publisher": "Electro Brain"
    },
    {
        "id": 250,
        "title": "Goal!",
        "release_date": "October 1989",
        "publisher": "Jaleco"
    },
    {
        "id": 251,
        "title": "Goal! Two",
        "release_date": "November 1992",
        "publisher": "Jaleco"
    },
    {
        "id": 252,
        "title": "Godzilla: Monster of Monsters",
        "release_date": "October 1989",
        "publisher": "Toho"
    },
    {
        "id": 253,
        "title": "Godzilla 2: War of the Monsters",
        "release_date": "February 1992",
        "publisher": "Toho"
    },
    {
        "id": 254,
        "title": "Golf",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 255,
        "title": "Golf Grand Slam",
        "release_date": "November 1991",
        "publisher": "Atlus"
    },
    {
        "id": 256,
        "title": "Golgo 13: Top Secret Episode",
        "release_date": "September 1988",
        "publisher": "Vic Tokai"
    },
    {
        "id": 257,
        "title": "The Goonies II",
        "release_date": "November 1987",
        "publisher": "Konami"
    },
    {
        "id": 258,
        "title": "Gotcha! The Sport!",
        "release_date": "November 1987",
        "publisher": "LJN"
    },
    {
        "id": 259,
        "title": "Gradius",
        "release_date": "December 1986",
        "publisher": "Konami"
    },
    {
        "id": 260,
        "title": "The Great Waldo Search",
        "release_date": "December 1992",
        "publisher": "THQ"
    },
    {
        "id": 261,
        "title": "Greg Norman's Golf Power",
        "release_date": "July 1992",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 262,
        "title": "Gremlins 2: The New Batch",
        "release_date": "October 1990",
        "publisher": "Sunsoft"
    },
    {
        "id": 263,
        "title": "The Guardian Legend",
        "release_date": "April 1989",
        "publisher": null
    },
    {
        "id": 264,
        "title": "Guerrilla War",
        "release_date": "June 1989",
        "publisher": "SNK"
    },
    {
        "id": 265,
        "title": "Gumshoe",
        "release_date": "August 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 266,
        "title": "Gun-Nac",
        "release_date": "September 1991",
        "publisher": "ASCII"
    },
    {
        "id": 267,
        "title": "Gun.Smoke",
        "release_date": "February 1988",
        "publisher": "Capcom"
    },
    {
        "id": 268,
        "title": "Gyromite",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 269,
        "title": "Gyruss",
        "release_date": "February 1989",
        "publisher": "Ultra Games"
    },
    {
        "id": 270,
        "title": "Hammerin' Harry",
        "release_date": "1992",
        "publisher": "Irem"
    },
    {
        "id": 271,
        "title": "Harlem Globetrotters",
        "release_date": "March 1991",
        "publisher": "GameTek"
    },
    {
        "id": 272,
        "title": "Hatris",
        "release_date": "April 1992",
        "publisher": "Bullet-Proof Software"
    },
    {
        "id": 273,
        "title": "Heavy Barrel",
        "release_date": "March 1990",
        "publisher": "Data East"
    },
    {
        "id": 274,
        "title": "Heavy Shreddin'",
        "release_date": "June 1990",
        "publisher": "Parker Brothers"
    },
    {
        "id": 275,
        "title": "High Speed",
        "release_date": "July 1991",
        "publisher": "Tradewest"
    },
    {
        "id": 276,
        "title": "Hogan's Alley",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 277,
        "title": "Hollywood Squares",
        "release_date": "September 1989",
        "publisher": "GameTek"
    },
    {
        "id": 278,
        "title": "Home Alone",
        "release_date": "October 1991",
        "publisher": "THQ"
    },
    {
        "id": 279,
        "title": "Home Alone 2: Lost in New York",
        "release_date": "October 1992",
        "publisher": "THQ"
    },
    {
        "id": 280,
        "title": "Hook",
        "release_date": "April 1992",
        "publisher": null
    },
    {
        "id": 281,
        "title": "Hoops",
        "release_date": "June 1989",
        "publisher": "Jaleco"
    },
    {
        "id": 282,
        "title": "Hudson Hawk",
        "release_date": "February 1992",
        "publisher": null
    },
    {
        "id": 283,
        "title": "The Hunt for Red October",
        "release_date": "January 1991",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 284,
        "title": "Hydlide",
        "release_date": "June 1989",
        "publisher": "FCI"
    },
    {
        "id": 285,
        "title": "Ice Climber",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 286,
        "title": "Ice Hockey",
        "release_date": "March 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 287,
        "title": "Ikari Warriors",
        "release_date": "May 1987",
        "publisher": "SNK"
    },
    {
        "id": 288,
        "title": "Ikari Warriors II: Victory Road",
        "release_date": "April 1988",
        "publisher": "SNK"
    },
    {
        "id": 289,
        "title": "Ikari Warriors III: The Rescue",
        "release_date": "February 1991",
        "publisher": "SNK"
    },
    {
        "id": 290,
        "title": "Image Fight",
        "release_date": "June 1990",
        "publisher": "Irem"
    },
    {
        "id": 291,
        "title": "The Immortal",
        "release_date": "November 1990",
        "publisher": "Electronic Arts"
    },
    {
        "id": 292,
        "title": "The Incredible Crash Dummies",
        "release_date": "August 1994",
        "publisher": "LJN"
    },
    {
        "id": 293,
        "title": "Indiana Jones and the Last Crusade",
        "release_date": "March 1991",
        "publisher": "Taito"
    },
    {
        "id": 294,
        "title": "Indiana Jones and the Last Crusade",
        "release_date": "December 1993",
        "publisher": "Ubisoft"
    },
    {
        "id": 295,
        "title": "Indiana Jones and the Temple of Doom",
        "release_date": "December 1988",
        "publisher": "Mindscape"
    },
    {
        "id": 296,
        "title": "Infiltrator",
        "release_date": "January 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 297,
        "title": "International Cricket",
        "release_date": "1992",
        "publisher": "Mattel"
    },
    {
        "id": 298,
        "title": "Iron Tank",
        "release_date": "July 1988",
        "publisher": "SNK"
    },
    {
        "id": 299,
        "title": "Ironsword: Wizards & Warriors II",
        "release_date": "December 1989",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 300,
        "title": "Isolated Warrior",
        "release_date": "February 1991",
        "publisher": "NTVIC"
    },
    {
        "id": 301,
        "title": "Ivan 'Ironman' Stewart's Super Off Road",
        "release_date": "April 1990",
        "publisher": "Tradewest"
    },
    {
        "id": 302,
        "title": "Jack Nicklaus' Greatest 18 Holes of Major Championship Golf",
        "release_date": "March 1990",
        "publisher": "Konami"
    },
    {
        "id": 303,
        "title": "Jackal",
        "release_date": "September 1988",
        "publisher": "Konami"
    },
    {
        "id": 304,
        "title": "Jackie Chan's Action Kung Fu",
        "release_date": "December 1990",
        "publisher": "Hudson Soft"
    },
    {
        "id": 305,
        "title": "James Bond Jr.",
        "release_date": "November 1992",
        "publisher": "THQ"
    },
    {
        "id": 306,
        "title": "Jaws",
        "release_date": "November 1987",
        "publisher": "LJN"
    },
    {
        "id": 307,
        "title": "Jeopardy!",
        "release_date": "September 1988",
        "publisher": "GameTek"
    },
    {
        "id": 308,
        "title": "Jeopardy! 25th Anniversary Edition",
        "release_date": "June 1990",
        "publisher": "GameTek"
    },
    {
        "id": 309,
        "title": "Jeopardy! Junior Edition",
        "release_date": "October 1989",
        "publisher": "GameTek"
    },
    {
        "id": 310,
        "title": "The Jetsons: Cogswell's Caper!",
        "release_date": "December 1992",
        "publisher": "Taito"
    },
    {
        "id": 311,
        "title": "Jimmy Connors Tennis",
        "release_date": "November 1993",
        "publisher": "Ubisoft"
    },
    {
        "id": 312,
        "title": null,
        "release_date": null,
        "publisher": null
    },
    {
        "id": 313,
        "title": "John Elway's Quarterback",
        "release_date": "March 1989",
        "publisher": "Tradewest"
    },
    {
        "id": 314,
        "title": "Jordan vs. Bird: One on One",
        "release_date": "August 1989",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 315,
        "title": "Journey to Silius",
        "release_date": "September 1990",
        "publisher": "Sunsoft"
    },
    {
        "id": 316,
        "title": "Joust",
        "release_date": "October 1988",
        "publisher": "HAL America"
    },
    {
        "id": 317,
        "title": "Jurassic Park",
        "release_date": "June 1993",
        "publisher": "Ocean Software"
    },
    {
        "id": 318,
        "title": "Kabuki Quantum Fighter",
        "release_date": "January 1991",
        "publisher": "HAL America"
    },
    {
        "id": 319,
        "title": "Karate Champ",
        "release_date": "December 1986",
        "publisher": "Data East"
    },
    {
        "id": 320,
        "title": "The Karate Kid",
        "release_date": "November 1987",
        "publisher": "LJN"
    },
    {
        "id": 321,
        "title": "Karnov",
        "release_date": "January 1988",
        "publisher": "Data East"
    },
    {
        "id": 322,
        "title": "Kick Master",
        "release_date": "January 1992",
        "publisher": "Taito"
    },
    {
        "id": 323,
        "title": "Kick Off",
        "release_date": "July 22, 1992",
        "publisher": "Imagineer"
    },
    {
        "id": 324,
        "title": "Kickle Cubicle",
        "release_date": "September 1990",
        "publisher": "Irem"
    },
    {
        "id": 325,
        "title": "Kid Icarus",
        "release_date": "July 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 326,
        "title": "Kid Klown in Night Mayor World",
        "release_date": "April 1993",
        "publisher": "Kemco"
    },
    {
        "id": 327,
        "title": "Kid Kool",
        "release_date": "March 1990",
        "publisher": "Vic Tokai"
    },
    {
        "id": 328,
        "title": "Kid Niki: Radical Ninja",
        "release_date": "November 1987",
        "publisher": "Data East"
    },
    {
        "id": 329,
        "title": "King's Knight",
        "release_date": "September 1989",
        "publisher": "Square"
    },
    {
        "id": 330,
        "title": "Kings of the Beach",
        "release_date": "January 1990",
        "publisher": "Ultra Games"
    },
    {
        "id": 331,
        "title": "King's Quest V: Absence Makes the Heart Go Yonder!",
        "release_date": "June 1992",
        "publisher": "Konami"
    },
    {
        "id": 332,
        "title": "Kirby's Adventure",
        "release_date": "May 1993",
        "publisher": null
    },
    {
        "id": 333,
        "title": "KlashBall",
        "release_date": "July 1991",
        "publisher": "SOFEL"
    },
    {
        "id": 334,
        "title": "Knight Rider",
        "release_date": "December 1989",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 335,
        "title": "Konami Hyper Soccer",
        "release_date": "1992",
        "publisher": "Konami"
    },
    {
        "id": 336,
        "title": "The Krion Conquest",
        "release_date": "January 1991",
        "publisher": "Vic Tokai"
    },
    {
        "id": 337,
        "title": "Krusty's Fun House",
        "release_date": "September 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 338,
        "title": "Kung-Fu",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 339,
        "title": "Kung-Fu Heroes",
        "release_date": "March 1989",
        "publisher": "Culture Brain"
    },
    {
        "id": 340,
        "title": "Laser Invasion",
        "release_date": "June 1991",
        "publisher": "Ultra Games"
    },
    {
        "id": 341,
        "title": "Last Action Hero",
        "release_date": "October 1993",
        "publisher": "Sony Imagesoft"
    },
    {
        "id": 342,
        "title": "The Last Ninja",
        "release_date": "February 1991",
        "publisher": "Jaleco"
    },
    {
        "id": 343,
        "title": "The Last Starfighter",
        "release_date": "June 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 344,
        "title": "Lee Trevino's Fighting Golf",
        "release_date": "September 1988",
        "publisher": "SNK"
    },
    {
        "id": 345,
        "title": "Legacy of the Wizard",
        "release_date": "April 1989",
        "publisher": "Br\u00f8derbund"
    },
    {
        "id": 346,
        "title": "The Legend of Kage",
        "release_date": "August 1987",
        "publisher": "Taito"
    },
    {
        "id": 347,
        "title": "The Legend of Prince Valiant",
        "release_date": "1992",
        "publisher": "Ocean Software"
    },
    {
        "id": 348,
        "title": "The Legend of Zelda",
        "release_date": "August 22, 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 349,
        "title": "Legendary Wings",
        "release_date": "July 1988",
        "publisher": "Capcom"
    },
    {
        "id": 350,
        "title": "Legends of the Diamond",
        "release_date": "January 1992",
        "publisher": "Bandai"
    },
    {
        "id": 351,
        "title": "Lemmings",
        "release_date": "November 1992",
        "publisher": "Sunsoft"
    },
    {
        "id": 352,
        "title": "L'Empereur",
        "release_date": "November 1991",
        "publisher": "Koei"
    },
    {
        "id": 353,
        "title": null,
        "release_date": "1987",
        "publisher": null
    },
    {
        "id": 354,
        "title": "Lethal Weapon",
        "release_date": "April 1993",
        "publisher": "Ocean Software"
    },
    {
        "id": 355,
        "title": "Life Force",
        "release_date": "August 1988",
        "publisher": "Konami"
    },
    {
        "id": 356,
        "title": "Little League Baseball: Championship Series",
        "release_date": "July 1990",
        "publisher": "SNK"
    },
    {
        "id": 357,
        "title": "Little Nemo: The Dream Master",
        "release_date": "September 1990",
        "publisher": null
    },
    {
        "id": 358,
        "title": "Little Ninja Brothers",
        "release_date": "December 1990",
        "publisher": "Culture Brain"
    },
    {
        "id": 359,
        "title": "Little Samson",
        "release_date": "November 1992",
        "publisher": "Taito"
    },
    {
        "id": 360,
        "title": "Lode Runner",
        "release_date": "September 1987",
        "publisher": "Br\u00f8derbund"
    },
    {
        "id": 361,
        "title": "The Lone Ranger",
        "release_date": "August 1991",
        "publisher": "Konami"
    },
    {
        "id": 362,
        "title": "Loopz",
        "release_date": "October 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 363,
        "title": "Low G Man: The Low Gravity Man",
        "release_date": "September 1990",
        "publisher": "Taxan"
    },
    {
        "id": 364,
        "title": "Lunar Pool",
        "release_date": "October 1987",
        "publisher": "FCI"
    },
    {
        "id": 365,
        "title": "M.C. Kids",
        "release_date": "February 1992",
        "publisher": null
    },
    {
        "id": 366,
        "title": "M.U.L.E.",
        "release_date": "September 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 367,
        "title": "M.U.S.C.L.E.",
        "release_date": "October 29, 1986",
        "publisher": "Bandai"
    },
    {
        "id": 368,
        "title": "Mach Rider",
        "release_date": "August 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 369,
        "title": "Mad Max",
        "release_date": "July 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 370,
        "title": "The Mafat Conspiracy",
        "release_date": "June 1990",
        "publisher": "Vic Tokai"
    },
    {
        "id": 371,
        "title": "Magic Darts",
        "release_date": "September 1991",
        "publisher": "Romstar"
    },
    {
        "id": 372,
        "title": "Magic Johnson's Fast Break",
        "release_date": "March 1990",
        "publisher": "Tradewest"
    },
    {
        "id": 373,
        "title": "The Magic of Scheherazade",
        "release_date": "December 1989",
        "publisher": "Culture Brain"
    },
    {
        "id": 374,
        "title": "Magician",
        "release_date": "February 1991",
        "publisher": "Taxan"
    },
    {
        "id": 375,
        "title": "MagMax",
        "release_date": "October 1988",
        "publisher": "FCI"
    },
    {
        "id": 376,
        "title": "Major League Baseball",
        "release_date": "April 1988",
        "publisher": "LJN"
    },
    {
        "id": 377,
        "title": "Maniac Mansion",
        "release_date": "September 1990",
        "publisher": "Jaleco"
    },
    {
        "id": 378,
        "title": "Mappy-Land",
        "release_date": "April 1989",
        "publisher": "Taxan"
    },
    {
        "id": 379,
        "title": "Marble Madness",
        "release_date": "March 1989",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 380,
        "title": "Mario Bros.",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 381,
        "title": "Mario Is Missing!",
        "release_date": "July 1993",
        "publisher": "Mindscape"
    },
    {
        "id": 382,
        "title": "Mario's Time Machine",
        "release_date": "June 1994",
        "publisher": "Mindscape"
    },
    {
        "id": 383,
        "title": "Mechanized Attack",
        "release_date": "June 1990",
        "publisher": "SNK"
    },
    {
        "id": 384,
        "title": "Mega Man",
        "release_date": "December 1987",
        "publisher": "Capcom"
    },
    {
        "id": 385,
        "title": "Mega Man 2",
        "release_date": "June 1989",
        "publisher": "Capcom"
    },
    {
        "id": 386,
        "title": "Mega Man 3",
        "release_date": "November 1990",
        "publisher": null
    },
    {
        "id": 387,
        "title": "Mega Man 4",
        "release_date": "January 1992",
        "publisher": null
    },
    {
        "id": 388,
        "title": "Mega Man 5",
        "release_date": "December 1992",
        "publisher": null
    },
    {
        "id": 389,
        "title": "Mega Man 6",
        "release_date": "March 1994",
        "publisher": "Nintendo"
    },
    {
        "id": 390,
        "title": "Mendel Palace",
        "release_date": "October 1990",
        "publisher": "Hudson Soft"
    },
    {
        "id": 391,
        "title": "Metal Gear",
        "release_date": "June 1988",
        "publisher": null
    },
    {
        "id": 392,
        "title": "Metal Mech",
        "release_date": "March 1991",
        "publisher": "Jaleco"
    },
    {
        "id": 393,
        "title": "Metal Storm",
        "release_date": "February 1991",
        "publisher": "Irem"
    },
    {
        "id": 394,
        "title": "Metroid",
        "release_date": "August 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 395,
        "title": "Michael Andretti's World GP",
        "release_date": "June 1990",
        "publisher": "American Sammy"
    },
    {
        "id": 396,
        "title": "Mickey Mousecapade",
        "release_date": "October 1988",
        "publisher": "Capcom"
    },
    {
        "id": 397,
        "title": "Mickey's Adventures in Numberland",
        "release_date": "March 1994",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 398,
        "title": "Mickey's Safari in Letterland",
        "release_date": "March 1993",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 399,
        "title": "Might and Magic Book One: The Secret of the Inner Sanctum",
        "release_date": "August 1992",
        "publisher": "American Sammy"
    },
    {
        "id": 400,
        "title": "Mighty Bomb Jack",
        "release_date": "July 1987",
        "publisher": "Tecmo"
    },
    {
        "id": 401,
        "title": "Mighty Final Fight",
        "release_date": "July 1993",
        "publisher": "Capcom"
    },
    {
        "id": 402,
        "title": "Mike Tyson's Punch-Out!!",
        "release_date": "October 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 403,
        "title": "Millipede",
        "release_date": "October 1988",
        "publisher": "HAL America"
    },
    {
        "id": 404,
        "title": "Milon's Secret Castle",
        "release_date": "September 1988",
        "publisher": "Hudson Soft"
    },
    {
        "id": 405,
        "title": "Miracle Piano Teaching System",
        "release_date": "1990",
        "publisher": "Mindscape"
    },
    {
        "id": 406,
        "title": "Mission: Impossible",
        "release_date": "September 1990",
        "publisher": "Ultra Games"
    },
    {
        "id": 407,
        "title": "Monopoly",
        "release_date": "May 1991",
        "publisher": "Parker Brothers"
    },
    {
        "id": 408,
        "title": "Monster in My Pocket",
        "release_date": "January 1992",
        "publisher": "Konami"
    },
    {
        "id": 409,
        "title": "Monster Party",
        "release_date": "June 1989",
        "publisher": "Bandai"
    },
    {
        "id": 410,
        "title": "Monster Truck Rally",
        "release_date": "September 1991",
        "publisher": "INTV"
    },
    {
        "id": 411,
        "title": "Motor City Patrol",
        "release_date": "January 1992",
        "publisher": "Matchbox"
    },
    {
        "id": 412,
        "title": "Mr. Gimmick!",
        "release_date": "May 19, 1993",
        "publisher": "Sunsoft"
    },
    {
        "id": 413,
        "title": "Ms. Pac-Man",
        "release_date": "November 1993",
        "publisher": "Namco"
    },
    {
        "id": 414,
        "title": "Muppet Adventure: Chaos at the Carnival",
        "release_date": "November 1990",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 415,
        "title": "The Mutant Virus: Crisis in a Computer World",
        "release_date": "April 1992",
        "publisher": "American Softworks"
    },
    {
        "id": 416,
        "title": "Mystery Quest",
        "release_date": "April 1989",
        "publisher": "Taxan"
    },
    {
        "id": 417,
        "title": "NARC",
        "release_date": "August 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 418,
        "title": "NES Open Tournament Golf",
        "release_date": "September 1991",
        "publisher": "Nintendo"
    },
    {
        "id": 419,
        "title": "NES Play Action Football",
        "release_date": "September 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 420,
        "title": "New Ghostbusters II",
        "release_date": "1990",
        "publisher": "HAL America"
    },
    {
        "id": 421,
        "title": null,
        "release_date": null,
        "publisher": null
    },
    {
        "id": 422,
        "title": "NFL Football",
        "release_date": "September 1989",
        "publisher": "LJN"
    },
    {
        "id": 423,
        "title": "Nigel Mansell's World Championship Racing",
        "release_date": "October 1993",
        "publisher": "GameTek"
    },
    {
        "id": 424,
        "title": "A Nightmare on Elm Street",
        "release_date": "October 1990",
        "publisher": "LJN"
    },
    {
        "id": 425,
        "title": "Nightshade",
        "release_date": "January 1992",
        "publisher": "Ultra Games"
    },
    {
        "id": 426,
        "title": "Ninja Crusaders",
        "release_date": "December 1990",
        "publisher": "American Sammy"
    },
    {
        "id": 427,
        "title": null,
        "release_date": null,
        "publisher": "Tecmo"
    },
    {
        "id": 428,
        "title": null,
        "release_date": null,
        "publisher": "Tecmo"
    },
    {
        "id": 429,
        "title": "Ninja Gaiden III: The Ancient Ship of Doom",
        "release_date": "August 1991",
        "publisher": "Tecmo"
    },
    {
        "id": 430,
        "title": "Ninja Kid",
        "release_date": "October 29, 1986",
        "publisher": "Bandai"
    },
    {
        "id": 431,
        "title": "Nintendo Campus Challenge",
        "release_date": "1991",
        "publisher": "Nintendo"
    },
    {
        "id": 432,
        "title": "Nintendo World Championships",
        "release_date": "1990",
        "publisher": "Nintendo"
    },
    {
        "id": 433,
        "title": "Nintendo World Cup",
        "release_date": "December 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 434,
        "title": "Noah's Ark",
        "release_date": "1992",
        "publisher": "Konami"
    },
    {
        "id": 435,
        "title": "Nobunaga's Ambition",
        "release_date": "June 1989",
        "publisher": "Koei"
    },
    {
        "id": 436,
        "title": "Nobunaga's Ambition II",
        "release_date": "April 1991",
        "publisher": "Koei"
    },
    {
        "id": 437,
        "title": "North & South",
        "release_date": "December 1990",
        "publisher": "Seika"
    },
    {
        "id": 438,
        "title": "Operation Wolf",
        "release_date": "May 1989",
        "publisher": "Taito"
    },
    {
        "id": 439,
        "title": "Orb-3D",
        "release_date": "October 1990",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 440,
        "title": "Othello",
        "release_date": "December 1988",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 441,
        "title": "Over Horizon",
        "release_date": "1991",
        "publisher": "Hot-B"
    },
    {
        "id": 442,
        "title": "Overlord",
        "release_date": "January 1993",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 443,
        "title": "P.O.W.: Prisoners of War",
        "release_date": "September 1989",
        "publisher": "SNK"
    },
    {
        "id": 444,
        "title": "Pac-Man",
        "release_date": "November 1993",
        "publisher": "Namco"
    },
    {
        "id": 445,
        "title": "Pac-Man",
        "release_date": "October 1988",
        "publisher": "Tengen"
    },
    {
        "id": 446,
        "title": "Palamedes",
        "release_date": "November 1990",
        "publisher": "Hot-B"
    },
    {
        "id": 447,
        "title": "Panic Restaurant",
        "release_date": "August 1992",
        "publisher": "Taito"
    },
    {
        "id": 448,
        "title": "Paperboy",
        "release_date": "December 1988",
        "publisher": "Mindscape"
    },
    {
        "id": 449,
        "title": "Paperboy 2",
        "release_date": "April 1992",
        "publisher": "Mindscape"
    },
    {
        "id": 450,
        "title": "Parasol Stars: The Story of Bubble Bobble 3",
        "release_date": "1991",
        "publisher": "Ocean Software"
    },
    {
        "id": 451,
        "title": "Parodius Da!",
        "release_date": "1992",
        "publisher": "Palcom"
    },
    {
        "id": 452,
        "title": "Peter Pan and the Pirates",
        "release_date": "January 1991",
        "publisher": "THQ"
    },
    {
        "id": 453,
        "title": "Phantom Fighter",
        "release_date": "April 1990",
        "publisher": "FCI"
    },
    {
        "id": 454,
        "title": "Pictionary",
        "release_date": "July 1990",
        "publisher": "LJN"
    },
    {
        "id": 455,
        "title": "Pinball",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 456,
        "title": "Pinball Quest",
        "release_date": "June 1990",
        "publisher": "Jaleco"
    },
    {
        "id": 457,
        "title": "Pin*Bot",
        "release_date": "April 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 458,
        "title": "Pipe Dream",
        "release_date": "September 1990",
        "publisher": "Bullet-Proof Software"
    },
    {
        "id": 459,
        "title": "Pirates!",
        "release_date": "October 1991",
        "publisher": "Ultra Games"
    },
    {
        "id": 460,
        "title": "Platoon",
        "release_date": "December 1988",
        "publisher": "Sunsoft"
    },
    {
        "id": 461,
        "title": "Popeye",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 462,
        "title": "Power Blade",
        "release_date": "March 1991",
        "publisher": "Taito"
    },
    {
        "id": 463,
        "title": "Power Blade 2",
        "release_date": "October 1992",
        "publisher": "Taito"
    },
    {
        "id": 464,
        "title": "Power Punch II",
        "release_date": "June 1992",
        "publisher": "American Softworks"
    },
    {
        "id": 465,
        "title": "Predator",
        "release_date": "April 1989",
        "publisher": "Activision"
    },
    {
        "id": 466,
        "title": "Prince of Persia",
        "release_date": "November 1992",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 467,
        "title": "Princess Tomato in the Salad Kingdom",
        "release_date": "February 1991",
        "publisher": "Hudson Soft"
    },
    {
        "id": 468,
        "title": "Pro Sport Hockey",
        "release_date": "November 1993",
        "publisher": "Jaleco"
    },
    {
        "id": 469,
        "title": "Pro Wrestling",
        "release_date": "March 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 470,
        "title": "Punch-Out!!",
        "release_date": "August 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 471,
        "title": "The Punisher",
        "release_date": "November 1990",
        "publisher": "LJN"
    },
    {
        "id": 472,
        "title": "Puss 'n Boots: Pero's Great Adventure",
        "release_date": "June 1990",
        "publisher": "Electro Brain"
    },
    {
        "id": 473,
        "title": "Puzznic",
        "release_date": "November 1990",
        "publisher": "Taito"
    },
    {
        "id": 474,
        "title": "Q*bert",
        "release_date": "February 1989",
        "publisher": "Ultra Games"
    },
    {
        "id": 475,
        "title": "Qix",
        "release_date": "January 1991",
        "publisher": "Taito"
    },
    {
        "id": 476,
        "title": "R.B.I. Baseball",
        "release_date": "June 1988",
        "publisher": "Tengen"
    },
    {
        "id": 477,
        "title": "R.C. Pro-Am",
        "release_date": "March 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 478,
        "title": "R.C. Pro-Am II",
        "release_date": "December 1992",
        "publisher": "Tradewest"
    },
    {
        "id": 479,
        "title": "Race America",
        "release_date": "May 1992",
        "publisher": null
    },
    {
        "id": 480,
        "title": "Racket Attack",
        "release_date": "October 1988",
        "publisher": "Jaleco"
    },
    {
        "id": 481,
        "title": "Rackets & Rivals",
        "release_date": "1993",
        "publisher": "Palcom"
    },
    {
        "id": 482,
        "title": "Rad Racer",
        "release_date": "October 1, 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 483,
        "title": "Rad Racer II",
        "release_date": "June 1990",
        "publisher": "Square"
    },
    {
        "id": 484,
        "title": "Raid on Bungeling Bay",
        "release_date": "September 1987",
        "publisher": "Br\u00f8derbund"
    },
    {
        "id": 485,
        "title": "Rainbow Islands: The Story of Bubble Bobble 2",
        "release_date": "June 1991",
        "publisher": null
    },
    {
        "id": 486,
        "title": "Rally Bike",
        "release_date": "September 1990",
        "publisher": "Romstar"
    },
    {
        "id": 487,
        "title": "Rambo",
        "release_date": "May 1988",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 488,
        "title": "Rampage",
        "release_date": "December 1988",
        "publisher": "Data East"
    },
    {
        "id": 489,
        "title": "Rampart",
        "release_date": "January 1992",
        "publisher": "Jaleco"
    },
    {
        "id": 490,
        "title": "Remote Control",
        "release_date": "May 1990",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 491,
        "title": "The Ren & Stimpy Show: Buckaroo$!",
        "release_date": "November 1993",
        "publisher": "THQ"
    },
    {
        "id": 492,
        "title": "Renegade",
        "release_date": "January 1988",
        "publisher": "Taito"
    },
    {
        "id": 493,
        "title": "Rescue: The Embassy Mission",
        "release_date": "January 1990",
        "publisher": "Seika"
    },
    {
        "id": 494,
        "title": "Ring King",
        "release_date": "September 1987",
        "publisher": "Data East"
    },
    {
        "id": 495,
        "title": "River City Ransom",
        "release_date": "January 1990",
        "publisher": null
    },
    {
        "id": 496,
        "title": "Road Fighter",
        "release_date": "1991",
        "publisher": "Palcom"
    },
    {
        "id": 497,
        "title": "RoadBlasters",
        "release_date": "January 1990",
        "publisher": "Mindscape"
    },
    {
        "id": 498,
        "title": "Robin Hood: Prince of Thieves",
        "release_date": "November 1991",
        "publisher": "Virgin Interactive"
    },
    {
        "id": 499,
        "title": "RoboCop",
        "release_date": "December 1989",
        "publisher": null
    },
    {
        "id": 500,
        "title": "RoboCop 2",
        "release_date": "April 1991",
        "publisher": null
    },
    {
        "id": 501,
        "title": "RoboCop 3",
        "release_date": "August 1992",
        "publisher": "Ocean Software"
    },
    {
        "id": 502,
        "title": "Robowarrior",
        "release_date": "December 1988",
        "publisher": "Jaleco"
    },
    {
        "id": 503,
        "title": "Rock 'n Ball",
        "release_date": "January 1990",
        "publisher": "NTVIC"
    },
    {
        "id": 504,
        "title": "Rocket Ranger",
        "release_date": "June 1990",
        "publisher": "Seika"
    },
    {
        "id": 505,
        "title": "The Rocketeer",
        "release_date": "May 1991",
        "publisher": "Bandai"
    },
    {
        "id": 506,
        "title": "Rockin' Kats",
        "release_date": "September 1991",
        "publisher": "Atlus"
    },
    {
        "id": 507,
        "title": "Rod Land",
        "release_date": "1993",
        "publisher": "Jaleco"
    },
    {
        "id": 508,
        "title": "Roger Clemens' MVP Baseball",
        "release_date": "October 1991",
        "publisher": "LJN"
    },
    {
        "id": 509,
        "title": "Rollerball",
        "release_date": "February 1990",
        "publisher": "HAL America"
    },
    {
        "id": 510,
        "title": "Rollerblade Racer",
        "release_date": "February 1993",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 511,
        "title": "RollerGames",
        "release_date": "September 1990",
        "publisher": "Ultra Games"
    },
    {
        "id": 512,
        "title": "Romance of the Three Kingdoms",
        "release_date": "October 1989",
        "publisher": "Koei"
    },
    {
        "id": 513,
        "title": "Romance of the Three Kingdoms II",
        "release_date": "September 1991",
        "publisher": "Koei"
    },
    {
        "id": 514,
        "title": "Roundball: 2 on 2 Challenge",
        "release_date": "May 1992",
        "publisher": "Mindscape"
    },
    {
        "id": 515,
        "title": "Rush'n Attack",
        "release_date": "April 1987",
        "publisher": "Konami"
    },
    {
        "id": 516,
        "title": "Rygar",
        "release_date": "July 1987",
        "publisher": "Tecmo"
    },
    {
        "id": 517,
        "title": null,
        "release_date": "June 1991",
        "publisher": null
    },
    {
        "id": 518,
        "title": "Section Z",
        "release_date": "July 1987",
        "publisher": "Capcom"
    },
    {
        "id": 519,
        "title": "Seicross",
        "release_date": "October 1988",
        "publisher": "FCI"
    },
    {
        "id": 520,
        "title": "Sesame Street: 1-2-3",
        "release_date": "January 1989",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 521,
        "title": "Sesame Street: A-B-C",
        "release_date": "September 1989",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 522,
        "title": "Sesame Street: A-B-C/1-2-3",
        "release_date": "November 1991",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 523,
        "title": "Sesame Street: Big Bird's Hide & Speak",
        "release_date": "October 1990",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 524,
        "title": "Sesame Street: Countdown",
        "release_date": "February 1992",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 525,
        "title": null,
        "release_date": "December 1990",
        "publisher": null
    },
    {
        "id": 526,
        "title": "Shadowgate",
        "release_date": "December 1989",
        "publisher": "Seika"
    },
    {
        "id": 527,
        "title": "Shatterhand",
        "release_date": "December 1991",
        "publisher": "Jaleco"
    },
    {
        "id": 528,
        "title": "Shingen the Ruler",
        "release_date": "June 1990",
        "publisher": "Hot-B"
    },
    {
        "id": 529,
        "title": "Shooting Range",
        "release_date": "June 1989",
        "publisher": "Bandai"
    },
    {
        "id": 530,
        "title": "Short Order / Eggsplode!",
        "release_date": "December 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 531,
        "title": "Side Pocket",
        "release_date": "November 30, 1987",
        "publisher": "Data East"
    },
    {
        "id": 532,
        "title": "Silent Service",
        "release_date": "December 1989",
        "publisher": null
    },
    {
        "id": 533,
        "title": "Silkworm",
        "release_date": "June 1990",
        "publisher": "American Sammy"
    },
    {
        "id": 534,
        "title": "Silver Surfer",
        "release_date": "November 1990",
        "publisher": "Arcadia Systems"
    },
    {
        "id": 535,
        "title": "The Simpsons: Bart vs. the Space Mutants",
        "release_date": "February 1991",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 536,
        "title": "The Simpsons: Bart vs. the World",
        "release_date": "December 1991",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 537,
        "title": "The Simpsons: Bartman Meets Radioactive Man",
        "release_date": "December 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 538,
        "title": "Skate or Die!",
        "release_date": "December 1988",
        "publisher": "Ultra Games"
    },
    {
        "id": 539,
        "title": "Skate or Die 2: The Search for Double Trouble",
        "release_date": "September 1990",
        "publisher": "Electronic Arts"
    },
    {
        "id": 540,
        "title": "Ski or Die",
        "release_date": "February 1991",
        "publisher": "Ultra Games"
    },
    {
        "id": 541,
        "title": "Sky Kid",
        "release_date": "September 1987",
        "publisher": "Sunsoft"
    },
    {
        "id": 542,
        "title": "Sky Shark",
        "release_date": "September 1989",
        "publisher": "Taito"
    },
    {
        "id": 543,
        "title": "Slalom",
        "release_date": "March 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 544,
        "title": "Smash TV",
        "release_date": "September 1991",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 545,
        "title": "The Smurfs",
        "release_date": "1994",
        "publisher": "Infogrames"
    },
    {
        "id": 546,
        "title": "Snake Rattle 'n' Roll",
        "release_date": "July 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 547,
        "title": "Snake's Revenge",
        "release_date": "April 1990",
        "publisher": null
    },
    {
        "id": 548,
        "title": "Snoopy's Silly Sports Spectacular",
        "release_date": "April 1990",
        "publisher": "Seika"
    },
    {
        "id": 549,
        "title": "Snow Brothers",
        "release_date": "November 1991",
        "publisher": "Capcom"
    },
    {
        "id": 550,
        "title": "Soccer",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 551,
        "title": "Solar Jetman: Hunt for the Golden Warpship",
        "release_date": "September 1990",
        "publisher": "Tradewest"
    },
    {
        "id": 552,
        "title": "Solomon's Key",
        "release_date": "July 1987",
        "publisher": "Tecmo"
    },
    {
        "id": 553,
        "title": "Solstice: The Quest for the Staff of Demnos",
        "release_date": "June 1990",
        "publisher": null
    },
    {
        "id": 554,
        "title": "Space Shuttle Project",
        "release_date": "November 1991",
        "publisher": "Absolute Entertainment"
    },
    {
        "id": 555,
        "title": "Spelunker",
        "release_date": "September 1987",
        "publisher": "Br\u00f8derbund"
    },
    {
        "id": 556,
        "title": "Spider-Man: Return of the Sinister Six",
        "release_date": "October 1992",
        "publisher": "LJN"
    },
    {
        "id": 557,
        "title": "Spot: The Video Game",
        "release_date": "September 1990",
        "publisher": "Arcadia Systems"
    },
    {
        "id": 558,
        "title": "Spy Hunter",
        "release_date": "September 1987",
        "publisher": "Sunsoft"
    },
    {
        "id": 559,
        "title": "Spy vs. Spy",
        "release_date": "October 1988",
        "publisher": "Seika"
    },
    {
        "id": 560,
        "title": "Sqoon",
        "release_date": "September 1987",
        "publisher": "Irem"
    },
    {
        "id": 561,
        "title": "Stack-Up",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 562,
        "title": "Stadium Events",
        "release_date": "September 1987",
        "publisher": "Bandai"
    },
    {
        "id": 563,
        "title": "Stanley: The Search for Dr. Livingston",
        "release_date": "October 1992",
        "publisher": "Electro Brain"
    },
    {
        "id": 564,
        "title": "Star Force",
        "release_date": "November 1987",
        "publisher": "Tecmo"
    },
    {
        "id": 565,
        "title": "Star Soldier",
        "release_date": "January 1989",
        "publisher": "Taxan"
    },
    {
        "id": 566,
        "title": "Star Trek: 25th Anniversary",
        "release_date": "February 1992",
        "publisher": "Ultra Games"
    },
    {
        "id": 567,
        "title": "Star Trek: The Next Generation",
        "release_date": "September 1993",
        "publisher": "Absolute Entertainment"
    },
    {
        "id": 568,
        "title": "Star Voyager",
        "release_date": "September 1987",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 569,
        "title": "Star Wars",
        "release_date": "November 1991",
        "publisher": null
    },
    {
        "id": 570,
        "title": "Star Wars: The Empire Strikes Back",
        "release_date": "March 1992",
        "publisher": "JVC"
    },
    {
        "id": 571,
        "title": "Starship Hector",
        "release_date": "June 1990",
        "publisher": "Hudson Soft"
    },
    {
        "id": 572,
        "title": "StarTropics",
        "release_date": "December 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 573,
        "title": "Stealth ATF",
        "release_date": "October 1989",
        "publisher": "Activision"
    },
    {
        "id": 574,
        "title": "Stinger",
        "release_date": "September 1987",
        "publisher": "Konami"
    },
    {
        "id": 575,
        "title": "Street Cop",
        "release_date": "June 1989",
        "publisher": "Bandai"
    },
    {
        "id": 576,
        "title": "Street Fighter 2010: The Final Fight",
        "release_date": "September 1990",
        "publisher": "Capcom"
    },
    {
        "id": 577,
        "title": "Strider",
        "release_date": "July 1989",
        "publisher": "Capcom"
    },
    {
        "id": 578,
        "title": "Super C",
        "release_date": "April 1990",
        "publisher": "Konami"
    },
    {
        "id": 579,
        "title": "Super Cars",
        "release_date": "February 1991",
        "publisher": "Electro Brain"
    },
    {
        "id": 580,
        "title": "Super Dodge Ball",
        "release_date": "July 1989",
        "publisher": "Sony Imagesoft"
    },
    {
        "id": 581,
        "title": "Super Glove Ball",
        "release_date": "October 1990",
        "publisher": "Mattel"
    },
    {
        "id": 582,
        "title": "Super Jeopardy!",
        "release_date": "September 1991",
        "publisher": "GameTek"
    },
    {
        "id": 583,
        "title": "Super Mario Bros.",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 584,
        "title": "Super Mario Bros./Duck Hunt",
        "release_date": "November 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 585,
        "title": "Super Mario Bros./Duck Hunt/World Class Track Meet",
        "release_date": "December 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 586,
        "title": "Super Mario Bros./Tetris/Nintendo World Cup",
        "release_date": "November 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 587,
        "title": "Super Mario Bros. 2",
        "release_date": "October 10, 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 588,
        "title": "Super Mario Bros. 3",
        "release_date": "February 12, 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 589,
        "title": "Super Pitfall",
        "release_date": "November 1987",
        "publisher": null
    },
    {
        "id": 590,
        "title": "Super Spike V'Ball",
        "release_date": "February 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 591,
        "title": "Super Spike V'Ball/Nintendo World Cup",
        "release_date": "December 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 592,
        "title": "Super Spy Hunter",
        "release_date": "February 1992",
        "publisher": "Sunsoft"
    },
    {
        "id": 593,
        "title": "Super Team Games",
        "release_date": "November 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 594,
        "title": "Super Turrican",
        "release_date": "1992",
        "publisher": "Imagineer"
    },
    {
        "id": 595,
        "title": "Superman",
        "release_date": "December 1988",
        "publisher": "Seika"
    },
    {
        "id": 596,
        "title": "Swamp Thing",
        "release_date": "December 1992",
        "publisher": "THQ"
    },
    {
        "id": 597,
        "title": "Sword Master",
        "release_date": "January 1992",
        "publisher": "Activision"
    },
    {
        "id": 598,
        "title": "Swords and Serpents",
        "release_date": "August 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 599,
        "title": "Taboo: The Sixth Sense",
        "release_date": "April 1989",
        "publisher": "Tradewest"
    },
    {
        "id": 600,
        "title": "Tag Team Wrestling",
        "release_date": "October 1986",
        "publisher": "Data East"
    },
    {
        "id": 601,
        "title": "TaleSpin",
        "release_date": "December 1991",
        "publisher": "Capcom"
    },
    {
        "id": 602,
        "title": "Target: Renegade",
        "release_date": "March 1990",
        "publisher": "Taito"
    },
    {
        "id": 603,
        "title": "Tecmo Baseball",
        "release_date": "January 1989",
        "publisher": "Tecmo"
    },
    {
        "id": 604,
        "title": "Tecmo Bowl",
        "release_date": "February 1989",
        "publisher": "Tecmo"
    },
    {
        "id": 605,
        "title": "Tecmo Cup Soccer Game",
        "release_date": "September 1992",
        "publisher": "Tecmo"
    },
    {
        "id": 606,
        "title": "Tecmo NBA Basketball",
        "release_date": "November 1992",
        "publisher": "Tecmo"
    },
    {
        "id": 607,
        "title": "Tecmo Super Bowl",
        "release_date": "December 1991",
        "publisher": "Tecmo"
    },
    {
        "id": 608,
        "title": "Tecmo World Cup Soccer",
        "release_date": "1991",
        "publisher": "Tecmo"
    },
    {
        "id": 609,
        "title": "Tecmo World Wrestling",
        "release_date": "April 1990",
        "publisher": "Tecmo"
    },
    {
        "id": 610,
        "title": "Teenage Mutant Ninja Turtles",
        "release_date": "June 1989",
        "publisher": "Ultra Games"
    },
    {
        "id": 611,
        "title": "Teenage Mutant Ninja Turtles II: The Arcade Game",
        "release_date": "December 1990",
        "publisher": null
    },
    {
        "id": 612,
        "title": "Teenage Mutant Ninja Turtles III: The Manhattan Project",
        "release_date": "February 1992",
        "publisher": "Konami"
    },
    {
        "id": 613,
        "title": "Teenage Mutant Ninja Turtles: Tournament Fighters",
        "release_date": "February 1994",
        "publisher": "Konami"
    },
    {
        "id": 614,
        "title": "Tennis",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 615,
        "title": "The Terminator",
        "release_date": "December 1992",
        "publisher": "Mindscape"
    },
    {
        "id": 616,
        "title": "Terminator 2: Judgment Day",
        "release_date": "February 1992",
        "publisher": "LJN"
    },
    {
        "id": 617,
        "title": "Terra Cresta",
        "release_date": "March 1990",
        "publisher": "Vic Tokai"
    },
    {
        "id": 618,
        "title": "Tetris",
        "release_date": "November 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 619,
        "title": "Tetris 2",
        "release_date": "October 1993",
        "publisher": "Nintendo"
    },
    {
        "id": 620,
        "title": "The Three Stooges",
        "release_date": "October 1989",
        "publisher": "Activision"
    },
    {
        "id": 621,
        "title": "Thunder & Lightning",
        "release_date": "December 1990",
        "publisher": "Romstar"
    },
    {
        "id": 622,
        "title": "Thunderbirds",
        "release_date": "September 1990",
        "publisher": "Activision"
    },
    {
        "id": 623,
        "title": "Thundercade",
        "release_date": "July 1989",
        "publisher": "American Sammy"
    },
    {
        "id": 624,
        "title": "Tiger Heli",
        "release_date": "September 1987",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 625,
        "title": "Time Lord",
        "release_date": "September 1990",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 626,
        "title": "Times of Lore",
        "release_date": "May 1991",
        "publisher": "Toho"
    },
    {
        "id": 627,
        "title": "Tiny Toon Adventures",
        "release_date": "December 1991",
        "publisher": "Konami"
    },
    {
        "id": 628,
        "title": "Tiny Toon Adventures 2: Trouble in Wackyland",
        "release_date": "April 1993",
        "publisher": "Konami"
    },
    {
        "id": 629,
        "title": "Tiny Toon Adventures Cartoon Workshop",
        "release_date": "December 1992",
        "publisher": "Konami"
    },
    {
        "id": 630,
        "title": "To the Earth",
        "release_date": "November 1989",
        "publisher": "Nintendo"
    },
    {
        "id": 631,
        "title": "Toki",
        "release_date": "December 1991",
        "publisher": "Taito"
    },
    {
        "id": 632,
        "title": "Tom and Jerry",
        "release_date": "December 1991",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 633,
        "title": "Tombs & Treasure",
        "release_date": "June 1991",
        "publisher": "Activision"
    },
    {
        "id": 634,
        "title": "Top Gun",
        "release_date": "November 1987",
        "publisher": "Konami"
    },
    {
        "id": 635,
        "title": "Top Gun: The Second Mission",
        "release_date": "January 1990",
        "publisher": "Konami"
    },
    {
        "id": 636,
        "title": null,
        "release_date": "January 1990",
        "publisher": "Asmik"
    },
    {
        "id": 637,
        "title": "Total Recall",
        "release_date": "August 1990",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 638,
        "title": "Totally Rad",
        "release_date": "March 1991",
        "publisher": "Jaleco"
    },
    {
        "id": 639,
        "title": "Touch Down Fever",
        "release_date": "February 1991",
        "publisher": "SNK"
    },
    {
        "id": 640,
        "title": "Town & Country Surf Designs: Wood & Water Rage",
        "release_date": "February 1988",
        "publisher": "LJN"
    },
    {
        "id": 641,
        "title": "Town & Country II: Thrilla's Surfari",
        "release_date": "March 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 642,
        "title": "Toxic Crusaders",
        "release_date": "April 1992",
        "publisher": "Bandai"
    },
    {
        "id": 643,
        "title": "Track & Field",
        "release_date": "April 1987",
        "publisher": "Konami"
    },
    {
        "id": 644,
        "title": "Track & Field II",
        "release_date": "June 1989",
        "publisher": "Konami"
    },
    {
        "id": 645,
        "title": "Treasure Master",
        "release_date": "December 1991",
        "publisher": "American Softworks"
    },
    {
        "id": 646,
        "title": "Trog!",
        "release_date": "October 1991",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 647,
        "title": "Trojan",
        "release_date": "February 1987",
        "publisher": "Capcom"
    },
    {
        "id": 648,
        "title": "The Trolls in Crazyland",
        "release_date": "1991",
        "publisher": "American Softworks"
    },
    {
        "id": 649,
        "title": "Twin Cobra",
        "release_date": "January 1990",
        "publisher": "American Sammy"
    },
    {
        "id": 650,
        "title": "Twin Eagle",
        "release_date": "October 1989",
        "publisher": "Romstar"
    },
    {
        "id": 651,
        "title": "Ufouria: The Saga",
        "release_date": "November 19, 1992",
        "publisher": "Sunsoft"
    },
    {
        "id": 652,
        "title": "Ultima III: Exodus",
        "release_date": "February 1989",
        "publisher": "FCI"
    },
    {
        "id": 653,
        "title": "Ultima IV: Quest of the Avatar",
        "release_date": "December 1990",
        "publisher": "FCI"
    },
    {
        "id": 654,
        "title": "Ultima V: Warriors of Destiny",
        "release_date": "January 1993",
        "publisher": "FCI"
    },
    {
        "id": 655,
        "title": "Ultimate Air Combat",
        "release_date": "April 1992",
        "publisher": "Activision"
    },
    {
        "id": 656,
        "title": "Ultimate Basketball",
        "release_date": "September 1990",
        "publisher": "American Sammy"
    },
    {
        "id": 657,
        "title": "The Uncanny X-Men",
        "release_date": "December 1989",
        "publisher": "LJN"
    },
    {
        "id": 658,
        "title": "Uncharted Waters",
        "release_date": "November 1991",
        "publisher": "Koei"
    },
    {
        "id": 659,
        "title": "Uninvited",
        "release_date": "June 1991",
        "publisher": "Seika"
    },
    {
        "id": 660,
        "title": "The Untouchables",
        "release_date": "January 1991",
        "publisher": "Ocean Software"
    },
    {
        "id": 661,
        "title": "Urban Champion",
        "release_date": "August 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 662,
        "title": "Vegas Dream",
        "release_date": "March 1990",
        "publisher": "HAL America"
    },
    {
        "id": 663,
        "title": "Vice: Project Doom",
        "release_date": "November 1991",
        "publisher": "American Sammy"
    },
    {
        "id": 664,
        "title": "Videomation",
        "release_date": "June 1991",
        "publisher": "THQ"
    },
    {
        "id": 665,
        "title": "Volleyball",
        "release_date": "March 1987",
        "publisher": "Nintendo"
    },
    {
        "id": 666,
        "title": "Wacky Races",
        "release_date": "May 1992",
        "publisher": "Atlus"
    },
    {
        "id": 667,
        "title": "Wall Street Kid",
        "release_date": "June 1990",
        "publisher": "SOFEL"
    },
    {
        "id": 668,
        "title": "Wario's Woods",
        "release_date": "December 10, 1994",
        "publisher": "Nintendo"
    },
    {
        "id": 669,
        "title": "Wayne Gretzky Hockey",
        "release_date": "January 1991",
        "publisher": "THQ"
    },
    {
        "id": 670,
        "title": "Wayne's World",
        "release_date": "November 1993",
        "publisher": "THQ"
    },
    {
        "id": 671,
        "title": "WCW Wrestling",
        "release_date": "April 1990",
        "publisher": "FCI"
    },
    {
        "id": 672,
        "title": "Werewolf: The Last Warrior",
        "release_date": "November 1990",
        "publisher": "Data East"
    },
    {
        "id": 673,
        "title": "Wheel of Fortune",
        "release_date": "September 1988",
        "publisher": "GameTek"
    },
    {
        "id": 674,
        "title": "Wheel of Fortune Family Edition",
        "release_date": "March 1990",
        "publisher": "GameTek"
    },
    {
        "id": 675,
        "title": "Wheel of Fortune: Featuring Vanna White",
        "release_date": "January 1992",
        "publisher": "GameTek"
    },
    {
        "id": 676,
        "title": "Wheel of Fortune Junior Edition",
        "release_date": "October 1989",
        "publisher": "GameTek"
    },
    {
        "id": 677,
        "title": "Where in Time Is Carmen Sandiego?",
        "release_date": "October 1991",
        "publisher": "Konami"
    },
    {
        "id": 678,
        "title": "Where's Waldo?",
        "release_date": "September 1991",
        "publisher": "THQ"
    },
    {
        "id": 679,
        "title": "Who Framed Roger Rabbit?",
        "release_date": "September 1989",
        "publisher": "LJN"
    },
    {
        "id": 680,
        "title": "Whomp 'Em",
        "release_date": "March 1991",
        "publisher": "Jaleco"
    },
    {
        "id": 681,
        "title": "Widget",
        "release_date": "November 1992",
        "publisher": "Atlus"
    },
    {
        "id": 682,
        "title": "Wild Gunman",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 683,
        "title": "Willow",
        "release_date": "December 1989",
        "publisher": "Capcom"
    },
    {
        "id": 684,
        "title": "Win, Lose, or Draw",
        "release_date": "March 1990",
        "publisher": "Hi Tech Expressions"
    },
    {
        "id": 685,
        "title": "Winter Games",
        "release_date": "September 1987",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 686,
        "title": "Wizardry: Proving Grounds of the Mad Overlord",
        "release_date": "July 1990",
        "publisher": "ASCII"
    },
    {
        "id": 687,
        "title": "Wizardry II: The Knight of Diamonds",
        "release_date": "April 1992",
        "publisher": "ASCII"
    },
    {
        "id": 688,
        "title": "Wizards & Warriors",
        "release_date": "December 1987",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 689,
        "title": "Wizards & Warriors III: Kuros: Visions of Power",
        "release_date": "March 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 690,
        "title": "Wolverine",
        "release_date": "October 1991",
        "publisher": "LJN"
    },
    {
        "id": 691,
        "title": "World Champ",
        "release_date": "April 1991",
        "publisher": "Romstar"
    },
    {
        "id": 692,
        "title": "World Class Track Meet",
        "release_date": "August 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 693,
        "title": "World Games",
        "release_date": "March 1989",
        "publisher": "Milton Bradley Company"
    },
    {
        "id": 694,
        "title": "Wrath of the Black Manta",
        "release_date": "April 1990",
        "publisher": "Taito"
    },
    {
        "id": 695,
        "title": "Wrecking Crew",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 696,
        "title": "Wurm: Journey to the Center of the Earth",
        "release_date": "November 1991",
        "publisher": "Asmik"
    },
    {
        "id": 697,
        "title": "WWF King of the Ring",
        "release_date": "November 1993",
        "publisher": "LJN"
    },
    {
        "id": 698,
        "title": "WWF WrestleMania",
        "release_date": "January 1989",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 699,
        "title": "WWF WrestleMania Challenge",
        "release_date": "November 1990",
        "publisher": "LJN"
    },
    {
        "id": 700,
        "title": "WWF WrestleMania: Steel Cage Challenge",
        "release_date": "September 1992",
        "publisher": "Acclaim Entertainment"
    },
    {
        "id": 701,
        "title": "Xenophobe",
        "release_date": "December 1988",
        "publisher": "Sunsoft"
    },
    {
        "id": 702,
        "title": "Xevious",
        "release_date": "September 1988",
        "publisher": "Bandai"
    },
    {
        "id": 703,
        "title": "Xexyz",
        "release_date": "April 1990",
        "publisher": "Hudson Soft"
    },
    {
        "id": 704,
        "title": "Yo! Noid",
        "release_date": "November 1990",
        "publisher": "Capcom"
    },
    {
        "id": 705,
        "title": "Yoshi",
        "release_date": "June 1, 1992",
        "publisher": "Nintendo"
    },
    {
        "id": 706,
        "title": "Yoshi's Cookie",
        "release_date": "April 1993",
        "publisher": "Nintendo"
    },
    {
        "id": 707,
        "title": "Young Indiana Jones Chronicles",
        "release_date": "January 1993",
        "publisher": "Jaleco"
    },
    {
        "id": 708,
        "title": "Zanac",
        "release_date": "October 1987",
        "publisher": "FCI"
    },
    {
        "id": 709,
        "title": "Zelda II: The Adventure of Link",
        "release_date": "December 1, 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 710,
        "title": "Zen the Intergalactic Ninja",
        "release_date": "March 1993",
        "publisher": "Konami"
    },
    {
        "id": 711,
        "title": "Zoda's Revenge: StarTropics II",
        "release_date": "March 1994",
        "publisher": "Nintendo"
    },
    {
        "id": 712,
        "title": "Zombie Nation",
        "release_date": "September 1991",
        "publisher": "Meldac"
    }
]
>>> response = requests.get('http://localhost:8080/game/710')
>>> print(json.dumps(response.json(), indent=4)
... )
{
    "id": 710,
    "title": "Zen the Intergalactic Ninja",
    "release_date": "March 1993",
    "publisher": "Konami"
}
>>> response = requests.get('http://localhost:8080/games/?title=mario')
>>> print(json.dumps(response.json(), indent=4))
[
    {
        "id": 190,
        "title": "Dr. Mario",
        "release_date": "October 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 380,
        "title": "Mario Bros.",
        "release_date": "June 1986",
        "publisher": "Nintendo"
    },
    {
        "id": 381,
        "title": "Mario Is Missing!",
        "release_date": "July 1993",
        "publisher": "Mindscape"
    },
    {
        "id": 382,
        "title": "Mario's Time Machine",
        "release_date": "June 1994",
        "publisher": "Mindscape"
    },
    {
        "id": 583,
        "title": "Super Mario Bros.",
        "release_date": "October 18, 1985",
        "publisher": "Nintendo"
    },
    {
        "id": 584,
        "title": "Super Mario Bros./Duck Hunt",
        "release_date": "November 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 585,
        "title": "Super Mario Bros./Duck Hunt/World Class Track Meet",
        "release_date": "December 1990",
        "publisher": "Nintendo"
    },
    {
        "id": 586,
        "title": "Super Mario Bros./Tetris/Nintendo World Cup",
        "release_date": "November 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 587,
        "title": "Super Mario Bros. 2",
        "release_date": "October 10, 1988",
        "publisher": "Nintendo"
    },
    {
        "id": 588,
        "title": "Super Mario Bros. 3",
        "release_date": "February 12, 1990",
        "publisher": "Nintendo"
    }
]
