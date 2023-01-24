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
				<img src="../logosquaresuqaredgooderWHITE.png" alt="temporary plant logo" height="42" width="42" id="logo">
				<div id="topGradient"></div>
				<a href="../Webfront/Initial.php" id="homeButton">Submission</a>
				<a href="../Results/Display.php">Results</a>
			</div>
			<h1 class="secondaryHeaderText">Identity Verification</h1>
				<div id="#secondaryMiddleGradient"></div>
		</div>
		
		<div id="bottomGradient"></div>
		
        <p class="regular">
            <?php

            $u_id = $_GET['u_id']; //get u_id from url
            $output = shell_exec("python Verification.py $u_id"); // execute back end

            if ($output == "True\n") {
                header("Location: Ballot.php?u_id=$u_id"); // if user is valid, redirect to Ballot
            } else {
                echo "ERROR, Ballot id not found in database, or student has already voted.";
            }

            ?>
		</p>
        
        <br><br><br>
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>

