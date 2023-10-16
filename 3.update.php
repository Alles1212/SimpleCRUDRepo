<?php
require('dbconfig.php');

$jobID = $_POST['jobID'];
$jobName=$_POST['name']; //$_GET, $_REQUEST
$jobUrgent=$_POST['urgent'];
$jobContent=$_POST['content'];

	$sql = "update todo set jobName=?, jobUrgent=?, jobContent=? where id=?"; //SQL中的 ? 代表未來要用變數綁定進去的地方
	$stmt = mysqli_prepare($db, $sql); //prepare sql statement
	mysqli_stmt_bind_param($stmt, "sssi", $jobName, $jobUrgent,$jobContent, $jobID); //bind parameters with variables, with types "sss":string, string ,string
	mysqli_stmt_execute($stmt);  //執行SQL
	echo "message added.";
?>
<a href="2.list.php">回工作列表</a>
