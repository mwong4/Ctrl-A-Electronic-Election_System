<!DOCTYPE html>
<html>
<title>
    Submission
</title>

<body>
    <h2>Please Enter Wat-Email. If valid, your ballot will be emailed to your Waterloo address.</h2>
    <form action="Result.php" method="post"> 
        E-Mail: <input type="text" placeholder="jdoe@waterloo.ca" name="EMAIL" id="email "><br>
        <input type="submit" value="submit" name="SUBMIT">
    </form>
</body>
</html>

<?php

$output = shell_exec("python Email.py");
?>