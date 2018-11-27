<html>
<head>
<meta charset="utf-8">
</head>

<body>

<?php 

function queryTeacherName($conn, $teacherId)
{
    //$studentId = $_GET['studentId'];
    //echo $studentId. '<br>';
    
    $sql = "SELECT TeacherName from tb_teacher where TeacherId=".$teacherId."";
    $result = $conn->query($sql);
    if($result==FALSE){
        echo "Connection error: ". $result;
    }
    
    $data = $result->fetch_array(MYSQLI_NUM);
    return $data[0];
}
  
    $courseId = $_GET['courseId'];
    $conn = new mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        echo "Connect error: ". $conn->connect_error. "<br>";
    }
    $sql = "SELECT * FROM tb_course WHERE CourseId=".$courseId."";
    $result=$conn->query($sql);
    $row = $result->fetch_array(MYSQLI_ASSOC);
    
    echo "<table border='1'>
    <tr>
    <th>TeacherName</th>
    <th>CourseId</th>
    <th>CourseName</th>
    <th>CourseCredit</th>
    <th>CourseClass</th>
    <th>Capatity/Remain</th>
    </tr>";
    
    echo "<tr>";
    echo "<td>" . queryTeacherName($conn, $row['TeacherId']) . "</td>";
    echo "<td>" . $row['CourseId'] . "</td>";
    echo "<td>" . $row['CourseName'] . "</td>";
    echo "<td>" . $row['CourseCredit'] . "</td>";
    echo "<td>" . $row['CourseClass'] . "</td>";
    echo "<td>" . $row['Capacity'] .'/'. $row['Remain'] .  "</td>";
    echo "</tr>";
    echo "</table>";
    
    $conn->close();
?>

<br>
<form action='modifyCapacity.php'>
<input type="hidden" name="courseId" value=<?php echo $row['CourseId']; ?> ><br>
容量/已选：<?php echo $row['Capacity']."/".$row['Remain']; ?>==>
修改容量：<input type="text" name="updateCourse" value=<?php echo $row['Capacity']; ?> > <br>
<input type="submit" value="提交"> 
</form>
注意：修改后的课程容量不能小于已选人数！<br>


</body>
</html>

    
    
