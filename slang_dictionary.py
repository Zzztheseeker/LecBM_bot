import pickle

slang_dictionary = {
    'матан': 'многомерный анализ',
    'линал': 'линейная алгебра',
    'определение': 'опр-',
    'подпространства': 'подр-',
    'отображение': 'отбр-',
    'городос': 'городецкий',
    'сакбой': 'сакбаев'
    }

with open('slang_dictionary.pkl', 'wb') as f:
    pickle.dump(slang_dictionary, f)
