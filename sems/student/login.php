<?php
session_start();

if(isset($_GET['action']) && $_GET['action']=="logout"){
	unset($_SESSION['student_login_id']);
	echo "logout success";
	exit;
}

if(!isset($_POST['submit'])){
	exit('failed');
}
$id = $_POST['id'];
$password = MD5($_POST['password']);

$sql = mysqli_connect("localhost","manager","123xyz,","sems");
if(!$sql){
	die("connect error ".mysqli_connect_error());
}
$ret = mysqli_query($sql,
	"select password from tb_student ".
	"where studentId = $id ");
$result = mysqli_fetch_assoc($ret);
if(strcmp($password,$result['password'])!=0){
	mysqli_close($sql);
	exit('wrong password or id');
}

$_SESSION['student_login_id']=$id;
echo "success $id";

mysqli_close($sql);
?>
