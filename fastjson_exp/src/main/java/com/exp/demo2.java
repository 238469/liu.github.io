package com.exp;


import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.parser.Feature;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class demo2 {
    public static void main(String[] args)  {
        Student student = new Student("moonsec" , 123);
        String jsonString1 = JSON.toJSONString(student);//是将对象转化为Json字符串
        System.out.println("序列化1");
        System.out.println(jsonString1);
        System.out.println("反序列化2 自动加入 @type");
        String jsonString2 = JSON.toJSONString(student, SerializerFeature.WriteClassName); //自动加入 @type
        System.out.println(jsonString2);
        System.out.println("反序列化1");
        JSONObject jsonObject=JSON.parseObject(jsonString2);
        System.out.println(jsonObject);
        System.out.println("反序列化2");
        String json1="{\"@type\":\"com.exp.Student\",\"age\":123,\"name\":\"moonsec\"}";
        Student student1=JSON.parseObject(json1,Student.class,Feature.SupportNonPublicField);
        System.out.println(student1);
        System.out.println("反序列化3");
        Object obj=JSON.parse(jsonString2,Feature.SupportNonPublicField);
        System.out.println(obj);

    }

}
