<?php
$id = $_POST["id"];
$name = $_POST["name"];
$gender = $_POST["gender"];
$sql = mysqli_connect("localhost","manager","123xyz,","sems");
if(!$sql){
	die("connect error ".mysqli_connect_error());
}

$ret = mysqli_query($sql,
	"insert into tb_student (student_id,student_name,student_gender) values(".
	$id. ",\"". $name. "\",". $gender.")");

if($ret){
	echo "succeeded";
}else{
	echo "failed";
}
mysqli_close($sql);

?>
