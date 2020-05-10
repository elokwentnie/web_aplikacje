function drawChart(request_data, title, element_id) {
    var data = new google.visualization.DataTable();
    data.addColumn('string', title);
    data.addColumn('number', 'Liczba osob');
    data.addRows( {{ request_data|tojson }} );

    var options = {
          title: title,
          pieHole: 0.4,
        };

    var chart = new google.visualization.PieChart(document.getElementById(element_id));
    chart.draw(data, options);
  }