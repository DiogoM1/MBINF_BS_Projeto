# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:59:15 2020

@author: Mariana
"""

from mewpy.simulation import get_simulator
import cobra
from cobamp.wrappers import KShortestEFMEnumeratorWrapper
# import escher

# Exercício 1

model_path = "iML1515.xml"
model = cobra.io.read_sbml_model(model_path)
print(model.summary())

envcond = {'EX_glc__D_e': (-15.0, 1000), 'EX_o2_e': (0, 1000)}
simul = get_simulator(model, envcond=envcond)
result = simul.simulate(method='FBA')
print(result)

model_path1 = "iML1515.xml"
model1 = cobra.io.read_sbml_model(model_path1)
print(model1.summary())

envcond = {'EX_glc__D_e': (-15.0, 1000), 'EX_o2_e': (0, 1000)}
simul1 = get_simulator(model1, envcond=envcond)
result1 = simul1.simulate(method='FBA')
print(result1)


# Exercício 3


model_path = "iML1515.xml"
model = cobra.io.read_sbml_model(model_path)

biomass_c = cobra.Metabolite(compartment='c', id='biomass_c', name='Biomass')
biomass_production = cobra.Reaction(id='EX_biomass_e', name='Biomass production', lower_bound=0, upper_bound=1000)

model_biomass = model.copy()
model_biomass.add_metabolites([biomass_c])

model_biomass.reactions.BIOMASS_Ec_iML1515_core_75p37M.add_metabolites({biomass_c: 1})
biomass_production.add_metabolites({biomass_c: -1})

ksefm = KShortestEFMEnumeratorWrapper(
    model=model_biomass,
    non_consumed=['o2_e'],
    consumed=['glc__D_e'],
    produced=['biomass_c', 'lac__D_e', 'lac__L_e'],
    non_produced=[],
    algorithm_type=KShortestEFMEnumeratorWrapper.ALGORITHM_TYPE_POPULATE,
    stop_criteria=100,
    solver='CPLEX'
)

enumerator = ksefm.get_enumerator()

efm_list = []

while len(efm_list) == 0:
    efm_list += next(enumerator)

print(len(efm_list))
print(*efm_list)

# escher_builder = escher.Builder(
#    map_name='e_coli_core.Core metabolism',
#    hide_secondary_metabolites=True,
#    reaction_data=efm_list[0]
# )
# escher_builder.display_in_notebook(js_source='local')
