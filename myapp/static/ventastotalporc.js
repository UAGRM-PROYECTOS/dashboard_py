fetch('http://144.22.133.47:8000/api/crecimiento')
.then(response => response.json())
.then(data => {
   // Accede directamente a la propiedad overall_growth_percentage
   const porcentajeCambio = data.overall_growth_percentage;

   // Verifica si el elemento con el id 'porcentajeCambio' existe antes de intentar actualizarlo
   const elementoPorcentajeCambio = document.getElementById('porcentajeCambio');
   if (elementoPorcentajeCambio) {
      // Actualiza el elemento HTML con el id 'porcentajeCambio' con el porcentaje calculado
      elementoPorcentajeCambio.innerText = `${porcentajeCambio.toFixed(2)}% `; // toFixed(2) para mostrar dos decimales
   } else {
      console.error('Elemento con id "porcentajeCambio" no encontrado.');
   }
})
.catch(error => console.error('Error al obtener datos:', error));