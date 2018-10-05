<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/ html; charset=utf-8" />
	<title>students</title>
</head>
<body>
	<h2>学生选课管理系统</h2>
	<?php include($_SERVER['DOCUMENT_ROOT']."\\sems\\share\\header.php"); ?>
	<div>					
		<div class="mainblock">
			学号<input type="text" name="id" id="input_id">
			<button type="button" onclick="lookupOne();">查找</button>
			<table>
				<thead>
					<tr>
						<td>学号</td>
						<td>姓名</td>
						<td>性别</td>
						<td></td>
					</tr>
				</thead>
				<tbody id="student_table">
				</tbody>
			</table>
		</div>
	</div>
	<script>
		function infoToTbody(rst){
			var tmp;
			if(rst.studentGender=="1"){
				tmp="男";
			}else tmp="女";
			var tmp_str="<tr><td>"+rst.studentId+
				"</td><td>"+rst.studentName+
				"</td><td>"+tmp+"</td><td>"+
				"<a href='delete.php?id="+rst.studentId+
				"' onclick='return confirm(\"确认删除？\")'>删除"+
				"</a></td></tr>";
			//window.alert(tmp_str);
			return tmp_str;	
		}
		function lookupOne(){
			var xhr = new XMLHttpRequest;
			xhr.open('post', 'search.php');
			xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			var input_id = document.getElementById("input_id");
			xhr.send("id="+input_id.value);	

			xhr.onreadystatechange = function(){
				if(xhr.readyState == 4
					&& (xhr.status == 200 || xhr.status ==304)) {
					var rst = JSON.parse(xhr.responseText);
					var tb = document.getElementById("student_table");
					tb.innerHTML=infoToTbody(rst);
				}
			}
		}
		function lookupAll(){
			var xhr = new XMLHttpRequest;
			xhr.open('post', 'search_all.php');
			xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			xhr.send();
			xhr.onreadystatechange = function(){
				if(xhr.readyState == 4
					&& (xhr.status == 200 || xhr.status ==304)) {
					var rst = JSON.parse(xhr.responseText);
					var tb = document.getElementById("student_table");
					var info="";
					for(i in rst)
						info+=infoToTbody(rst[i]);
					//window.alert(info);
					tb.innerHTML=info;
				}
			}
		}
		lookupAll();
	</script>
</body>
