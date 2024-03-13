import pokédex
import type_chart
#the first one is the pokedex up 151
#the second is the table of advantage and weakness

def pokémon():
    pokémon_procurado = input('Nome do pokémon: ')
    
    if pokémon_procurado in pokédex:
        print('Pokémon encontrado!')
        return pokédex[pokémon_procurado]
    else:
        return None
        
        type_pkmn=pokédex[pokémon_procurado[0][1]]
        for type_pkmn in type_chart_dict:
                	return type_chart_dict[type_pokémon].analysis(pokémon_procurado)
                	
pokémon ()
#insert a name of pokémon and will return it's advantagens and weakness'