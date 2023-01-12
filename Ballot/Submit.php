<!DOCTYPE html>
<html>
<title>
    Submit
</title>

<body>
    <h1>Thank you for voting</h1>
    <br>
    <input type="button" onclick="window.location.href='http://localhost/Results/Display.php';" value="check out results" />
    <br>
</body>

<?php
    $post_results = $_POST;
    $json_encoded = json_encode($post_results);
    $escaped_json = escapeshellarg($json_encoded);
    $command = escapeshellcmd("py Voting.py $escaped_json");
    $result = exec($command);

    echo $result;
?>