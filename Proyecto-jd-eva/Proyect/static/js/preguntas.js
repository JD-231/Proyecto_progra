async function preguntas() {
    console.log("Botón presionado");

    const texto = document.getElementById("texto").value;
    console.log(texto);

    const respuesta = await fetch("/api/preguntas",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            texto:texto
        })

    });

    const datos = await respuesta.json();

    document.getElementById("resultado").innerHTML =
        datos.resultado;

}