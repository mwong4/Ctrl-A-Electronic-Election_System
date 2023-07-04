


<?php

    
    $orig_HTML = <<<EOD

    <!DOCTYPE html>
    <html>
    <title>
        Ballot
    </title>

    <body>
        <h1>This is the ballot! Multiple Votes Allowed!</h1>

        <!-- form that is submitted via post -->
        <form action="Submit.php" method="post">

        <!-- repeating sections go here -->
            <div>
                    <h3>president (Multi vote available)</h3>
    
                    <p>Hi, my name is Joel. I code.</p>
    
                    <p>Hello, my name is Sasha. I like art.</p>
    
                </div>
    
            <div class="center checkbox-wrapper-13">
                <input type="checkbox" id="Joel" name="president[]" value="Joel">
                <label for="Joel">Support Joel</label><br>
            </div>
    
            <div class="center checkbox-wrapper-13">
                <input type="checkbox" id="Sasha" name="president[]" value="Sasha">
                <label for="Sasha">Support Sasha</label><br>
            </div>
    
        
            <div>
                    <h3>treasurer (Multi vote available)</h3>
    
                    <p>Hey, I'm K. I really like anime... and maybe money.</p>
    
                </div>
    
            <div class="center checkbox-wrapper-13">
                <input type="checkbox" id="K" name="treasurer[]" value="K">
                <label for="K">Support K</label><br>
            </div>
    
        
            <div>
                    <h3>promotion manager (Multi vote available)</h3>
    
                </div>
    
        

            <br><br>
            <label for="u_id">Your user id: </label>
            <!-- u_id stored here, passed on to back end with post call -->
            <input type="text" id="u_id" name="u_id" value="null_id" readonly>
            <br><br>
            <input type="submit" value="Submit">
            <br><br>
            <form action="Submit.php" method="post">

        </form>
        <br>
        <br>   
    </body>
    EOD;


    //HTML data (template)
    $orig_HTML = <<<EOD
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
                <h1 class="secondaryHeaderText">Election Ballot</h1>
                    <div id="#secondaryMiddleGradient"></div>
            </div>
            
    
            <div id="bottomGradient"></div>
            
            <div class="headerTheme">
                <h2 class="secondHeader"> Reminder: Multiple Vote Per Position Allowed/Encouraged! <h2>
            </div>
            
            <br>
            <div class="container">
                <!-- form that is submitted via post -->
                <form action="Submit.php" method="post">

                <br><br>
                <label for="u_id">Your user id: </label>
                <!-- u_id stored here, passed on to back end with post call -->
                <br><br>
                <input type="text" id="u_id" name="u_id" value="null_id" readonly>
                <br><br>
        
                    <!-- repeating sections go here -->
                        <div>
                    <h3>president (Multi vote available)</h3>
    
                    <p>Hi, my name is Joel. I code.</p>
    
                    <p>Hello, my name is Sasha. I like art.</p>
    
                </div>
    
            <div class="center checkbox-wrapper-13">
                <input type="checkbox" id="Joel" name="president[]" value="Joel">
                <label for="Joel">Support Joel</label><br>
            </div>
    
            <div class="center checkbox-wrapper-13">
                <input type="checkbox" id="Sasha" name="president[]" value="Sasha">
                <label for="Sasha">Support Sasha</label><br>
            </div>
    
                    
                        <div>
                    <h3>treasurer (Multi vote available)</h3>
    
                    <p>Hey, I'm K. I really like anime... and maybe money.</p>
    
                </div>
    
            <div class="center checkbox-wrapper-13">
                <input type="checkbox" id="K" name="treasurer[]" value="K">
                <label for="K">Support K</label><br>
            </div>
    
                    
                        <div>
                    <h3>promotion manager (Multi vote available)</h3>
    
                </div>
    
                    
        
                    <br><br>
                    <input type="submit" value="Submit">
                    <br><br>
                    <form action="Submit.php" method="post">
        
                </form>
            </div>
    
            <br><br><br>
            <div class="footer">
                Front-end/Back-end Developed by Wax <br>
                Ctrl-A (University of Waterloo) Electronic Election System
            </div>
        </Body>
    </html>
    
    EOD;

    // u_id from url embedded into template, then rendered
    $u_id = $_GET['u_id'];
    echo str_replace("null_id", $u_id, $orig_HTML);

?>