const URLDOLAR = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";
const tablaPrecios = document.querySelector("#tablaPrecioDolares");
const fecha = new Date();
const dia =
	String(fecha.getDate()).padStart(2, "0") +
	"/" +
	String(fecha.getMonth() + 1).padStart(2, "0") +
	"/" +
	String(fecha.getFullYear() + 1).padStart(2, "0");
const horas = String(fecha.getHours());
const minutos = String(fecha.getMinutes());
const segundos = String(fecha.getSeconds());

function traerPreciosDolar() {
	fetch(URLDOLAR)
		.then((res) => res.json())
		.then((data) => {
			let preciosDolar = data;
			preciosDolar
				.filter(
					(precio) =>
						precio.casa.nombre !== "Argentina" &&
						precio.casa.venta != 0 &&
						precio.casa.variacion
				)
				.forEach((precio) => {
					tablaPrecios.innerHTML += `
        <section class="cuenta-info">      
        <h1 class="tipo__dolar">${precio.casa.nombre}</h1>
        <section class="dolar__precio">
          <article class="dolar__precio--articulo">
            <h4>Compra</h4>
            <h2>${precio.casa.compra != "No Cotiza" ? "$" : ""}${
						precio.casa.compra
					}</h2>
          </article>
          <article class="dolar__precio--articulo">
            <h4>Venta</h4>
            <h2>$${precio.casa.venta}</h2>
          </article>
        </section>
        <div> 
        <article class="dolar__precio--datos">
        <div class= "${
					precio.casa.variacion.indexOf("-") < 0 ? conoverde : conorojo
				}">    </div>
          <h4 class="dolar__precio--dato">VARIACION ${
						precio.casa.variacion
					}%</h4>
        <h5 class="dolar__precio--dato center">ACTUALIZADO: <br> ${dia} ${horas}:${minutos}:${segundos}</h5>

          

        </article>
      </section>
        `;
				});
		});
}

function esconderLoader() {
	this.document.getElementById("loader").classList.toggle("loader2");
}

window.onload = () => {
	traerPreciosDolar();
	setTimeout(esconderLoader, 320);
};
let conorojo = "cono-rojo";
let conoverde = "cono-verde";
