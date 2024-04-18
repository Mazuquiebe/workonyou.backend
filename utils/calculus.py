import decimal


class NutriCalculus:
    
    def __init__(self, weight_kg:float, height_cm:int, age_yr:int, sex:str):

        self.weight = float(weight_kg)
        self.height = float(height_cm)
        self.age    = int(age_yr)
        self.sex    = sex

        self.basal_metabolism = 0

        self.protein = 0
        self.carb    = 0

        self.saturated_fat   = 0
        self.unsaturated_fat = 0

        self.water = 2
        
        self.ml_water_per_kg = 0.035
        self.protein_per_kg  = 1.7


    def calculate_formule_for_male(self):
        """
        Harris Benedict formule 
           66    + ( 13.7   * self.weight) + ( 5.0   * self.height) -  ( 6.8    * self.age)
        |CONST_A|  |CONST_B|                 |CONST_C|                |CONST_D| 
        |        BLOCK_A                 | + |     BLOCK_B        | - |     BLOCK_B       | 
        """
        CONST_A = 66
        CONST_B = 13.7
        CONST_C = 5.0
        CONST_D = 6.8
 
        BLOCK_A = CONST_A + (CONST_B * self.weight)
        BLOCK_B = CONST_C * self.height
        BLOCK_C = CONST_D * self.age
         
        EQUATION = BLOCK_A + BLOCK_B - BLOCK_C
        return EQUATION
        # return  66 + (13.7 * float(self.weight)) + (5.0 * int(self.height)) - (6.8 * int(self.age))


    def calculate_formule_for_female(self):
        """
        Harris Benedict formule 
        665 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age) 
        |        BLOCK_A        | + |     BLOCK_B     | - |     BLOCK_B    | 
        """
        CONST_A = 665
        CONST_B = 9.6 
        CONST_C = 1.8
        CONST_D = 4.7

        BLOCK_A = CONST_A + (CONST_B * self.weight)
        BLOCK_B = CONST_C * self.height
        BLOCK_C = CONST_D * self.age
        
        EQUATION = BLOCK_A + BLOCK_B - BLOCK_C

        return EQUATION


    def calculate_basal_metabolism(self):

        if  self.sex == "MALE":
            self.basal_metabolism = self.calculate_formule_for_male()

        elif self.sex == "FEMALE":
            self.basal_metabolism = self.calculate_formule_for_female()
        
        self.basal_metabolism = round(self.basal_metabolism,2)

        data = {
            'basal_metabolism': self.basal_metabolism
        }

        return data


    def calculate_imc(self):
        # O índice de massa corporal (IMC) foi calculado com as medidas de peso e altura, 
        # através da seguinte fórmula: IMC = peso (kg) / altura2 (m); 
        # os pontos de corte adotados foram: baixo peso (IMC < 18,5), 
        # eutrofia (IMC = 18,5 a 24,9), sobrepeso (IMC = 25 a 29,9) e obesidade (IMC ≥ 30)10.
        height_in_meter = self.height/100
        imc = self.weight / (height_in_meter)**2
        return imc
        ...


    def calculate_water(self, ml_water_per_kg=None):

        if ml_water_per_kg:
            self.ml_water_per_kg = float(ml_water_per_kg)

        self.water = self.weight * self.ml_water_per_kg
        self.water = round(self.water,1)

        return self.water
    

