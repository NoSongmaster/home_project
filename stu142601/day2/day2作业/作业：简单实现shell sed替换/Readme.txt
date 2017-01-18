作业：
简单实现shell sed替换功能。

[使用方法：python file_sed.py argv[1] argv[2] argv[3] ]

范例： python file_sed.py old_str new_str filename
注意：请切换到，程序文件所在目录执行。

利用文件操作,将file文件做一个备份file.old,然后根据file.old文件内容,
进行匹配替换,重新写回到file文件中.
利用try抓取异常：1、输入参数个数不满足3个，2、操作文件不存在。
				输出使用方法：
涉及文件：
		程序文件：file_sed.py
        源文件：test 	备份文件：test.old
