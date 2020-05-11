function drawChart() {
     var data = new google.visualization.DataTable();
     data.addColumn('string', 'Wiek');
     data.addColumn('number', 'Liczba osob');
     data.addRows( {{ ages|tojson }} );

     var options = {
          title: 'Wiek',
          pieHole: 0.4
        };

      var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
      chart.draw(data, options);
    }