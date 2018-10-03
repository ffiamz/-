<?php
$id = $_POST["id"];
$name = $_POST["name"];
$gender = $_POST["gender"];
$sql = mysqli_connect("localhost","manager","123xyz,","sems");
if(!$sql){
	die("connect error ".mysqli_connect_error());
}

$ret = mysqli_query($sql,
	"update tb_student set student_name=\"".$name.
	"\", student_gender=".$gender." where student_id=".$id);

if($ret){
	echo "succeeded";
}else{
	echo "failed";
}
mysqli_close($sql);

?>
