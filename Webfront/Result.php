<!DOCTYPE html>

<html>
<!-- Header -->
	<head>
		<title>Ctrl A EES | Submission</title>
		
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
			<h1 class="secondaryHeaderText">Submission Result</h1>
				<div id="#secondaryMiddleGradient"></div>
		</div>
		

		<div id="bottomGradient"></div>
		
		<div class="headerTheme">
			<h2 class="secondHeader"> Redirecting in 10 Seconds... <h2>
		</div>
		
        <p class="regular">
            <?php
                //gets email from previous page, formwards this to back end to be processed
                $input_email = (array_key_exists('EMAIL', $_POST)) ? $_POST['EMAIL'] : "";
                $result = exec("python Email.py $input_email");

                echo $result; //prints result/error message

                $_POST['EMAIL'] = NULL;
                header( "refresh:10;url=Initial.php" ); //forwards the user back to submission page
            ?>
		</p>
        
        <br><br><br>
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>
