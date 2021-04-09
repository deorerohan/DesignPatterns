from Interfaces import AbsObserver

class CurrentKPIs(AbsObserver.AbsObserver):
    def __init__(self, kpis) -> None:
        super().__init__()
        self._open_tickets = -1
        self._closed_tickets = -1
        self._new_tickets = -1
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self._open_tickets = self._kpis._open_tickets
        self._closed_tickets = self._kpis._closed_tickets
        self._new_tickets = self._kpis._new_tickets
        self.display()

    def display(self):
        print(f'Open KPIs : {self._open_tickets}')
        print(f'Closed KPIs : {self._closed_tickets}')
        print(f'New KPIs : {self._new_tickets}')
        print('***\n')