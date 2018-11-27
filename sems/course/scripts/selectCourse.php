<!DOCTYPE HTML>
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

    $courseId = $_GET['courseId'];
    $studentId = $_GET['studentId'];
    $teacherId = $_GET['teacherId'];
    
    $conn = new  mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        die("Connect error: ". $conn->connect_error);
    }
    //echo $courseId . '<br>' . $studentId;
    $conn->set_charset("utf8");
    
    //插入学生选课表
    $sql="INSERT ignore INTO
    tb_stucourse(StudentId, CourseId, TeacherId)
    VALUES('".$studentId."', '".$courseId."', '".$teacherId."');";
    
    if($conn->query($sql)==FALSE){
        echo "Insert error: ". $conn->error."<br>";
        //$result = False;
    }else{
        echo "选课成功<br>";
        
        //更新剩余人数
        $sql = "SELECT Remain FROM tb_course WHERE CourseId=".$courseId."";
        $result=$conn->query($sql);
        $value = $result->fetch_array(MYSQLI_NUM)[0];
        updateCourseRemain($conn, $courseId, $value-1);
    
        //$result = True;
    }
    $conn->close();
    
?>
<!--<a href="javascript:" onclick="self.location=document.referrer;">返回上一页并刷新</a> -->

</body>

<html>

