// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8;

contract Student_management{
    struct Student{
        int stud_ID;
        string Name;
        string department;
    }
    Student[] Students;
    function add_stud(int stud_ID,string memory Name, string memory department)public {
        Student memory stud = Student(stud_ID,Name,department);
        Students.push(stud);
    }
    function getStudent(int stud_ID)public view returns(string memory, string memory){
        for(uint i = 0; i<Students.length;i++){
            Student memory stud = Students[i];
            if(stud.stud_ID == stud_ID){
                return (stud.Name, stud.department);
            }
        }
        return ("Not Found", "Not Found");
    }
}