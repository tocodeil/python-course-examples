"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""

test1 = "LifeMustBeLivedAsPlay"
tesxt2 = "Life_must_be_lived_as_play"

def  toCamelCase(text):
	spaced = re.sub('_', ' ', text)
	UpperCase = re.sub(r'\s\b([a-z])', lambda m: m.group(1).upper(), spaced)
	withoutSpaces = re.sub(' ', '', UpperCase)
	return withoutSpaces
	
	
def to_underscore(text):
	spaced = re.sub(r'([A-Z])', lambda m: " " + m.group(1).lower(), text)
	UnderScored = re.sub(' ', '_', spaced)
	return UnderScored
