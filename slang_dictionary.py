import pickle

slang_dictionary = {
    'многомерный анализ': 'матан',
    'линейная алгебра': 'линал',
    'опр-': 'определение',
    'подр-': 'подпространства',
    'отбр-': 'отображение'
    }

with open('slang_dictionary.pkl', 'wb') as f:
    pickle.dump(slang_dictionary, f)
