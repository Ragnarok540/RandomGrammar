import random
import re

class RandomGrammar:
    
    def __init__(self, ruleSet):
        self.grammar = {}
        self.regex = '<\w+>'
        for rule in ruleSet:
            self.addRule(rule, ruleSet[rule])
            
    def addRule(self, ruleName, ruleContent):
        if re.match(self.regex, ruleName) == None:
            raise Exception('Malformed rule name.')
        if type(ruleContent) is not list:
            raise Exception('Rule content must be a list.')
        if ruleName not in self.grammar:
            self.grammar[ruleName] = ruleContent
        else:
            raise Exception('Rule already exists.')
        
    def replace(self, ruleContent):
        result = ruleContent
        words = ruleContent.split()
        for word in words:
            if word in self.grammar:
                newValue = random.sample(self.grammar[word], 1)[0]
                result = result.replace(word, newValue, 1)
        return result
    
    def generate(self, startRule):
        if len(self.grammar) == 0:
            raise Exception('Empty grammar.')
        start = self.grammar.get(startRule)
        if start == None:
            raise Exception('Start rule not in grammar.')
        generatedString = startRule
        while generatedString.find('<') != -1:
            generatedString = self.replace(generatedString)
        return generatedString
