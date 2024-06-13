//  // Datos de ejemplo para los gráficos (reemplázalos con tus propios datos)
//  fetch(' http://144.22.133.47:8000/api/producto')
//  .then(response => response.json())
//  .then(data => {


//    // Configuración de gráfico de barra
//    var datosBarra = {
// labels: data.productos.map(item => (item.nombre_producto.length > 6 ? item.nombre_producto.substring(0, 6) : item.nombre_producto)),
// datasets: [{
// label: 'Cantidad de Stock',
// data: data.productos.map(item => item.cantidad_stock),
// backgroundColor: 'rgba(60, 199, 132, 0.5)',
// borderColor: 'rgba(60, 199, 132, 0.5)',
// borderWidth: 1
// }]
// };


// var dataTendenciaTemporada = JSON.parse('{{ data_most_viewed_presenter_name|safe }}');
// var data_most_viewed_presenter = JSON.parse('{{ data_most_viewed_presenter|safe }}');

// // Verificar si la variable es un objeto JavaScript
// if (typeof dataTendenciaTemporada === 'string') {
//     try {
//         dataTendenciaTemporada = JSON.parse(dataTendenciaTemporada);
//     } catch (e) {
//         console.error('Error al analizar JSON:', e);
//         dataTendenciaTemporada = [];
//     }
// }

// if (typeof data_most_viewed_presenter === 'string') {
//     try {
//         data_most_viewed_presenter = JSON.parse(data_most_viewed_presenter);
//     } catch (e) {
//         console.error('Error al analizar JSON:', e);
//         data_most_viewed_presenter = [];
//     }
// }

// var datosBarra = {
//     labels: dataTendenciaTemporada.map(item => item.full_name),
//     datasets: [{
//         label: 'Cantidad de Vistas',
//         data: data_most_viewed_presenter.map(item => item.views),
//         backgroundColor: 'rgba(60, 199, 132, 0.5)',
//         borderColor: 'rgba(60, 199, 132, 0.5)',
//         borderWidth: 1
//     }]
// };

// var opciones = {
//     responsive: true,
//     maintainAspectRatio: false,
// };

// var ctxBarra = document.getElementById('graficoBarra').getContext('2d');
// new Chart(ctxBarra, {
//     type: 'bar',
//     data: datosBarra,
//     options: opciones,
// });


// })

//  .catch(error => console.error('Error al obtener datos:', error));