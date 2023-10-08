#Given a load factor, an altitude (in a given atmosphere) and a true 
#airspeed, as well as a set of basic geometrical and aerodynamic performance parameters, 
#compute the necessary T/W ratio to hold that load factor in the turn.
from ADRpy import atmospheres as at
from ADRpy import constraintanalysis as ca
from ADRpy import unitconversions as co

designbrief = {'stloadfactor': 2, 'turnalt_m': co.feet2m(10000),
            'turnspeed_ktas': 140}

etap = {'turn': 0.85}

designperformance = {'CLmaxclean': 1.45, 'CDminclean':0.02541,
                    'etaprop': etap}

designdef = {'aspectratio': 10.12, 'sweep_le_deg': 2,
            'sweep_mt_deg': 0, 'bpr': -1}

designatm = at.Atmosphere()

concept = ca.AircraftConcept(designbrief, designdef,
designperformance, designatm)

wingloadinglist_pa = [1250, 1500, 1750]

twratio, clrequired, feasibletw = concept.twrequired_trn(wingloadinglist_pa)

print('T/W:               ', twratio)
print('Only feasible T/Ws:', feasibletw)
print('CL required:       ', clrequired)
print('CLmax clean:       ', designperformance['CLmaxclean'])
