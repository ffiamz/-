<?php
echo "<div id='header'><ul>";
session_start();
if(isset($_SESSION['student_login_id'])){
	echo "<li><a href='/sems/student/login.php?action=logout'>
		退出登陆
		</a></li>";

}else{
	echo "<li><a href='/sems/student/student_login.php'>登陆</a></li>
		<li><a href='/sems/student/student_add.php'>注册</a></li>";
}

echo "<li><a href='/sems/course/main.php'>课程</a></li>
	<li><a href='/sems/student/student_change.php'>个人信息</a></li>
	<li><a href='/sems/student/student_search.php'>学生信息</a></li>
	</ul></div>";
?>
