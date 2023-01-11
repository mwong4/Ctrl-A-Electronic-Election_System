<!DOCTYPE html>
<html>
<title>
    Submit
</title>

<body>
    <h1>Thank you for voting</h1>
</body>

<?php
    $post_results = $_POST;
    $json_encoded = json_encode($post_results);
    $escaped_json = escapeshellarg($json_encoded);
    $command = escapeshellcmd("py Voting.py $escaped_json");
    $result = exec($command);

    echo $result;
?>