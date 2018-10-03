<?php
//从数据库中删除课程 tb_course tb_stucourse
    $courseId = $_GET['courseId'];
    $teacherId = $_GET['teacherId'];
    
    $conn = new mysqli("localhost", "root", "", "SEMS");
    if($conn->connect_error){
        die("Connect error: ". $conn->connect_error);
    }
    
    $sql = "DELETE FROM tb_course WHERE CourseId=".$courseId." and TeacherId=".$teacherId."";
    if($conn->query($sql)==False){
        echo "delete error: ". $conn->error ."<br>";
        $conn->close();
        return;
    }else{
        echo "从课程表中成功删除课程<br>";
    }
    $sql = "DELETE FROM tb_stucourse WHERE CourseId=".$courseId." and TeacherId=".$teacherId."";
    if($conn->query($sql)==False){
        echo "delete error: ". $conn->error ."<br>";
        $conn->close();
        return;
    }else{
        echo "从选课表中成功删除课程<br>";
    }
    
    $conn->close();
?>

    