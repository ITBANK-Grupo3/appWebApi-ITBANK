const apiDolar = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";
const tablaDolar = document.querySelector("#tablaDolar");
const fecha = new Date();
const dia =  String(fecha.getDate()).padStart(2, '0') + '/' + String(fecha.getMonth() + 1).padStart(2, '0')+ '/' + String(fecha.getFullYear() + 1).padStart(2, '0');
const horas = String(fecha.getHours());
const minutos = String(fecha.getMinutes());
const segundos = String(fecha.getSeconds());

function compra(valor) {
    if (valor == "No Cotiza") {
        return "---"
    }
    else if (valor.toString().length > 5) {
        return valor.toString().slice(0, 5);
    }
    else {
        return valor;
    }
}
function liqui(nombre) {
    if (nombre == "Dolar Contado con Liqui") {
        return "Contado con Liqui";
    }
    else {
        return nombre;
    }
}

function setImgVariacion(dato){
    
    if(dato.indexOf("-") < 0 ){
      return '<div class="cono-verde"></div>'
    }else{
      return '<div class="cono-rojo"></div>'
  }
  }
function traerPreciosDolar() {
    fetch(apiDolar)
        .then((res) => res.json())
        .then((data) => {
            let dolarPrecio = data;
            let res = dolarPrecio.filter(precio =>
                precio.casa.nombre !== "Argentina" &&
                precio.casa.venta != 0 &&
                precio.casa.variacion)

            console.log(res.forEach(element => console.log(parseFloat(element.casa.variacion))));
            res.forEach(element => 
                
                 
                tablaDolar.innerHTML += `
                <div class="dolarcards col fw-bold p-0 m-1 border border-white rounded">
                    <div class="p-1 "> ${liqui(element.casa.nombre)}</div>
                    <div class="row fw-bold w-100 m-0" style="font-size:1rem">
                    <div class="col p-0">
                        Compra
                    </div>
                    <div class="col p-0">
                        Venta
                    </div>
                    </div>
                    <div class="row fw-bold  w-100 m-0">
                        <div class="col p-0">
                            $${compra(element.casa.compra)}
                        </div>
                        <div class="col p-0">
                            $${compra(element.casa.venta)}
                        </div>
                    </div>
                    <div style="font-size:15px" class=""> ${setImgVariacion(element.casa.variacion)} Variación ${element.casa.variacion} </div>
                    <div style="font-size:10px" class="" > Actualización <br> ${dia} ${horas}:${minutos}:${segundos}</div>
                </div>

                ` );

             
       
               
       })
}

window.onload = () => {
    traerPreciosDolar();
}
