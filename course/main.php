<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" type="text/css" href="/sems/share/style.css"/>
		<title>学生选课管理系统</title>
	</head>
	
	<body>
		
		<?php include $_SERVER['DOCUMENT_ROOT']."/sems/share/header.php";?>
		<div class="mainblock">
		  <div class="mcontain">
		<form action="scripts/showCourse.php">
			<!--输入学号，开始选课-->
			学号: <input type="text" name="studentId" value="3840">
			<input type="submit" name="submit" value="开始选课"><br>
		</form>
		<br>
		<!--<input type="submit" value="学生选课" />-->
		
		<!--输入学号，查询已选课程，可以退选-->
		<form action="scripts/selectedCourse.php">
			学号: <input type="text" name="studentId" value="3840">
			<input type="submit" value="已选课程"><br>
		</form>
		<br>
		
		<!--输入课程名，开始查询，可以删除、修改、更新--->
		<form action="scripts/queryCourse.php">
			课程号:<input type="text" name="courseName" value="课程1">
			<input type="submit" value="课程查询"><br>
		</form>
		<br>
		
		<form method="POST" action="scripts/addCourse.php">
			教师号:<input type="text" name="teacherId" >
			教师名:<input type="text" name="teacherName">
			性别：<input type="text" name="teacherGender"><br>
			课程号:<input type="text" name="courseId" >
			课程名:<input type="text" name="courseName"><br>
			学分:<input type="text" name="courseCredit">
			学时:<input type="text" name="courseClass">
			容量:<input type="text" name="capacity" ><br>
			说明：如果数据库中已经存在相同的课程或者教师，则该插入行为将被忽略！<br>
			
			<input type="submit" value="添加课程">
		</form>
		
		<br />
		
		<div id="course"></div>
		</div>
	</div>
	</body>
	
</html>
