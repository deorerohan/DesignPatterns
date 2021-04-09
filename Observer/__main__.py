from KPIs import KPIs
from CurrentKPIs import CurrentKPIs

kpis = KPIs()
current_kpis = CurrentKPIs(kpis)

kpis.set_kpis(25, 10, 5)
kpis.set_kpis(40, 20, 50)
kpis.set_kpis(34, 90, 2)

print('detach one of the observers')
kpis.detach(current_kpis)
kpis.set_kpis(75, 24, 55)
