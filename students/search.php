<?php
$sql = mysqli_connect('localhost', 'root', '262359for*', 'sems');
$id = $_POST["id"];

$result = mysqli_query($sql,
	"select student_id, student_name, student_gender from tb_student where ".
	"student_id = ".$id);
if($result){
	$ret= mysqli_fetch_assoc($result);
}else{
	die("search failed");
}
$info = json_encode($ret);
echo $info;
?>
