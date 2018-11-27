<html>
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

    //$studentId = $_GET['studentId'];
    //echo $studentId."<br>";
    session_start();
    if(!isset($_SESSION['student_login_id'])){
        echo "您还未登录，请先登录";
        echo "<a href='../../student/student_login.html'>前往登陆</a>";
    }
    $studentId = $_SESSION['student_login_id'];
    
    $conn = new mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        die("Connect error: ". $conn->connect_error);
    }
    
    $sql = "SELECT * from tb_student WHERE StudentId=".$studentId."";
    $result = $conn->query($sql);
    if(count($result->fetch_array(MYSQLI_NUM))==0){
        echo "您还没注册，请先注册，再开始选课！<br>";
        echo "<a>前往注册</a><br>";
        $conn->close();
        return;
    }
    
    $sql = "SELECT CourseId from tb_stucourse WHERE StudentId=".$studentId."";
    $result = $conn->query($sql);
    //$courseId = $result->fetch_all(MYSQLI_NUM); //二维数组 N*1
    $dataAll = $result->fetch_all(MYSQLI_NUM);
    if (count($dataAll)==0){
        echo "您还没有选课记录！";
        return;
    }
    
    echo "<h2> ".$studentId."学生的选课表</h2>";
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
    
    $i = 0;
    while($i < count($dataAll)){
    $data = $dataAll[$i];
        //echo count($data), "<br>", $data[0], "<br>";
    $row = ($conn->query("SELECT * FROM tb_course WHERE CourseId=".$data[0].""))->fetch_array(MYSQLI_ASSOC);
    
    echo "<tr>";
    echo "<td><a href='deleteCourse.php?studentId=".$studentId."&&courseId=".$row['CourseId']."&&teacherId=".$row['TeacherId']."' >退课</a></td>";
    echo "<td>" . queryTeacherName($conn, $row['TeacherId']) . "</td>";
    echo "<td>" . $row['CourseId'] . "</td>";
    echo "<td>" . $row['CourseName'] . "</td>";
    echo "<td>" . $row['CourseCredit'] . "</td>";
    echo "<td>" . $row['CourseClass'] . "</td>";
    echo "<td>" . $row['Capacity'] . $row['Remain']. "</td>";
    echo "</tr>";
    
    $i ++;
    }
    echo "</table>";
    $conn->close();
?>

</body>
</html>
