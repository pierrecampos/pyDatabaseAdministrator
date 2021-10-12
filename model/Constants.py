class Constants:
    FIREBIRD2_5 = 0
    FIREBIRD3_0 = 1

    @classmethod
    def get_version_string(cls, version):
        if version == cls.FIREBIRD2_5:
            return "Firebird 2.5"
        elif version == cls.FIREBIRD3_0:
            return "Firebird 3.0"
        else:
            return "-"
