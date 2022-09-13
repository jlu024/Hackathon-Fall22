CONFIG_DATA = {
    'Regular-1': {
            'boardSize': [8, 8],
            'candyFreq': {
                'item01': 2,
                'item02': 1,
                'item03': 2,
                'item04': 3,
                'item05': 1,
                'item06': 1,
            },
            'completionCriteria': 20,
            'turns': 15,
    },
    'Regular-2': {
        'boardSize': [9, 9],
                    'candyFreq': {
                        'item01': 2,
                        'item02': 1,
                        'item03': 2,
                        'item04': 3,
                        'item05': 1,
                        'item06': 1,
                    },
                    'completionCriteria': 20,
                    'turns': 10,
    },
    'Fruit-1': {
                'boardSize': [5, 5],
                'candyFreq': {
                    'red': 1,
                    'yellow': 1,
                    'green': 3,
                    'blue': 5
                },
                'completionCriteria': {
                    'red': 0,
                    'yellow': 0,
                    'green': 0,
                    'blue': 0,
                    'fruit': 2,
                },
                'turns': 20,
        }
}

GAME_MODE = 1
SOUND_VOLUME = 0.1
SOUND_MUTED = False