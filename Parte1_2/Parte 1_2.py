
# identificar os metabolitos externos

model.summary()


# identificar as reações do metabolito pretendido (lactato)

model.metabolites.get_by_id("M_lac__L_e")
model.metabolites.get_by_id("M_lac__D_e")



# pode calcular-se a produção máxima em wildtype mantendo a função objectivo de maximização do crescimento, usando FVA

simul.FVA(reactions=['R_EX_lac_L_e'])


#OU

# podemos alterar a função objectivo para maximização da produção de lactato e depois analisar o fluxo minimo e maximo usando FVA
# não está completo, são duas reações objectivo
simul.objective = 'R_EX_lac_L_e'
Simul.objective
simul.FVA(reactions=['R_EX_lac_L_e'])
