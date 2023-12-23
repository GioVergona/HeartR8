document.addEventListener('DOMContentLoaded', function () {
    // Obtener el contexto del canvas
    var ctx = document.getElementById('myChart').getContext('2d');

    // Inicializar el gráfico con datos iniciales
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Valores',
                data: [],
                fill: false,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Elemento HTML para mostrar el valor actual
    var valueDisplay = document.getElementById('valueDisplay');

    // Función para generar y agregar valores aleatorios al gráfico
    function generateAndAddData() {
        // Generar un nuevo valor aleatorio
        var newValue = Math.floor(Math.random() * 100);

        // Obtener el tiempo actual en formato HH:mm:ss
        var now = new Date();
        var time = now.toLocaleTimeString();

        // Mostrar el valor actual en la web
        valueDisplay.textContent = newValue;

        // Agregar el nuevo valor y etiqueta al gráfico
        myChart.data.labels.push(time);
        myChart.data.datasets[0].data.push(newValue);

        // Limitar el número de puntos en el gráfico a 10
        var maxDataPoints = 20;
        if (myChart.data.labels.length > maxDataPoints) {
            myChart.data.labels.shift();
            myChart.data.datasets[0].data.shift();
        }

        // Actualizar el gráfico
        myChart.update();

        // Llamar recursivamente para continuar generando y agregando datos
        setTimeout(generateAndAddData, 1000); // Actualiza cada segundo
    }

    // Llamar a la función para iniciar la generación continua de datos
    generateAndAddData();
});
