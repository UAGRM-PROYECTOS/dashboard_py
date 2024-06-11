// Hacer la solicitud a la API
fetch('http://144.22.133.47:8000/api/factura')
.then(response => response.json())
.then(data => {
  // Extraer datos relevantes de la respuesta JSON
  const facturas = data.facturas;
// Formatear las fechas en el formato deseado (YYYY-MM-DD)
const labels = facturas.map(factura => {
  const fecha = new Date(factura.fecha);
  const year = fecha.getFullYear();
  const month = String(fecha.getMonth() + 1).padStart(2, '0'); // Se suma 1 ya que los meses son base 0
  const day = String(fecha.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
});
  const ventasData = facturas.map(factura => factura.total);
  
  // Asumiendo que tienes un método para calcular el promedio móvil y la variación porcentual
  const promedioMovilData = calcularPromedioMovil(ventasData);
  const variacionPorcentualData = calcularVariacionPorcentual(ventasData);

  // Crear el gráfico con Chart.js
  var ctx = document.getElementById('tendenciasEstacionalesChart').getContext('2d');

  var chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Ventas Mensuales',
          data: ventasData,
          fill: false,
          borderColor: 'rgba(75, 192, 192, 1)',
        },
        {
          label: 'Promedio Móvil',
          data: promedioMovilData,
          fill: false,
          borderColor: 'rgba(255, 99, 132, 1)',
        },
        {
          label: 'Variación Porcentual',
          data: variacionPorcentualData,
          fill: false,
          borderColor: 'rgba(255, 205, 86, 1)',
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          type: 'category',
          labels: labels,
        },
      },
    },
  });
})
.catch(error => console.error('Error al obtener datos:', error));

// Función para calcular el promedio móvil (debes implementarla según tus necesidades)
// Función para calcular el promedio móvil
function calcularPromedioMovil(data, ventana = 3) {
const promedioMovil = [];
for (let i = 0; i < data.length; i++) {
const inicioVentana = Math.max(0, i - ventana + 1);
const finVentana = i + 1;
const subconjunto = data.slice(inicioVentana, finVentana);
const suma = subconjunto.reduce((total, valor) => total + valor, 0);
const promedio = suma / subconjunto.length;
promedioMovil.push(promedio);
}
return promedioMovil;
}

// Función para calcular la variación porcentual
function calcularVariacionPorcentual(data) {
const variacionPorcentual = [];
for (let i = 1; i < data.length; i++) {
const variacion = ((data[i] - data[i - 1]) / data[i - 1]) * 100;
variacionPorcentual.push(variacion);
}
return variacionPorcentual;
}
