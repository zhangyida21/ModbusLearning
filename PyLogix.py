from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '192.168.2.110'
    # print(comm.GetModuleProperties(0))                            #获取设备信息
    # print(comm.GetPLCTime())                       #获取PLC时间
    # print(comm.GetProgramsList())                      #获取程序列表
    # print(comm.GetTagList())                          #获取所有Tag名称列表
    # for Tag in comm.GetTagList().Value:                   #遍历获取到的tag名称列表
    #
    #     print(Tag)
    # print(comm.GetProgramTagList('Program:Cell1'))             #获取指定Program范围内Tag名称列表
    # for Tag in comm.GetProgramTagList('Program:Armorstart_test').Value:                  #遍历获取到的tag名称列表
    #
    #     print(Tag)
    # print(comm.Read('Program:Cell1.AGVHeartBeatTimeOutAlarm'))                   #读取单个tag

    # tagList = [                                                                 ##读取多个tag组合的列表
    #     'Program:Cell1.zzAlarmTest.EnableIn',
    #     'Program:Cell1.zzAlarmTest.zzAlarmTest.In',
    #     'Program:Cell1.zzAlarmTest.zzAlarmTest.InFault',
    #     'Program:Cell1.zz_testAxisGapVelocity1'
    # ]
    #
    # responses = comm.Read(tagList)
    #
    # # 遍历每个响应
    # for response in responses:
    #     # 处理状态为成功的情况
    #     if response.Status == 'Success':
    #         # 如果是布尔值，将 True 转为 1，False 转为 0
    #         if isinstance(response.Value, bool):
    #             numeric_value = 1 if response.Value else 0
    #         # 如果是整数或浮点数，直接显示
    #         elif isinstance(response.Value, (int, float)):
    #             numeric_value = response.Value
    #         else:
    #             numeric_value = "Unknown Type"  # 如果有其他类型，可以显示为未知
    #
    #         print(f"Tag: {response.TagName}, Value: {numeric_value}, Status: {response.Status}")
    #
    #     else:
    #         # 处理路径未知或其他错误的情况
    #         print(f"Tag: {response.TagName}, Value: None, Status: {response.Status}")





    # comm.Write('Program:Cell1.zz_test3', 2)                   #写入单个数值










    # write_data = [('Program:Cell1.zz_test3', 10),                                              #同时写入多种数据类型的值
    #
    #               ('Program:Cell1.zz_test4', 3.5),
    #               ('Program:Cell1.zz_test5', 1)]
    # comm.Write(write_data)




    # comm.Write('Program:Cell1.zz_test4[0]',['123','456','789'])                       #写入数组数据






















