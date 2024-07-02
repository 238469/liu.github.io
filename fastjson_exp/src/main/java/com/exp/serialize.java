package com.exp;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class serialize {
    public static void main(String[] args) {
        Student student = new Student("moonsec" , 123);
        String jsonString1 = JSON.toJSONString(student);//是将对象转化为Json字符串
        System.out.println(jsonString1);
        String jsonString2 = JSON.toJSONString(student, SerializerFeature.WriteClassName); //自动加入 @type
        System.out.println(jsonString2);
    }
}
