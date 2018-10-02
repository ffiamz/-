<?php
$id = $_GET["id"];
$sql = mysqli_connect("localhost","root","262359for*","sems");
if(!$sql){
	die("connect error ".mysqli_connect_error());
}
$ret = mysqli_query($sql,
	"delete from tb_student where student_id=".$id);

if($ret){
	echo "succeeded";
}else{
	echo "failed";
}
mysqli_close($sql);

?>
