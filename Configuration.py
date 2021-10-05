class Configuration:
    def __init__(self, attributes=None):
        self.databases_path = ''
        self.local_xml_path = ''
        self.log2_5_path = ''
        self.log3_0_path = ''
        self.database_nfe_path = ''
        self.version_path = ''
        self.address_path = ''
        self.firebird2_5_path = ''
        self.firebird3_0_path = ''
        self.port_firebird2_5 = ''
        self.port_firebird3_0 = ''
        self.set_attributes(attributes)

    def set_attributes(self, attributes):
        if attributes is None:
            return

        keys = dict(attributes).keys()
        for key in keys:
            self.__setattr__(str(key), attributes[key])

    def get_attributes(self):
        return self.__dict__
