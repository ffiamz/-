<?php
    /*
    $courseId = $_POST['courseId'];
    $courseName = $_POST['courseName'];
    $teacherId = $_POST['teacherId'];
    $teacherName = $_POST['teacherName'];
    $courseCredit = $_POST['courseCredit'];
    $courseClass = $_POST['courseClass'];
    $capacity = $_POST['capacity'];
    */
    $courseId = $_POST['courseId'];
    $courseName = $_POST['courseName'];
    $teacherId = $_POST['teacherId'];
    $teacherName = $_POST['teacherName'];
    $teacherGender = $_POST['teacherGender'];
    $courseCredit = $_POST['courseCredit'];
    $courseClass = $_POST['courseClass'];
    $capacity = $_POST['capacity'];
    
    if($courseId=='' || $courseName=='' || $teacherId=='' || $teacherName=='' || $teacherGender=='' ||
    $courseClass=='' || $courseCredit=='' || $capacity==''){
        echo "不能有空字段!<br>";
        return;
    }
    
    $conn = new mysqli("localhost", "manager", "123xyz,", "SEMS");
    if($conn->connect_error){
        echo "Connection error: ".$conn->connect_error;
        return;
    }
    /*
    //判断是否有重复的课程
    $sql = "SELECT * FROM tb_course WHERE CourseId=".$courseId." and TeacherId=".$teacherId."";
    $result=$conn->query($sql);
    if(count($result->fetch_all())!=0){
        echo "课程已经存在，不可以重复添加！<br>";
        $conn->close();
        return;
    }
    */
    
    $sql = "INSERT IGNORE INTO
    tb_course(CourseId, CourseName, CourseCredit, CourseClass, Capacity, TeacherId, Remain)
    VALUES(".$courseId.", '".$courseName."', ".$courseCredit.", ".$courseClass.", ".$capacity.", ".$teacherId.", ".$capacity.");";
    if($conn->query($sql)==False){
        echo "插入失败！<br>". $conn->error;
        $conn->close();
        return;
    }
    $sql = "INSERT IGNORE INTO 
    tb_teacher(TeacherId, TeacherName, TeacherGender)
    VALUES(".$teacherId.", '".$teacherName."', '".$teacherGender."');";
    if($conn->query($sql)==False){
        echo "插入失败！<br>". $conn->error;
        $conn->close();
        return;
    }else{
        echo "插入成功！<br>";
    }
    $conn->close();
    
?>
