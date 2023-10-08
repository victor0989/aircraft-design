import math
from ADRpy import constraintanalysis as co

designdef = {'aspectratio':8}
wingarea_m2 = 10
wingspan_m = math.sqrt(designdef['aspectratio'] * wingarea_m2)

for wingheight_m in [0.6, 0.8, 1.0]:

    designdef['wingheightratio'] = wingheight_m / wingspan_m

    aircraft = co.AircraftConcept({}, designdef, {}, {})

    print('h/b: ', designdef['wingheightratio'],
          'Phi: ', aircraft.wigfactor())

#OUTPUT
h/b:  0.06708203932499368  Phi:  0.5353159851301115
h/b:  0.08944271909999159  Phi:  0.6719160104986877
h/b:  0.11180339887498948  Phi:  0.761904761904762
