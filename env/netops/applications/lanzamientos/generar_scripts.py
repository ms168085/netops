
# Funcion para generar script para el HSS MAG y MUN
# item = objeto lanzamiento
def generar_script_hss(item, nodo):
    hss = "MAG" if nodo == "MAG" else "MUN"
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
        f'DIA-CFG-Drt=epc.mnc{item.mnc}.mcc{item.mcc}.3gppnetwork.org:HSS_ESM:FALSE\n'
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