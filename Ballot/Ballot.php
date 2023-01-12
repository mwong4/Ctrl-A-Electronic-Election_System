<?php

    $orig_HTML = <<<EOD

    <!DOCTYPE html>
    <html>
    <title>
        Ballot
    </title>

    <body>
        <h1>This is the ballot! Multiple Votes Allowed!</h1>

        <form action="Submit.php" method="post">
            <div>
                <h3>president (Multi vote available)</h3>
    
                <p>Hi, my name is Joel. I code.</p>
    
                <p>Hello, my name is Sasha. I like art.</p>
    
            </div>
    
            <input type="checkbox" id="Joel" name="president[]" value="Joel">
            <label for="Joel">Support Joel</label><br>
    
            <input type="checkbox" id="Sasha" name="president[]" value="Sasha">
            <label for="Sasha">Support Sasha</label><br>
    
        
            <div>
                <h3>treasurer (Multi vote available)</h3>
    
                <p>Hey, I'm K. I really like anime... and maybe money.</p>
    
            </div>
    
            <input type="checkbox" id="K" name="treasurer[]" value="K">
            <label for="K">Support K</label><br>
    
        
            <div>
                <h3>promotion manager (Multi vote available)</h3>
    
            </div>
    
        

            <br><br>
            <label for="u_id">Your user id: </label>
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

    $u_id = $_GET['u_id'];
    echo str_replace("null_id", $u_id, $orig_HTML);

?>