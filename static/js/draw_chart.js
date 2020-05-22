function drawChart(title, answers) {
     var data = new google.visualization.DataTable();
     data.addColumn('string', title);
     data.addColumn('number', 'Liczba osob');
     data.addRows( answers );

     var options = {
          title: title,
          pieHole: 0.4
        };

      var chart = new google.visualization.PieChart(document.getElementById(title + 'chart'));
      chart.draw(data, options);
    }
