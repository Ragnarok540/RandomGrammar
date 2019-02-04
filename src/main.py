from rgrammar import RandomGrammar 

def main():
    
    rules = { '<start>'    : ['<template>'],
              '<template>' : ['<det> <noun> <verb> <adj>', '<det> <adj> <noun>'],
              '<det>'      : ['A', 'The', 'This', 'That'],
              '<verb>'     : ['is', 'was'],
              '<noun>'     : ['house', 'cat', 'fish', 'girl', 'boat'],
              '<adj>'      : ['red', 'tiny', 'big', 'cute', 'pretty']
             }
    
    gr = RandomGrammar(rules)

    print(gr.generate('<start>'))
    print(gr.generate('<start>'))
    print(gr.generate('<start>'))
    print(gr.generate('<start>'))
    print(gr.generate('<start>'))
    print(gr.generate('<start>'))
    print(gr.generate('<start>'))
    print(gr.generate('<start>'))

if __name__ == '__main__':
    
    main()
