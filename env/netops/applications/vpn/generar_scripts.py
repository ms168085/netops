
# Funcion para generar script para el HLR
def generar_script_hlr(vpn):
    contenido = f'***** COMANDOS PARA EL HLR *****\n\nHGAPI:APN1="{vpn.apn}", APNID={vpn.apn_id};'
    return contenido

# Funcion para generar script para el vUSN
def generar_script_vusn(vpn):
    contenido = (
        '***** COMANDOS PARA LOS vUSN *****\n\n'
        '***** Tecnología 2G/3G *****\n\n'
        f'ADD DNSN: FQDN="{vpn.apn.upper()}.MNC001.MCC748.GPRS", HSINDEX=1011, ENTITY=GGSN, INTYPE=Gn, UEUSGTYPEPLCY=NO, PRIORITY=10, WEIGHT=36, DESC="NULL";\n'
        f'ADD DNSN: FQDN="{vpn.apn.upper()}.MNC001.MCC748.GPRS", HSINDEX=1012, ENTITY=GGSN, INTYPE=Gn, UEUSGTYPEPLCY=NO, PRIORITY=10, WEIGHT=36, DESC="NULL";\n\n'
        '***** Tecnología LTE *****\n\n'
        f'ADD DNSN: FQDN="{vpn.apn.upper()}.APN.EPC.MNC001.MCC748.3GPPNETWORK.ORG", HSINDEX=1011, ENTITY=PGW, INTYPE=S5, UEUSGTYPEPLCY=NO, PRIRITY=10, WEIGHT=36, DESC="NULL";\n'
        f'ADD DNSN: FQDN="{vpn.apn.upper()}.APN.EPC.MNC001.MCC748.3GPPNETWORK.ORG", HSINDEX=1012, ENTITY=PGW, INTYPE=S5, UEUSGTYPEPLCY=NO, PRIRITY=10, WEIGHT=36, DESC="NULL";\n'
    )
    return contenido


# Funcion para generar el script para los HSS MAG y MUN
def generar_script_hss(vpn, hss_type):
    header = f'***** COMANDOS PARA HSS {hss_type} *****\n\n'
    managed_element = f'ManagedElement=HSSFEM{hss_type}01\n'
        
    contenido = (
        header +
        managed_element +
        'HSS-Function=HSS_FUNCTION\n'
        'HSS-EsmApplication=HSS_ESM\n'
        'HSS-EsmConfigurationContaniner=HSS-EsmConfigurationContainer\n'
        'HSS-EsmApnContainer=HSS-EsmApnContainer\n'
        'configure\n'
        f'HSS-EsmApn={vpn.apn_id}\n'
        f'hss-EsmApnName={vpn.apn}\n'
        'commit\n'
        'up\n'
        f'show HSS-EsmApn={vpn.apn_id}\n'
        + managed_element +
        'HSS-Function=HSS_FUNCTION\n'
        'HSS-EsmApplication=HSS_ESM\n'
        'HSS-EsmConfigurationContainer=HSS-EsmConfigurationContainer\n'
        'HSS-EsmApnConfigurationContainer=HSS-EsmApnConfigurationContainer\n'
        'configure\n'
        f'HSS-EsmApnConfig={vpn.apn_id}\n'
        'hss-EsmAmbrMaxDl=157286400\n'
        'hss-EsmAmbrMaxUl=52428800\n'
        f'hss-EsmApnId={vpn.apn_id}\n'
        'hss-EsmQosProfileArp=13\n'
        'hss-EsmQosProfileQci=9\n'
        'commit\n'
        'up\n'
        f'show HSS-EsmApnConfig={vpn.apn_id}\n'
        + managed_element +
        'HSS-Function=HSS_FUNCTION\n'
        'HSS-EsmApplication=HSS_ESM\n'
        'HSS-EsmConfigurationContainer=HSS-EsmConfigurationContainer\n'
        'HSS-EsmProfileContainer=HSS-EsmProfileContainer\n'
        'configure\n'
        f'HSS-EsmProfile={vpn.apn}\n'
        'hss-EsmAmbrMaxDl=157286400\n'
        'hss-EsmAmbrMaxUl=52428800\n'
        f'hss-EsmDefaultContextId={vpn.apn_id}\n'
        f'hss-EsmContextIdList={vpn.apn_id}\n'
        'commit\n'
        'up\n'
        f'show HSS-EsmProfile={vpn.apn}\n'
    )
    return contenido

# Función para generar script para los UGW
def generar_script_ugw(vpn, ugw_type):
    header = f'***** COMANDOS PARA UGW {ugw_type} *****\n\n'
    primer_parte = (
        'system-view\n'
        f'ip vpn-instance {vpn.vpn_instance}\n'
        f'description TRAMITE {vpn.tinco_movil}\n'
        f'route-distinguisher {vpn.route_distinguisher}:1\n\n'
        f'interface Eth-Trunks5.{vpn.route_distinguisher}\n'
        f'vlan-type dot1q {vpn.route_distinguisher}\n'
        f'description VPRNID 2 {vpn.tinco_movil[1:]}\n' # Elimino el primer caracter habitualmente P
        f'ip binding vpn-instance {vpn.vpn_instance}\n'
        f'ip address {vpn.primer_ip_mag if ugw_type == "MAG" else vpn.primer_ip_mun} 30\n'
    )

    contenido = (
        header + 
        primer_parte
    )
    return contenido
