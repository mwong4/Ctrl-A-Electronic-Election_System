<!DOCTYPE html>

<html>
<!-- Header -->
	<head>
		<title>Ctrl A EES | Ballot</title>
		
		<link rel="stylesheet" type="text/css" href="../styles.css">
	</head>

  <!-- body -->
	<body>
  
		<!-- header -->
		<div class="secondaryHeader">

			<!-- the navigation bar -->
 			<div class="topnav">
				<img src="../logo.png" alt="temporary plant logo" height="42" width="42" id="logo">
				<div id="topGradient"></div>
				<a href="../Webfront/Initial.php" id="homeButton">Submission</a>
				<a href="../Results/Display.php">Results</a>
			</div>
			<h1 class="secondaryHeaderText">Thank You for Voting!</h1>
				<div id="#secondaryMiddleGradient"></div>
		</div>
		
		<div id="bottomGradient"></div>
		
        <?php
            //encodes data from Ballot page's post into json data
            $post_results = $_POST;
            $json_encoded = json_encode($post_results);
            $escaped_json = escapeshellarg($json_encoded);
            $command = escapeshellcmd("py Voting.py $escaped_json");
            $result = exec($command); // execute back end, passing on user data

            echo $result;
        ?>

        <input type="button" class="button" onclick="window.location.href='../Results/Display.php';" value="check out results" />
        
        <br><br><br>
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>

