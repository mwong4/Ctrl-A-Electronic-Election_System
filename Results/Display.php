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
		
        <p class="regular">
          <?php
            $result = exec("python Results.py"); //calls back end to get current results, then displays them
            echo $result;
          ?>
		    </p>
        
        <br><br><br>
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>
