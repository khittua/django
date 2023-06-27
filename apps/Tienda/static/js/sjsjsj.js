function load(){
    api();

}

function toggleDarkMode() {
  var style = $('#style');

  if (style.length > 0) {
    var currentHref = style.attr('href');
    
    if (currentHref && currentHref.match(staticCSS)) {
      style.attr('href', staticCSSDark);
    } else {
      style.attr('href', staticCSS);
    }
  }
}

$(document).ready(function() {
  $('#toggle-theme').click(function() {
    toggleDarkMode();
  });
});

function api(){
    fetch('http://worldtimeapi.org/api/ip')
    .then(response => response.json())
    .then(data => {
        const datetime = new Date(data.datetime);
        const hour = datetime.getHours();
        const minute = datetime.getMinutes();
        const second = datetime.getSeconds();
        const StringHora = `${hour < 10 ? "0" + hour : hour}:${minute < 10 ? "0" + minute : minute}:${second < 10 ? "0" + second : second}`  
        let hora = document.getElementById("hora");
        hora.innerText = StringHora;
    })
}

setInterval(api, 1000);



$("#ocultar").on("click",function(){
    //$(".primero").hide();
    //$(".primero").fadeOut();
    $("#ocultar").slideUp();
    $(".primero").slideUp();
})

$(function(){
    $("#miFormulario").validate({
        rules:{
            txtUsuario:{
                required: true,
                minlength:5
            },
            txtContraseña:{
                required: true,
                minlength:3
            }
          
        },
        messages:{
            txtUsuario:{
                required: "Debe ingresar un usuario",
                minlength: "El largo minimo es 5"
            },
            txtContraseña:{
                required: "Debe ingresar su contraseña",
                minlength: "El largo minimo es 3"
            }
        }
    })
})



$(function(){
    $("#formRegistro").validate({
        rules:{
            txtNombre:{
                required: true,
                minlength:5
            },
            txtUsuario:{
                required: true,
                minlength:5
            },
            txtCorreo:{
                required: true,
                minlength:5,
                email: true
            },
            txtCCorreo:{
                required: true,
                minlength:5,
                equalTo: "#txtCorreo"
            },
            txtContraseña:{
                required: true,
                minlength:3
            },
            txtCContraseña:{
                required: true,
                minlength:3
            }
            
        },
        messages:{
            txtNombre:{
                required: "Debe ingresar un nombre",
                minlength: "El largo minimo es 5"
            },
            txtUsuario:{
                required: "Debe ingresar un usuario",
                minlength: "El largo minimo es 5"
            },
            txtCorreo:{
                required: "Debe ingresar un correo",
                minlength: "El largo minimo es 5"
            },
            txtCCorreo:{
                required: "Debe confirmar su correo",
                minlength: "El largo minimo es 5"
            },
            txtContraseña:{
                required: "Debe ingresar un contraseña",
                minlength: "El largo minimo es 3"
            },
            txtCContraseña:{
                required: "Debe confirmar su contraseña",
                minlength: "El largo minimo es 3"
            }
        }
    })
})



