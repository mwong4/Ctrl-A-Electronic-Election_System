<!DOCTYPE html>

<html>
<!-- Header -->
	<head>
		<title>Ctrl A EES | Dev - Terminal</title>
		
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
			<h1 class="secondaryHeaderText">Submission</h1>
				<div id="#secondaryMiddleGradient"></div>
		</div>
		

		<div id="bottomGradient"></div>
		
		<div class="headerTheme">
			<h2 class="secondHeader"> Terminal <h2>
		</div>
		
        <br>
		<div class="container">
				<form action="terminal_response.php", method="post">
		 
				<label for="fname">Password</label>
				<input type="text" id="fname" name="PASS" placeholder="passwd">
				<label for="fname">Command</label>
				<input type="text" id="fname" name="CMD" placeholder="echo 'hello'">
                <input type="submit" value="submit" name="SUBMIT">
			 </form>
		</div>

        <br><br><br>
        <div class="footer">
            Front-end/Back-end Developed by Wax <br>
            Ctrl-A (University of Waterloo) Electronic Election System
		</div>
	</Body>
</html>
