<!DOCTYPE html>
<html>
<title>
    Result
</title>

<body>
    <h2>Please Check SPAM Folder</h2>
</body>
</html>

<?php

$input_email = (array_key_exists('EMAIL', $_POST)) ? $_POST['EMAIL'] : "";
$result = exec("python Email.py $input_email");

echo $result;

$_POST['EMAIL'] = NULL;

?>