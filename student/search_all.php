<?php
$sql = mysqli_connect("localhost", "manager","123xyz,", "sems");
if(!$sql){
	die("connect failed");
}

$result = mysqli_query($sql,
	"select student_id, student_name, student_gender from tb_student");
if($result){
	$ret= mysqli_fetch_all($result, MYSQLI_ASSOC);
}else{
	die("search failed");
}
$len=count($ret);

$info = json_encode($ret);
echo $info;
?>
