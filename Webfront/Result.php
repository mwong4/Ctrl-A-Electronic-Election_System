<!DOCTYPE html>
<html>
<title>
    Result
</title>

<body>
    <h2>Please Check SPAM Folder</h2>
    <p>redirecting in 10 seconds...</p>
</body>
</html>

<?php

//gets email from previous page, formwards this to back end to be processed
$input_email = (array_key_exists('EMAIL', $_POST)) ? $_POST['EMAIL'] : "";
$result = exec("python Email.py $input_email");

echo $result; //prints result/error message

$_POST['EMAIL'] = NULL;
header( "refresh:10;url=Initial.php" ); //forwards the user back to submission page

?>