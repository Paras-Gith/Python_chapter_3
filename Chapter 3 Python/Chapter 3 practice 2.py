letter = ''' Dear <|name|>,
            You are selected! 
            <|Date|>'''

print(letter.replace("<|name|>", "Paras Nainwal").replace("<|Date|>", "27 may 2025"))