# Segundo as Diretrizes da Sociedade Brasileira de 
# Medicina do Exercício e do Esporte6, 
# a ingestão adequada de proteínas para atletas de força 
# seria de 1,6 a 1,7 gramas por quilo de peso corporal por dia. 

    def calculate_protein(self, protein_per_kg:float=None)-> dict:

        if  protein_per_kg:
            self.protein_per_kg = float(protein_per_kg)

        consumed_protein = self.weight * self.protein_per_kg
        kcal_value = consumed_protein * 4

        self.protein = round(consumed_protein,1)

        data = {
            'protein': consumed_protein,
            'kcal_value': kcal_value      
        }

        return data


    def calculate_fat(self)-> dict:
        self.basal_metabolism = self.calculate_basal_metabolism()['basal_metabolism']
        saturated_fat_kcal    = self.basal_metabolism * 10/100
        unsaturated_fat_kcal  = self.basal_metabolism * 20/100
        sat_fat_consumed      = saturated_fat_kcal / 4
        unsat_fat_consumed    = unsaturated_fat_kcal / 4
        
        self.saturated_fat   = round(sat_fat_consumed, 2)
        self.unsaturated_fat = round(unsat_fat_consumed, 2)

        total_fat_kcal     = saturated_fat_kcal + unsaturated_fat_kcal
        total_fat_consumed = sat_fat_consumed + unsat_fat_consumed
        
        data = {
            'saturated_fat': sat_fat_consumed,
            'saturated_fat_kcal': saturated_fat_kcal,
            'unsaturated_fat': unsat_fat_consumed,
            'unsaturated_fat_kcal': unsaturated_fat_kcal,
            'total_kcal': total_fat_kcal,
            'total_fat': total_fat_consumed,
        }

        return data


    def calculate_carb(self)-> dict:
        
        self.calculate_basal_metabolism()['basal_metabolism']
        
        protein_values = self.calculate_protein()
        fat_values     = self.calculate_fat()
        fat_ptn_kcal   = protein_values['kcal_value'] + fat_values['total_kcal']

        carb_kcal      = self.basal_metabolism - fat_ptn_kcal
        consumed_carb  = carb_kcal / 4 

        self.carb = round(consumed_carb, 1)

        data = {
            'carb': consumed_carb,
            'kcal_value': carb_kcal
        }

        return data
        

    def calculate_macro(self):

        self.calculate_basal_metabolism()
        self.calculate_fat()
        self.calculate_carb()
        self.calculate_protein()
        self.calculate_water()

        data = {
            'suggested_protein':   self.protein,
            'suggested_carb':      self.carb,
            'suggested_sat_fat':   self.saturated_fat,
            'suggested_unsat_fat': self.unsaturated_fat,
            'suggested_water':     self.water,
            'basal_metabolism':    self.basal_metabolism,
        }

        return data


    # def suggestions(self):

        # reccomended_nutri = self.calculate_macro()

        # about_basal_metabolism = f"""
        #     {self.username} segundo nossos calculos internos 
        #     sua Taxa de Metabolismo Basal é de aproximadamente 
        #     {reccomended_nutri['basal_metabolism']}.
        #     Isso significa que seu organismo consome esse valor 
        #     em kcal estando em repouso e por isso é muito importante 
        #     que se você pratica alguma atividade física 
        #     leve em consideração o consumo de energia em kcal dessa atividade.
        # """

        # about_protein = f"""
        #     Segundo as Diretrizes da Sociedade Brasileira de 
        #     Medicina do Exercício e do Esporte, 
        #     a ingestão adequada de proteínas para atletas de força 
        #     seria de 1,6 a 1,7 gramas por kg de peso corporal por dia.
        #     Levamos em consideração que você já 
        #     pratica algum esporte para hipertrofia e manutenção 
        #     de massa muscular, além da perda de gordura
        #     por isso a quantidade de proteína por peso corporal que 
        #     foi utilizada para calcular esse valor foi de 
        #     {self.protein_per_bodyweight} g de proteína por kg 
        #     de peso corporal. Então a quantidade de proteína 
        #     sugerida para seu consumo diario é de aproximadamente 
        #     {reccomended_nutri['protein']} gramas e esse valor deve 
        #     ser divido entre suas refeições.
        # """

        # about_carb = f"""
        #     Carboidrato é um macronutriente muito importante 
        #     para o fornecimento de energia ao nosso corpo por 
        #     isso é de grande importância que tenhamos o consumo 
        #     regulado desse macronutriente, pois acredite ou não 
        #     o seu consumo exacerbado é que leva ao acúmulo 
        #     de sobrepeso. Quando você passa por longos períodos 
        #     sem se alimentar e quando se alimenta ingere mais 
        #     energia do que o suficiente para o seu organismo 
        #     funcionar o seu corpo armazena essa energia em 
        #     um "estoque de gordura" para que da proxima vez que 
        #     você passar por um longo período sem se alimentar 
        #     essa gordura seja quebrada e forneça energia para o 
        #     corpo. Então levando em conta os valores calóricos 
        #     que seram consumidos em gramas de proteínas e gorduras 
        #     o valor em carboidratos deverá consumir é de 
        #     {reccomended_nutri['carb']} gramas.
        # """
        # about_lipids = f"""
        #     Os Lipídeos conhecidos popularmente como gordura 
        #     também são fundamentais para a boa nutrição do 
        #     ser humano. São fonte de energia para o corpo 
        #     assim como o carboidrato mas também exercem um papel 
        #     fundamental na s síntese de hormônios do seu organismo.  
        #     Porém devem ser selecionados os tipos de gordura 
        #     saturadas e insaturadas que segundo a maior parte 
        #     dos estudos sobre nutrição apontam que 30% da 
        #     alimentação diária deve ser coonsumida 
        #     em forma de gordura. Onde 20% deve ser de gordura 
        #     insaturada e 10% de gordura saturada.
        #     Então de acordo com os valores que você nos forneceu
        #     tivemos como resultado de todo o processo de calculos complexos 
        #     o valor sugerido de gorduras insaturadas de {reccomended_nutri['unsat_fat']} gramas
        #     e de gordura saturada {reccomended_nutri['sat_fat']} gramas.
        # """
        
        # message = {
        #     'about_basal_metabolism': about_basal_metabolism,
        #     'about_lipids': about_lipids,
        #     'about_carb': about_carb,
        #     'about_protein': about_protein,
        # }

        # return message





class FoodCalculus:

    def __init__(self, kcal, protein, carb, unsat_fat, sat_fat, quantity_g):
        
        self.kcal = float(kcal)
        
        self.protein = float(protein)
        self.carb    = float(carb)

        self.unsat_fat = float(unsat_fat)
        self.sat_fat   = float(sat_fat)
        
        self.quantity_g = float(quantity_g)

    
    def divide(self, dividend, divider):
        return dividend / divider


    def multiply(self, multiplied, multiplier):
        return multiplied * multiplier
    
    
    def calculate_total_nutri(self, food_grams):

        protein_per_g   = self.divide(self.protein, self.quantity_g)
        carb_per_g      = self.divide(self.carb, self.quantity_g)
        sat_fat_per_g   = self.divide(self.sat_fat, self.quantity_g)
        unsat_fat_per_g = self.divide(self.unsat_fat, self.quantity_g)
        kcal_per_g      = self.divide(self.kcal, self.quantity_g)

        total_protein_g   = protein_per_g * food_grams
        total_carb_g      = carb_per_g * food_grams
        total_sat_fat_g   = sat_fat_per_g * food_grams
        total_unsat_fat_g = unsat_fat_per_g * food_grams
        total_kcal        = kcal_per_g * food_grams


 

