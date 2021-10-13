class SampleFiles:
    #Alias
    BASE_CONF_ALIAS = '@path_database@'
    NFE_ALIAS = '@path_nfe@'
    LOG_ALIAS = '@path_log@'
    VERSION_ALIAS = '@path_versao@'
    ADDRESS_ALIAS = '@path_endereco@'

    LOCAL_XML_ALIAS = '@port@'

    #Samples
    BASE_CONF = 'mentor=' + BASE_CONF_ALIAS + '\MENTOR.FDB \nnfe='+ NFE_ALIAS +' \nlog='+ LOG_ALIAS +' \nversao=' + VERSION_ALIAS + '\nendereco=' + ADDRESS_ALIAS
    LOCAL_XML = '<?xml version="1.0" encoding="UTF-8"?><mentorLocal><url.database>jdbc:firebirdsql://host:porta/mentor</url.database><host>localhost</host><porta>' + LOCAL_XML_ALIAS + '</porta><url.database.cep>jdbc:firebirdsql://host:porta/endereco</url.database.cep><url.database.log>jdbc:firebirdsql://host:porta/log</url.database.log><url.database.nfe>jdbc:firebirdsql://host:porta/nfe</url.database.nfe><versao.codigo>2021010200</versao.codigo><versao.sub.codigo>23</versao.sub.codigo><url.database.communicator>jdbc:firebirdsql://host:porta/communicator</url.database.communicator><url.database.versao>jdbc:firebirdsql://host:porta/versao</url.database.versao><url.host.communicador>localhost</url.host.communicador><url.database.binarydata>jdbc:firebirdsql://host:porta/binarydata?lc_ctype=ISO8859_1</url.database.binarydata><tipo.sistema>1</tipo.sistema><codigo.sistema>7</codigo.sistema><xml.patch.update /></mentorLocal>'