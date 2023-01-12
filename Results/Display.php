<!DOCTYPE html>
<html>
<title>
    Results
</title>

<body>
    <h1>Vote Results (Current)</h1>
</body>

<?php
  $result = exec("python Results.py");
  echo $result;
?>