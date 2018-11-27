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

    $courseName = $_GET['courseName'];
    if($courseName==''){
        echo '';
        return ;
    }
    
    $conn = new mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        die("Connect error: ".$conn->connect_error);
    }
    $conn->set_charset("utf8");
    
    $sql = "SELECT * FROM tb_course WHERE CourseName='".$courseName."'";
    $result = $conn->query($sql);
    if($result==False){
        echo "Connect error: ".$conn->error;
        $conn->close();
        return;
    }
    $course = $result->fetch_all(MYSQLI_ASSOC);
    if(count($course)==0){
        echo "课程不存在<br>";
        $conn->close();
        return;
    }
    
    echo "<h2>".$courseName."的课程信息";
    
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
    
    foreach ($course as $row){ 
    //while($row=$result->fetch_array(MYSQLI_ASSOC)){
    echo "<tr>";
    echo "<td><a href='removeCourse.php?courseId=".$row['CourseId']."&&teacherId=".$row['TeacherId']."' >删除</a></td>";
    echo "<td>" . queryTeacherName($conn, $row['TeacherId']) . "</td>";
    echo "<td>" . $row['CourseId'] . "</td>";
    echo "<td>" . $row['CourseName'] . "</td>";
    echo "<td>" . $row['CourseCredit'] . "</td>";
    echo "<td>" . $row['CourseClass'] . "</td>";
    echo "<td>" . $row['Capacity'] .'/'. $row['Remain'] . "<a href='updateCapacity.php?courseId=".$row['CourseId']."' >修改</a></td>";
    echo "</tr>";
    }
    
    echo "</table>";
    
    $conn->close();
    
?>