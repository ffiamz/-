<?php
echo "<div id='header'><ul>";
session_start();
if(isset($_SESSION['student_login_id'])){
	echo "<li><a href='/sems/student/login.php?action=logout'>
		退出登陆
		</a></li>";

}else{
	echo "<li><a href='/sems/student/student_login.html'>登陆</a></li>
		<li><a href='/sems/student/student_add.html'>注册</a></li>";
}

echo "<li><a href='/sems/course/main.html'>课程</a></li>
	<li><a href='/sems/student/student_change.html'>个人信息</a></li>
	<li><a href='/sems/student/student_search.html'>学生信息</a></li>
	</ul></div>";
?>
