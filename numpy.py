import numpy as np

from ADRpy import atmospheres as at
from ADRpy import constraintanalysis as ca

designbrief = {'rwyelevation_m': 0, 'groundrun_m': 313,
                'stloadfactor': [1.5, 1.65], 'turnalt_m': [1000, 1075], 'turnspeed_ktas': [100, 110],
                'climbalt_m': 0, 'climbspeed_kias': 101, 'climbrate_fpm': 1398,
                'cruisealt_m': [2900, 3200], 'cruisespeed_ktas': [170, 175], 'cruisethrustfact': 1.0,
                'servceil_m': [6500, 6650], 'secclimbspd_kias': 92,
                'vstallclean_kcas': 69}
designdefinition = {'aspectratio': [10, 11], 'sweep_le_deg': 2, 'sweep_25_deg': 0, 'bpr': -1,
                    'wingarea_m2': 13.46, 'weight_n': 15000,
                    'weightfractions': {'turn': 1.0, 'climb': 1.0, 'cruise': 0.853, 'servceil': 1.0}}
designperformance = {'CDTO': 0.0414, 'CLTO': 0.59, 'CLmaxTO': 1.69, 'CLmaxclean': 1.45, 'mu_R': 0.02,
                     'CDminclean': [0.0254, 0.026], 'etaprop': {'take-off': 0.65, 'climb': 0.8,
                                                                'cruise': 0.85, 'turn': 0.85,
                                                                'servceil': 0.8}}

wingloadinglist_pa = np.arange(700, 2500, 5)
customlabelling = {'aspectratio': 'AR',
                   'sweep_le_deg': '$\Lambda_{LE}$',
                   'sweep_mt_deg': '$\Lambda_{MT}$'}

atm = at.Atmosphere()
concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, atm)

concept.propulsionsensitivity_monothetic(wingloading_pa=wingloadinglist_pa, y_var='p_hp', x_var='s_m2',
                                     customlabels=customlabelling)
#OUTPUT
ISA-10C density at 38000 feet (geopotential): 0.348049478999 kg/m^3
ISA-10C speed of sound at 38000 feet (geopotential): 288.1792251702055 m/s
