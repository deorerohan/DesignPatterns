from Interfaces import AbsSubject

class KPIs(AbsSubject.AbsSubject):
    def __init__(self) -> None:
        super().__init__()
        self._open_tickets = -1
        self._closed_tickets = -1
        self._new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets
    
    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open, closed, new):
        self._open_tickets = open
        self._closed_tickets = closed
        self._new_tickets = new
        self.notify()

    