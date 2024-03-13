class TypeChart:
      def __init__(self,type,advantage,weakness):
          self.type= type
          self.advantage=advantage
          self.weakness=weakness
                  
      def analysis(self,pokémon):
         	return f"Your{pokémon} is weak against{self.weakness}"\
            and f"Your {pokémon} is strong against{self.advantage}"
#the whole ideia was to compare e define the advantagens and weakness    	    

fire_type_chart=TypeChart('fire','ice,grass,bug,steel','water,ground,rock')
water_type_chart=TypeChart('water','ground,fire,rock','grass,electric')
grass_type_chart=TypeChart('grass','ground,rock,water','fire,flying,ice,bug,poison')
normal_type_chart=TypeChart('normal','none','fighting')
flying_type_chart=TypeChart('flying','grass,fighting','rock,electric,ice')
electric_type_chart=TypeChart('electric','water,flying','ground')
fighting_type_chart=TypeChart('fighting','normal','psychic,flying')
ground_type_chart=TypeChart('ground','rock,fire,steel,poison','water,grass,ice')
rock_type_chart=TypeChart('rock','flying,fire,bug','water,grass,ground,fighting,steel')
poison_type_chart=TypeChart('poison','grass','ground,psychic')
psychic_type_chart=TypeChart('psychic','poison,fighting','bug,ghost')
ghost_type_chart=TypeChart('ghost','ghost,psychic','ghost')
bug_type_chart=TypeChart('bug','grass,psychic','fire,flying,rock')
ice_type_flying=TypeChart('ice','grass,flying','fire,rock,steel,fighting')
steel_type_chart=TypeChart('steel','ice,rock','fire,ground,fighting')
dragon_type_chart=TypeChart('dragon','dragon','dragon,ice')

#this is based in Pokémon Red,Blue and Yellow, aswell in Pokémon FireRed and LeafGreen. So, does not include nor dark and fairy types. 

