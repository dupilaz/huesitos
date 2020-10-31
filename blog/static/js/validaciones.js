$(document).ready(function(){

    $('#btnSend').click(function(){

        var errores = '';

        //Validaciones campo Nombre
        if( $('#nombre').val() == '' ){
            errores += '<p>Escriba un Nombre</p>';
            $('#nombre').css("border-bottom-color", "#F14B4b")
        } else {
            $('#nombre').css("border-bottom-color", "#d1d1d1")
        }

        //validando campo correo
        if( $('#email').val() == ''){
            errores += '<p>Ingrese un Correo</p>';
            $('#email').css("border-bottom-color", "#F14B4b")
        } else {
            $('#email').css("border-bottom-color", "#d1d1d1")
        }

        //validando campo asunto
        if( $('#asunto').val() == ''){
            errores += '<p>Debe Ingresar asunto del mensaje';
            $('#asunto').css("border-bottom-color", "#F14B4b")
        } else {
            $('#asunto').css("border-bottom-color", "#d1d1d1")
        }

        //validando campo mensaje
        if( $('#mensaje').val() == ''){
            errores += '<p>Escriba Un mensaje</p>';
            $('#mensaje').css("border-bottom-color", "#F14B4b")
        } else {
            $('#mensaje').css("border-bottom-color", "#d1d1d1")
        }

        // Enviando Mensajes de errores
        if ( errores == '' == false){
            var mensajeError = '<div class="modal_wrap">'+
                                    '<div class="mensaje_modal">'+
                                        '<h3>Errores Encontrados!</h3>'+
                                        errores+
                                        '<span id="btnClose">Cerrar</span>'+
                                    '</div>'+
                                '</div>'
            $('body').append(mensajeError);
        }

        // Cerrar la modal
        $('#btnClose').click(function(){
            $('.modal_wrap').remove();
        });

    }); //fin btnSend

}); //fin document





