
# Funcion para generar script para el HSS MAG y MUN
# item = objeto lanzamiento
def generar_script_hss(item, nodo):
    hss = "MAG" if nodo == "MAG" else "MUN"

    # Verificar cantidad de digitos MNC
    dato_mnc = item.mnc
    if len(dato_mnc) == 1:
        dato_mnc = f'00{dato_mnc}'
    elif len(dato_mnc) == 2:
        dato_mnc = f'0{dato_mnc}'
    
    carrier = ''
    if item.carrier == "1":
        # Syniverse
        carrier = f'DIA-CFG-Drt=epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org:HSS_ESM:FALSE\n'
    else:
        # Comfone
        carrier = f'DIA-CFG-Drt=epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org.key2roam.comfone.com:HSS_ESM:FALSE\n'
    contenido = (
        f'***** COMANDOS PARA HSS {hss} *****\n\n'
        f'ManagedElement=HSSFE{hss}01\n'
        f'HSS-Function=HSS_FUNCTION\n'
        f'HSS-EsmApplication=HSS_ESM\n'
        f'HSS-EsmConfigurationContainer=HSS-EsmConfigurationContainer\n'
        f'HSS-EsmPlmnContainer=HSS-EsmPlmnContainer\n'
        f'configure\n'
        f'HSS-EsmPlmn={item.mcc}{item.mnc}\n'
        f'up\n'
        f'commit\n'
        f'up\n'
        f'up\n'
        f'up\n\n'
        f'ManagedElement=HSSFE{hss}01\n'
        f'HSS-Function=HSS-Function\n'
        f'DIA-CFG-Application=DIA\n'
        f'DIA-CFG-StackContainer=HSS_ESM\n'
        f'DIA-CFG-RoutingContainer=HSS_ESM\n'
        f'configure\n'
        f'{carrier}'
        f'DIA-CFG-AuthReqContainer=authReqContainerName\n'
        f'DIA-CFG-AppRouting=10415:16777251\n'
        f'action="4"\n'
        f'nodeIds="0:dra02.cia.epc.mnc001.mcc748.3gppnetwork.org#HSS_ESM"\n'
        f'nodeIds="1:dra02.mun.epc.mnc001.mcc748.3gppnetwork.org#HSS_ESM\n'
        f'commit\n'
        f'up\n'
        f'up\n'
        f'up\n'
        f'up\n'
    )
    return contenido

def generar_script_ugw(item):
    # Verificar cantidad de digitos MNC
    dato_mnc = item.mnc
    if len(dato_mnc) == 1:
        dato_mnc = f'00{dato_mnc}'
    elif len(dato_mnc) == 2:
        dato_mnc = f'0{dato_mnc}'

    real_name = ''
    dmrt = ''
    if item.carrier == "1":
        # Syniverse
        real_name = f'ADD IMSIHSS:IMSIPRE="{item.mcc}{item.mnc},HSSRLM="epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org",MNNAME="{item.operadora}_{item.pais}";\n\n'
        dmrt = (
            f'ADD DMRT:ROUTEIDX={item.dmrt},ISDEFAULT=NO,RSELMODE=SELMODE_ROUND_ROBIN,REALNAME="epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org",PEERIDX=6,ROUTENAM="{item.operadora}_{item.pais},DESC="DRA CIA";\n'
            f'ADD DMRT:ROUTEIDX={item.dmrt},ISDEFAULT=NO,RSELMODE=SELMODE_ROUND_ROBIN,REALNAME="epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org",PEERIDX=7,ROUTENAM="{item.operadora}_{item.pais},DESC="DRA MUN";\n\n'
        )
    else:
        # Comfone
        real_name = f'ADD IMSIHSS:IMSIPRE="{item.mcc}{item.mnc},HSSRLM="epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org.key2roam.comfone.com",MNNAME="{item.operadora}_{item.pais}";\n\n'
        dmrt = (
            f'ADD DMRT:ROUTEIDX={item.dmrt},ISDEFAULT=NO,RSELMODE=SELMODE_ROUND_ROBIN,REALNAME="epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org.key2roam.comfone.com",PEERIDX=6,ROUTENAM="{item.operadora}_{item.pais}",DESC="DRA CIA";\n'
            f'ADD DMRT:ROUTEIDX={item.dmrt},ISDEFAULT=NO,RSELMODE=SELMODE_ROUND_ROBIN,REALNAME="epc.mnc{dato_mnc}.mcc{item.mcc}.3gppnetwork.org.key2roam.comfone.com",PEERIDX=7,ROUTENAM="{item.operadora}_{item.pais}",DESC="DRA MUN";\n\n'
        )

    contenido = (
        f'## CONFIGURACIONES PARA LOS vUGW ##\n\n'
        f'ADD CONNECTPLMN:MCC="{item.mcc},MNC="{item.mnc},CC="{item.cc},SM=YES,SMS=YES,SMSCR=NO,COUNTRYORAREANAME="{item.operadora}_{item.pais}";\n\n'
        f'ADD IMSIGT:IMSIPRE="{item.mcc}{item.mnc}",GT="{item.cc}{item.nc}",MNNAME="{item.operadora}_{item.pais}"\n\n'
        f'{real_name}\n'
        f'{dmrt}\n\n'
        f'##### En caso de ser 5G #####\n'
        f'### Previamente verificar que no existan SIMs de prueba: LST NSACTRLPLCY, en caso de existir, eliminarlas con RMV\n\n'
        f'ADD NSACTRLPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="{item.mcc}{item.mnc}", ISDCNR=YES, ISSECRATRPT=NO, DESC="{item.operadora}_{item.pais}"\n\n'
        f'\n'
    )
    return contenido