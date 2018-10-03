<html>
<body>
<?php

function updateCourseRemain($conn, $courseId, $value)
{
    $sql = "UPDATE tb_course SET Remain=".$value." WHERE CourseId=".$courseId."";
    if ($conn->query($sql)==False){
        echo "update error: ".$conn->error;
    }
    
}

    $studentId = $_GET['studentId'];
    $courseId = $_GET['courseId'];
    $teacherId = $_GET['teacherId'];
    
    $conn = new mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        die("Connect Errot: ".$conn->connect_error);
    }
    
    $sql = "DELETE FROM tb_stucourse WHERE StudentId=".$studentId." and CourseId=".$courseId." and TeacherId=".$teacherId."";
    if($conn->query($sql)==FALSE){
        echo "delete error: ".$conn->error;
    }else{
        echo "退课成功<br>";
        //更新课程信息
        $sql = "SELECT  Remain FROM tb_course WHERE CourseId=".$courseId."";
        $result = $conn->query($sql);
        if($result==True){
            $value  = $result->fetch_array(MYSQLI_NUM)[0];
            updateCourseRemain($conn, $courseId, $value-1);
        }
    }
    $conn->close();
    
?>

<!--<a href="javascript:" onclick="self.location=document.referrer;">返回上一页并刷新</a> -->

</body>
</html>

    
    