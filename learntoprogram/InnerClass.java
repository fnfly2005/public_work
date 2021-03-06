/**
* Description: 内部类、静态内部类、局部内部类、匿名内部类
*/

class Outer
{
    int x = 4;
    class Inner
    {
        int y = 5;
        void show()
        {
            int z = 6;
            System.out.println("show...innershowvalue" + z);//默认优先采用局部变量
            System.out.println("show...innervalue" + this.y);//其次向上搜索类成员变量
            System.out.println("show...outervalue" + Outer.this.x);//再向上搜索外部类的成员变量，内部类持有外部类的引用,Outer.this可省略
        }
    }

    static class InnerStatic //静态内部类
    {
        void show()
        {
            System.out.println("show...static");
        }
    }

    void method(final int x) //局部内部类引用局部变量应添加final关键字
    {
        class InnerLocal//局部内部类只能在局部函数中使用
        {
            void show()
            {
                System.out.println("show...InnerLocal" + x + Outer.this.x);
            }
        }
        InnerLocal il = new InnerLocal();
        il.show();
    }

}

interface innerDemo
{
    public void show1();
    public void show2();
}

class InnerClass
{
    public static void main(String [] args)
    {
        //普通内部类初始化需要两步
        Outer o = new Outer();
        Outer.Inner i = o.new Inner();
        i.show();    

        //静态内部类可以单独初始化,但不能访问非静态资源
        Outer.InnerStatic si = new Outer.InnerStatic();
        si.show();

        o.method(10);

        //匿名内部类必须是另一个类或接口的子类,向上转型后只能使用父类方法
        innerDemo l = new innerDemo(){
            int x = 11;
            public void show1()
            {
                System.out.println("anonymous...class...run");
            }
            public void show2()
            {
                System.out.println("anonymous...class...run" + x);
            }
        };

        l.show1();
        l.show2();
    }
}
