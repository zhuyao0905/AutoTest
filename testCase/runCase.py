# runCase.py:运行测试用例（1）运行前会根据配置文件里面配置的是否清空前面的运行结果，如果配置是0，result下面就会保存每次的运行结果，如果配置为1，就会保存最后一次运行结果（就是运行前，把result里面的各个项下面的内容清空了）（2）运行前会去调用caseList.txt,如果里面带#的测试用例文件名称不执行（3）运行后，会自动生成html的报告，并跟进配置文件里面的邮箱配置发送测试结果文件，邮件函数具体编写，请参考我另一篇文章
