<!DOCTYPE html>
<html>
<title>
    Results
</title>

<body>
    <h1>Vote Results (Current)</h1>
</body>

<?php
  $result = exec("python Results.py"); //calls back end to get current results, then displays them
  echo $result;
?>