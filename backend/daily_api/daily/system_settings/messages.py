from enum import Enum, auto


class msg(Enum):
    _成功 = auto()
    _失敗 = auto()
    _ソンナidノニッポーハナイヨ = auto()

    def get_name(self):
        return self.name
