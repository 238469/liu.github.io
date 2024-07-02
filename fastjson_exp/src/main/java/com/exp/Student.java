package com.exp;

public class Student {

    private String name;
    private int age;

    public Student() {
        System.out.println(" method: Student() ");
    }

    public Student(String name , int age) {
        System.out.println(" method: Student(String name , int age) ");
        this.name = name;
        this.age = age;
    }

    public String getName() {
        System.out.println(" method: getName() ");
        return name;
    }

    public int getAge() {
        System.out.println(" method: getAge() ");
        return age;
    }



/*    public void setName(String name) {
        System.out.println(" method: setName() ");
        this.name = name;
    }*/

    public void setAge(int age) {
        System.out.println(" method setAge() ");
        this.age = age;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}