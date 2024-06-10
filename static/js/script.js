$(document).ready(function(){
  $("#compileButton").click(function(){
      const code = $("#consoleInput").val();

      $.ajax({
          url: '/compile',
          type: 'POST',
          data: { code: code },
          success: function(response) {
              // Agrega la salida al área de consola sin borrar lo anterior
              $("#consoleOutput").html(response.output);
          },
          error: function(error) {
              // Muestra un mensaje de error en la consola
              const currentOutput = $("#consoleOutput").html();
              $("#consoleOutput").html(currentOutput + "<br>" + "Error al compilar el código.");
          }
      });
  });
});
