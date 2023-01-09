<!DOCTYPE html>
<html>
<title>
    Verification
</title>

<body>
    <h2>Verifying Ballot...</h2>
</body>

<?php

$u_id = $_GET['u_id'];
$output = shell_exec("python Verification.py $u_id");
echo ("output: |$output|");

if ($output == "True\n") {
    header("Location: Ballot.php");
} else {
    echo "ERROR, Ballot id does not exist";
}

?>
