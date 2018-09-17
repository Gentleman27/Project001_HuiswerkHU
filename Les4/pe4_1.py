cijferICOR = 7
cijferPROG = 8
cijferCSN = 6

gemiddelde = (cijferCSN + cijferICOR + cijferPROG)/3
beloning = float(cijferCSN + cijferICOR + cijferPROG) * 30
overzicht = "Mijn gemiddelde is " + str(gemiddelde) + " en al mijn cijfers samen leveren €" + str(beloning) + " op!"

print(overzicht)