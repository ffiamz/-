<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" type="text/css" href="/sems/share/style.css"/>
	<title>学生选课管理系统</title>
</head>
	<?php include($_SERVER['DOCUMENT_ROOT']."\\sems\\share\\header.php"); ?>
	<div>					
	  <div class="mainblock">
		<div class="mcontain">
		  <form action="login.php" method="post"/>
		  学号<input type="text" name="id" ><br/>
		  密码<input type="password" name="password"/><br/>
		  <input type="submit" name="submit" value="提交"/>
		  </form>
		</div>
	  </div>
	</div>

</body>
