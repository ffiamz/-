<?php
$id = $_GET["id"];
$sql = mysqli_connect("localhost","manager","123xyz,","sems");
if(!$sql){
	die("connect error ".mysqli_connect_error());
}
$ret = mysqli_query($sql,
	"delete from tb_student where studentId=".$id);

if($ret){
	echo "succeeded";
}else{
	echo "failed";
}
mysqli_close($sql);

?>
