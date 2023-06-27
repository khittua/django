formulario.addEventListener('submit', function(evento) {
    evento.preventDefault();

    console.log('Submit button clicked'); // Agrega esta línea

    if (document.getElementById("txtSku").value.length == 0) {
        alert("Debe ingresar el código del producto.");
        return;
    } else {
        this.submit();
    }
});
