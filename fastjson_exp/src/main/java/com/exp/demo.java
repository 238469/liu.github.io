package com.exp;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.parser.Feature;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class demo {
    //fastjson提供了两个反序列化函数：parseObject和parse，我们通过示例程序来看一下fastjson的反序列化过程
    //toJSONString将对象转成字符串
    public static void main(String[] args) {
        Student student = new Student("moonsec" , 123);
        String jsonString1 = JSON.toJSONString(student);//是将对象转化为Json字符串
        System.out.println("转成json");
        System.out.println(jsonString1);
        System.out.println("转成json @type");
        String jsonString2 = JSON.toJSONString(student, SerializerFeature.WriteClassName); //自动加入 @type
        System.out.println(jsonString2);
        System.out.println("json转对象1");
        JSONObject jsonObject=JSON.parseObject(jsonString2);
        System.out.println(jsonObject);
        System.out.println("json转对象2");
        Student student1=JSON.parseObject(jsonString2,Student.class);
        System.out.println(student1);
        System.out.println("json转对象3");
        Object obj=JSON.parse(jsonString2);
        System.out.println(obj);

    }
}
