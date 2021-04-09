import abc
from Interfaces import AbsObserver

class AbsSubject(metaclass = abc.ABCMeta):

    def __init__(self) -> None:
        self._observers = set()

    def attach(self, obs):
        if not isinstance(obs, AbsObserver.AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {obs}

    def detach(self, obs):
        self._observers -= {obs}

    def notify(self, value=None):
        for obs in self._observers:
            if value is None:
                obs.update()
            else:
                obs.update(value)

