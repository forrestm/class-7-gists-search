from gist_search.utils import get_gists
# from utils import get_gists

def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    results = []
    
    gists = get_gists(username)
    
    for gist in gists:
        if description and description.lower() not in gist['description'].lower():
            continue
            
        if file_name:
            found = False
            
            for fname, fbody in gist['files'].items():
                if file_name in fname:
                    found = True
                    break
            if not found:
                continue
            
        results.append(gist)
        
    return results