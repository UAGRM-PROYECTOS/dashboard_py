 // Datos de ejemplo para los gráficos (reemplázalos con tus propios datos)
 fetch(' http://144.22.133.47:8000/api/producto')
 .then(response => response.json())
 .then(data => {


   // Configuración de gráfico de barra
   var datosBarra = {
labels: data.productos.map(item => (item.nombre_producto.length > 6 ? item.nombre_producto.substring(0, 6) : item.nombre_producto)),
datasets: [{
label: 'Cantidad de Stock',
data: data.productos.map(item => item.cantidad_stock),
backgroundColor: 'rgba(60, 199, 132, 0.5)',
borderColor: 'rgba(60, 199, 132, 0.5)',
borderWidth: 1
}]
};


// Configuración de gráfico de pastel (ejemplo)


// Configuración de los gráficos
var opciones = {
 responsive: true,
 maintainAspectRatio: false,
};


// Inicialización de los gráficos
var ctxBarra = document.getElementById('graficoBarra').getContext('2d');
new Chart(ctxBarra, {
 type: 'bar',
 data: datosBarra,
 options: opciones,

});


})

 .catch(error => console.error('Error al obtener datos:', error));