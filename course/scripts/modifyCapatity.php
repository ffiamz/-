<?php 
    $courseId = $_GET['courseId'];
    $update = $_GET['updateCourse'];
    
    $conn = new mysqli("localhost", "root", "", "SEMS");
    if($conn->connect_error){
        echo "Connect error: ". $conn->connect_error. "<br>";
    }
    $conn->set_charset("utf8");
    
    $sql = "SELECT Capatity, Remain FROM tb_course WHERE CourseId=".$courseId."";
    $result = $conn->query($sql);
    if($result==False){
        echo "查询容量失败<br>";
        $conn->close();
        return;
    }
    $data = $result->fetch_array(MYSQLI_NUM);
    $selected = $data[0] - $data[1];
    if($update < $selected){
        echo "课程容量不能小于已选人数<br>";
        $conn->close();
        return;
    }
    
    $sql = "UPDATE tb_course SET Capatity=".$update." WHERE CourseId=".$courseId."";
    if($conn->query($sql)==FALSE){
        echo "更新容量失败！<br>";
        $conn->close();
        return;
    }else{
        echo "更新容量成功！<br>";
    }
    $sql = "UPDATE tb_course SET Remain=".($update-$selected)." WHERE CourseId=".$courseId."";
    
    if($conn->query($sql)==FALSE){
        echo "更新剩余容量失败！<br>";
    }else{
        echo "更新剩余容量成功！<br>";
    }
    $conn->close();
?>