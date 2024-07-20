""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api


reg_params = {
        'Title': "",
        'Body': [],
    }

def main():
    ###poke_name = get_pokemon_name()
    poke_name="rockruff"
    poke_info = poke_api.get_pokemon_info(poke_name)
    paste_title =poke_name.capitalize()
        
    if poke_info is not None:
        reg_params['Title']=paste_title
        paste_body = get_paste_data(poke_info)
        print(f"Abilities for:{paste_title}")
        for i in range(len(paste_body)+1):
               print(f"- {paste_body['Body'][i]}")
   
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        print(paste_url)


def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    # TODO: Function body
    
    if len(sys.argv)!= 2:
           print("ERROR: Name for Pokemon not provided.")
           sys.exit('Script executon aborted')
    else:    
           name_pokem=sys.argv[1]
           return(name_pokem)
    return(name_pokem)   


def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # TODO: Build the paste title
    # TODO: Build the paste body text

    for pokereg in pokemon_info['abilities']:
            reg_params['Body'].append(pokereg['ability']['name'])
  
    #return the paste data
    return (reg_params)  

if __name__ == '__main__':
    main()