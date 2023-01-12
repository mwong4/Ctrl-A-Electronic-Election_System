<!DOCTYPE html>
<html>
<title>
    Verification
</title>

<body>
    <h2>Verifying Ballot...</h2>
</body>

<?php

    $u_id = $_GET['u_id']; //get u_id from url
    $output = shell_exec("python Verification.py $u_id"); // execute back end

    if ($output == "True\n") {
        header("Location: Ballot.php?u_id=$u_id"); // if user is valid, redirect to Ballot
    } else {
        echo "ERROR, Ballot id not found in database, or student has already voted.";
    }

?>
