<?php
$id = $_POST["id"];
$name = $_POST["name"];
$gender = $_POST["gender"];
$password = $_POST["password"];
$sql = mysqli_connect("localhost","manager","123xyz,","sems");
if(!$sql){
	die("connect error ".mysqli_connect_error());
}

$password = MD5($password);
$ret = mysqli_query($sql,
"insert into tb_student (studentId,studentName,studentGender,password)".
" values($id, '$name', $gender, '$password')");

if($ret){
	echo "succeeded";
}else{
	echo "failed" . $sql->error;
}
mysqli_close($sql);

?>
