<!DOCTYPE html>

<html>
<!-- Header -->
	<head>
		<title>Ctrl A EES | terminal</title>
		
		<link rel="stylesheet" type="text/css" href="styles.css">
	</head>

  <!-- body -->
	<body>
  
		<!-- header -->
		<div class="secondaryHeader">

			<!-- the navigation bar -->
 			<div class="topnav">
				<img src="logo.png" alt="temporary plant logo" height="42" width="42" id="logo">
				<div id="topGradient"></div>
				<a href="Webfront/Initial.php" id="homeButton">Submission</a>
				<a href="Results/Display.php">Results</a>
			</div>
			<h1 class="secondaryHeaderText">Terminal Response</h1>
				<div id="#secondaryMiddleGradient"></div>
		</div>
		

		<div id="bottomGradient"></div>
		
		<div class="headerTheme">
			<h2 class="secondHeader"> Terminal Result <h2>
		</div>
		
        <p class="regular">
            <?php
                //gets email from previous page, formwards this to back end to be processed
                $input_pass = (array_key_exists('PASS', $_POST)) ? " -P " . $_POST['PASS'] : "";
                $input_cmd = (array_key_exists('CMD', $_POST)) ? $_POST['CMD'] : "";
				echo "Command: [python3 Database_commands.py" . $input_pass . " " . $input_cmd . " 2>&1] <br><br><br>";
                $result = shell_exec("python3 Database_commands.py" . $input_pass . " " . $input_cmd . " 2>&1");

                echo $result; //prints result/error message

                $_POST['PASS'] = NULL;
            ?>
		</p>

		<input type="button" class="button" onclick="window.location.href='terminal.php';" value="Back" />
        
        <br><br><br>
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>
