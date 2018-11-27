<?php
$sql = mysqli_connect("localhost","manager","123xyz,", "sems");
$id = $_POST["id"];

$result = mysqli_query($sql,
	"select studentId, studentName, studentGender from tb_student where ".
	"studentId = ".$id);
if($result){
	$ret= mysqli_fetch_assoc($result);
}else{
	die("search failed");
}
$info = json_encode($ret);
echo $info;
?>
