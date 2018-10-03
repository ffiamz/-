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
    
    $studentId = $_GET['studentId'];
    $conn = new mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        die("Connect error: ". $conn->connect_error);
    }
    $conn->set_charset("utf8"); //设置语言，防止出现中文乱码
    
    //判断是否存在学生ID
    $sql = "SELECT * from tb_student WHERE StudentId=".$studentId."";
    $result = $conn->query($sql);
    if(count($result->fetch_array(MYSQLI_NUM))==0){
        echo "您还没注册，请先注册，在开始选课！<br>";
        echo "<a href='../../student/student_add.html'>前往注册</a><br>";
        $conn->close();
        return;
    }
    //echo count($result->fetch_array(MYSQLI_NUM))." <br>";
    
    $sql = "SELECT * FROM tb_course";
    $result = $conn->query($sql);
    
    echo "<h2>您好！".$studentId."可以开始选课啦";
    
    echo "<table border='1'>
    <tr>
    <th></th>
    <th>TeacherName</th>
    <th>CourseId</th>
    <th>CourseName</th>
    <th>CourseCredit</th>
    <th>CourseClass</th>
    <th>Capacity/Remain</th>
    </tr>";
    
    while($row = $result->fetch_array(MYSQLI_ASSOC)){
    echo "<tr>";
    echo "<td><a href='selectCourse.php?studentId=".$studentId."&&courseId=".$row['CourseId']."&&teacherId=".$row['TeacherId']."' >选课</a></td>";
    echo "<td>" . queryTeacherName($conn, $row['TeacherId']) . "</td>";
    echo "<td>" . $row['CourseId'] . "</td>";
    echo "<td>" . $row['CourseName'] . "</td>";
    echo "<td>" . $row['CourseCredit'] . "</td>";
    echo "<td>" . $row['CourseClass'] . "</td>";
    echo "<td>" . $row['Capatity'] .'/'. $row['Remain'] .  "</td>";
    echo "</tr>";
    }
    echo "</table>";
    
    $conn->close();
    
?>