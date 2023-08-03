def make_snippet(string):
    if not isinstance(string, str):
        raise Exception("Please enter a string") 
    
    words = string.split()
    snippet = ' '.join(words[:5])
    
    return snippet + "..." if len(words) > 5 else snippet