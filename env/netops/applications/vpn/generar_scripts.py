
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
    tipo = "FULL MESH" if vpn.conectividad_entre_moviles == "1" else "HUB & SPOKE"
    header = f'***** COMANDOS PARA UGW {ugw_type} - {tipo} *****\n\n'
    primera_parte = (
        'system-view\n'
        f'ip vpn-instance {vpn.vpn_instance}\n'
        f'description TRAMITE {vpn.tinco_movil}\n'
        f'route-distinguisher {vpn.route_distinguisher}:1\n\n'
    )
    bgp = 65412
    if ugw_type == "MUN":
        bgp = 65422
    if vpn.con_sitio_central:
        armado_bgp = (
            f'interface Eth-Trunks5.{vpn.route_distinguisher}\n'
            f'vlan-type dot1q {vpn.route_distinguisher}\n'
            f'description VPRNID 2{vpn.tinco_movil[1:]}0\n' # Elimino el primer caracter habitualmente P
            f'ip binding vpn-instance {vpn.vpn_instance}\n'
            f'ip address {vpn.ip_mag if ugw_type == "MAG" else vpn.ip_mun} 30\n\n'
            f'bgp {bgp}\n'
            f'ipv4-family vpn-instance {vpn.vpn_instance}\n'
            f'as-number 65500\n'
            f'import-route wlr\n'
            f'peer {vpn.peer_mag if ugw_type == "MAG" else vpn.peer_mun} as-number 7167\n'
            f'peer {vpn.peer_mag if ugw_type == "MAG" else vpn.peer_mun} timer keepalive 10 hold 30\n'
            'quit\n'
            'quit\n\n'
        )

    armado_acl = (
        'system-view\n'
        'service-view\n'
        f'acl {vpn.vpn_instance} match-order config\n'
        f'filter {vpn.vpn_instance}pool l34-protocol any ms-ip 0.0.0.0 255.255.255.255 server-ip {vpn.server_ip} {vpn.wildcard}\n'
        f'acl-node {vpn.acl_node} filter {vpn.vpn_instance}pool gate discard\n'
        f'acl-node-binding acl {vpn.vpn_instance} acl-node {vpn.acl_node} priority {vpn.prioridad}\n'
        'quit\n\n'
    )

    tercera_parte = (
        f'ip pool {vpn.nombre_pool_moviles} local ipv4\n'
        f'vpn-instance {vpn.vpn_instance}\n'
        f'section 0 {vpn.primer_ip_mag if ugw_type == "MAG" else vpn.primer_ip_mun} {vpn.ultima_ip_mag if ugw_type == "MAG" else vpn.ultima_ip_mun} static\n'
        'quit\n\n'
    )

    if vpn.con_sitio_central:
        contenido = (
            header +
            primera_parte +
            armado_bgp +
            armado_acl +
            tercera_parte
        )
    else:
        contenido = (
            header +
            tercera_parte
        )
    acl = ''
    if vpn.conectividad_entre_moviles == "2":
        acl = f'acl-binding direction down-in acl {vpn.nombre_acl}'

    cuarta_parte = (
        f'apn {vpn.apn}\n'
        f'vpn-instance {vpn.vpn_instance}\n'
        f'content-awareness disable\n'
        f'service-report switch flow global\n'
        f'access-mode transparent-non-authentication\n'
        f'framed-route-mode disable\n'
        f'address-allocate ipv4 local radius-prior disable ipv6 local radius-prior disable\n'
        f'address-support ipv4 enable ipv6 enable preference ipv4\n'
        f'address-allocate-preference enable\n'
        f'ppp-access authentication disable\n'
        f'ppp-access address-allocate local radius-prior disable\n'
        f'virtual-apn disable\n'
        f'address-inherit enable\n'
        f'apn-restriction disable\n'
        f'session-timeout enable length 1440\n'
        f'idle-timeout enable length 120 updatemsg disable\n'
        f'static-ip hlr-hss-provided enable conflict deactive route enable all\n'
        f'select-mode-check disable\n'
        f'lock disable\n'
        f'l2tp disable'
        f'{"dns ipv4 primary-ip" if vpn.dns_1 is not None else ""} {vpn.dns_1 if vpn.dns_1 is not None else ""}'
        f'{" secondary-ip" if vpn.dns_2 is not None else ""} {vpn.dns_2 if vpn.dns_1 is not None else ""}\n'
        f'dns priority ipv4 first radius second dhcp third local\n'
        f'ims-switch inherit\n'
        f'address-pool {vpn.nombre_pool_moviles}\n'
        f'volume-statistic-mode layer-all\n'
        f'aaa-apn-secondauth disable\n'
        f'apn-type-select perf service cg service aaaacct service aaaauth service ocs service pcrf service header-enrichment service\n'
        f'plmn serving-node-mapping enable\n'
        f'rat sgsn-sgw-mapping enable\n'
        f'multiple-service-mode radius\n'
        f'radius-disconnect enable\n'
        f'offline-charge-binding ggsn cc_0x0800_oct pgw cc_0x0800_oct sgw cc_0x0800_oct\n'
        f'radius acctctrl accounting-update enable\n'
        f'service-statistic-switch enable\n'
        f'{acl if vpn.conectividad_entre_moviles == "2" else ""}\n'
        f'quit\n'
        f'quit\n'
        f'\n'
    )    
    contenido += cuarta_parte
    return contenido
