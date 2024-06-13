var dataTendenciaTemporada = JSON.parse('{{ data_top_three_news|safe }}');
    
// Verificar si la variable es un objeto JavaScript
if (typeof dataTendenciaTemporada === 'string') {
    // Convertir la cadena JSON a un objeto JavaScript
    try {
        dataTendenciaTemporada = JSON.parse(dataTendenciaTemporada);
    } catch (e) {
        console.error('Error al analizar JSON:', e);
        dataTendenciaTemporada = [];
    }
}
    
// Configuración de gráfico de pastel
var datosPastel = {
    labels: dataTendenciaTemporada.map(item => item.titulo),
    datasets: [{
        data: dataTendenciaTemporada.map(item => item.percentage),
        backgroundColor: ['rgba(255, 99, 132, 0.5)', 'rgba(54, 162, 235, 0.5)', 'rgba(255, 206, 86, 0.5)'],
        hoverBackgroundColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
    }]
};

var ctxPastel = document.getElementById('graficoPastel2').getContext('2d');
new Chart(ctxPastel, {
    type: 'doughnut',
    data: datosPastel,
    options: {
        // Puedes personalizar las opciones según tus necesidades
    }
});