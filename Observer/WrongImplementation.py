class Data:
    def __init__(self, name='open', value=1) -> None:
        self.name = name
        self.value = value

KPI_Data = list()
KPI_Data.append(Data())
KPI_Data.append(Data('closed', 2))
KPI_Data.append(Data('new', 4))


# report on current KPI values
for kpi in KPI_Data:
    if kpi.name == 'open':
        print(f'Curret open tickets : {kpi.value}')
    elif kpi.name == 'new':
        print(f'New tickets in last hour : {kpi.value}')
    elif kpi.name == 'closed':
        print(f'Tickets closed in last hour : {kpi.value}')