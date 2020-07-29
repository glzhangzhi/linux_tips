使用nohup可以让程序运行以后，断开ssh连接，程序不停止

nohup python3 test.py &

tail -f nohup.out

会默认将输出记录都同目录下的nohup.out文件中，可以在这里实时查看进度

jobs  # 查看当前有哪些nohup任务

bg %n  # 将某任务放到后台

fg %n  # 将某任务放到前台

ctrl + z  # 挂起当前任务

kill +PID  # 结束某任务

如果需要将当前运行的某程序放到后台，需要先ctrl + z挂起，然后bg