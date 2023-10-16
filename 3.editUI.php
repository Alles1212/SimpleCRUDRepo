<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>無標題文件</title>
</head>

<body>

<p>my todo task</p>
<hr />
<?php
require("dbconfig.php");

$id=(int)$_GET['id'];
if ($id <=0) {
	echo "error!! empty ID";
	exit(0);
} 

	$sql = "select jobName, jobUrgent, jobContent from todo where id=?;"; 
	//SQL中的 ? 代表未來要用變數綁定進去的地方
	$stmt = mysqli_prepare($db, $sql ); //precompile sql指令，建立statement 物件，以便執行SQL
	mysqli_stmt_bind_param($stmt, "i", $id); //綁定參數到變數 $id 上, 型態為 i (integer)
	mysqli_stmt_execute($stmt); //執行SQL
	$result = mysqli_stmt_get_result($stmt); //取得查詢結果
if ($rs=mysqli_fetch_array($result)) { //將查詢結果取出轉成註標型陣列 (類似python 的dict)

	//若結果不為空值，代表有找到，將結果帶入html表單中作為預設值
?>
<form method="post" action="3.update.php">
<input type='hidden' name='jobID' value="<?php echo $id;?>" />
工作名稱: <input name="name" type="text"  value="<?php echo $rs['jobName'];?>" /> <br>

緊急程度: <select name="urgent">
<option selected value="<?php echo $rs['jobUrgent'];?>"><?php echo $rs['jobUrgent'];?></option>
<option value="普通">普通</option>
<option value="急">急</option>
<option value="急死了">急死了</option>
</select> <br>

工作說明: <textarea name='content'><?php echo $rs['jobContent'];?></textarea><br>

<input type="submit" name="Submit" value="送出" />

</form>

<?php
} else {
	echo "cannot find the message to edit.";
}
?>
</body>
</html>
