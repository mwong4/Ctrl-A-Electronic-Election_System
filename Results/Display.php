<!DOCTYPE html>

<html>
<!-- Header -->
	<head>
		<title>Ctrl A EES | Results</title>
		
		<link rel="stylesheet" type="text/css" href="../styles.css">
	</head>

  <!-- body -->
	<body>
  
		<!-- header -->
		<div class="secondaryHeader">

			<!-- the navigation bar -->
 			<div class="topnav">
				<img src="../logosquaresuqaredgooderWHITE.png" alt="temporary plant logo" height="42" width="42" id="logo">
				<div id="topGradient"></div>
				<a href="../Webfront/Initial.php" id="homeButton">Submission</a>
				<a href="../Results/Display.php">Results</a>
			</div>
			<h1 class="secondaryHeaderText">Current Result</h1>
				<div id="#secondaryMiddleGradient"></div>
		</div>
		

		<div id="bottomGradient"></div>

		<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
		<script>
			Chart.defaults.font.size = 16;
			Chart.defaults.backgroundColor = '#9BD0F5';
			Chart.defaults.borderColor = '#acadad';
			Chart.defaults.color = '#FFF';
			Chart.defaults.family = 'Trebuchet MS';
		</script>

		<?php
			$template = "
				<div class='headerTheme'>
					<h2 class='secondHeader'><h2>
				</div>
				<canvas id='chart_id#' style='width:100%;max-width:40%;margin:auto;'></canvas>
				<script>
				var xValues = [];
				var yValues = [];
				var color = '#fc9fad';
				var barColors = [color, color, color, color, color, color, color, color, color, color, color, color, color, color, color, color, color, color];
				var title = 'Votes';
				new Chart('chart_id#', {type: 'bar',data: {labels: xValues, datasets: [{backgroundColor: barColors,data: yValues,label: title}]}});
				</script>
			";

            $result = exec("python Results.py"); //calls back end to get current results, then displays them
			$result = str_replace("'", "\"", $result);
            $decoded_json = json_decode($result, false);
			foreach($decoded_json as $key => $value) {
				$output = $template;
				$title = $key;
				$people = "[";
				$votes = "[";

				foreach($value as $inner_key => $inner_value) {
					$people = $people . "'" . $inner_key . "', ";
					$votes = $votes . $inner_value . ", ";
				}
				$people = rtrim($people, ", ");
				$votes = rtrim($votes, ", ");
				$people = $people ."]";
				$votes = $votes . "]";

				$output = str_replace("<h2 class='secondHeader'><h2>", "<h2 class='secondHeader'>" . $title ."<h2>", $output);
				$output = str_replace("chart_id#", "chart_id#" . $key, $output);
				$output = str_replace("var xValues = [];", "var xValues = " . $people . ";", $output);
				$output = str_replace("var yValues = [];", "var yValues = " . $votes . ";", $output);
				echo $output;
			}
        ?>

		<br>
		<br>
		<p class="regular">
          <?php
            $result = exec("python Results.py"); //calls back end to get current results, then displays them
            echo $result;
          ?>
		</p>
        
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>
