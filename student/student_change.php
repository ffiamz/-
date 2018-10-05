<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" type="text/css" href="/sems/share/style.css"/>
	<title>学生选课管理系统</title>
</head>
<body>
	<?php include($_SERVER['DOCUMENT_ROOT']."\\sems\\share\\header.php"); ?>
	<div>					
		<div class="mainblock">
		  <div class="mcontain">
			<form action="change.php" method="post">
				姓名<input type="text" name="name"><br/>
				男<input type="radio" checked="checked" name="gender" value="1"/>
				女<input type="radio" name="gender" value="0" /><br/>
				<input type="submit" value="提交">
			</form>
		</div>
		</div>
	</div>

</body>
