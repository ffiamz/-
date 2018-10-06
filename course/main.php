<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" type="text/css" href="/sems/share/style.css"/>
        <style type="text/css">
        #begin {
            padding:0.2cm 0.4cm 0.3cm 0.4cm;
            background-color: #C3C0C0;
        }
        
        #selected {
            position: relative;
            //left: 50px;
            margin : 10px 0px 15px 5px;
            padding:0.2cm 0.4cm 0.3cm 0.4cm;
            background-color: #C3C0C0;
        }
        </style>
        
		<title>学生选课管理系统</title>
	</head>
	
	<body>
		
		<?php include $_SERVER['DOCUMENT_ROOT']."/sems/share/header.php";?>
		<div class="mainblock">
		  <div class="mcontain">
                <div class="course">
                    <a id = "begin" href="scripts/showCourse.php">开始选课</a>
                    <a id = "selected" href="scripts/selectedCourse.php">已选课程</a> <br>
                </div>
                </br>
        
                <!--输入课程名，开始查询，可以删除、修改、更新--->
                <form action="scripts/queryCourse.php">
                    <input type="submit" value="课程查询">
                    课程号:<input type="text" name="courseName" value="课程1"><br>
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
		
            </div>
        </div>
	</body>
	
</html>
