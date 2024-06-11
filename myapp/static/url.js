document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('tuFormulario');
    var fechaInicioInput = document.getElementById('fecha_inicio');
    var fechaFinalInput = document.getElementById('fecha_final');

    // Initialize chart instance
    var ctxLineas = document.getElementById('myChart').getContext('2d');
    var opciones = {
        responsive: true,
        maintainAspectRatio: false,
    };
    var myChart = null;

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var fechaInicio = fechaInicioInput.value;
        var fechaFinal = fechaFinalInput.value;

        var apiUrl = 'http://34.151.236.58:3000/api/show/prediction';
        var urlWithParams = apiUrl + '?fecha_inicio=' + fechaInicio + '&fecha_final=' + fechaFinal;

        // Enviar la URL al servidor
        fetch('/get_services_ia_api_pre/?urlWithParams=' + encodeURIComponent(urlWithParams), {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta si es necesario
            console.log(data);

            // Use the dynamic data for the chart
            var dynamicData = data.data.prediccion.demanda.data;
            var predictionData = data.data.prediccion.prediccion.data;
            updateChart(myChart, dynamicData, predictionData);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Function to update the chart with dynamic data
    function updateChart(chart, dynamicData, predictionData) {
        var dates = dynamicData.map(item => formatDate(item.fecha));
        var demandTotals = dynamicData.map(item => item.total);
        var predictionTotals = predictionData.map(item => item.total);

        var chartData = {
            labels: dates,
            datasets: [
                {
                    label: 'Demand Prediction',
                    data: demandTotals,
                    fill: false,
                    borderColor: 'blue',
                },
                {
                    label: 'Predicción',
                    data: predictionTotals,
                    fill: false,
                    borderColor: 'red',
                },
            ],
        };

        if (!chart) {
            // Create a new chart if it doesn't exist
            myChart = new Chart(ctxLineas, {
                type: 'line',
                data: chartData,
                options: opciones,
            });
        } else {
            // Update the existing chart
            myChart.data.labels = chartData.labels;
            myChart.data.datasets = chartData.datasets;
            myChart.update(); // Update the chart to reflect the changes
        }
    }

    // Function to format date string
    function formatDate(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = (date.getMonth() + 1).toString().padStart(2, '0');
        const day = date.getDate().toString().padStart(2, '0');
        return `${year}-${month}-${day}`;
    }
});
