
//Implementación de doble click sobre una fila de la tabla lista de VPNs

$("#tabla tr").dblclick(function(){
    let apnid = $(this).find('td:eq(0)').html();
    let apn = $(this).find('td:eq(1)').html();

    let texto = "APN ID: " + apnid + "<br>APN: " + apn;

    //SweetAlert
    Swal.fire({
        title: "<span style='font-size: 2rem; color:orange;'>DATOS DE LA VPN</span>",
        html: texto,
        icon: '<span style="font-size: 1.5rem;">success</span>',
        button: "Cerrar"
    });
});