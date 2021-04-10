from AbsBuilder import AbsBuilder

class MyBuilder(AbsBuilder):
    def get_case(self):
        self._computer.case = 'Open machine'

    def build_mainboard(self):
        self._computer.mainboard = 'Intel'
        self._computer.cup = 'Intel'
        self._computer.memory = 'Segate'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'WD'

    def install_video_card(self):
        self._computer.video_card = 'On board'