# ！/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
正则化模块
'''

import re

# 顿号字符切割


def split_text(text):

    split_text = re.split('、', text)

    return split_text
# 当事人

def get_Prosecutor(text):
    pattern = re.compile("公诉机关(.+?)。")
    Prosecutor = pattern.findall(text)
    return Prosecutor

def get_province(text):

    pattern = re.compile('北京市|天津市|上海市|重庆市|河北省|山西省|辽宁省|吉林省|'
                                  '黑龙江省|江苏省|浙江省|安徽省|福建省|江西省|山东省|河南省|'
                                  '湖北省|湖南省|广东省|海南省|四川省|贵州省|云南省|陕西省|'
                                  '甘肃省|青海省|台湾省|内蒙古自治区|广西壮族自治区|西藏自治区|'
                                  '宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区')
    province = pattern.findall(text)
    return province

def get_reasons(text):
    pattern = re.compile('^为了感谢[\u4e00-\u9fa5"“”（）’‘]+(?=[,，。、；;])|'
                         '帮助[\u4e00-\u9fa5"“”（）’‘]+[,，。、；;]|'
                         '以[\u4e00-\u9fa5"“”（）’‘]+为[\u4e00-\u9fa5]+(?=[,，。、；;])|'
                         '为[\u4e00-\u9fa5"“”（）’‘]+(?=[,，。、；;])|'
                         '(?<=[,，。、；;])[\u4e00-\u9fa5"“”（）’‘]+提供帮助|'
                         '[\u4e00-\u9fa5"“”（）’‘]+提供帮助|'
                         '[\u4e00-\u9fa5"“”（）’‘]+给予帮助|'
                         '[\u4e00-\u9fa5"“”（）’‘]+关照|'
                         '[\u4e00-\u9fa5"“”（）’‘]+提供[\u4e00-\u9fa5"“”（）’‘]+帮助|'
                         '[\u4e00-\u9fa5"“”（）’‘]+给予[\u4e00-\u9fa5"“”（）’‘]+帮助')
    reasons = pattern.findall(text)
    return reasons

def get_accused_person(text):
    accused = re.search('被告人|上诉人|上诉者|（上诉者）', text, re.M | re.I)
    if accused:

        pattern = re.compile(
                             '(?<=被告人|上诉人)[\u4e00-\u9fa5]某[甲乙丙丁一二三123*]|'
                             '(?<=被告人|上诉人)[\u4e00-\u9fa5]某{1,2}|'
                             '(?<=被告人|上诉人)[\u4e00-\u9fa5]{2,3}、[\u4e00-\u9fa5]{2,3}、[\u4e00-\u9fa5]{2,3}、[\u4e00-\u9fa5]{2,3}|'
                             '(?<=被告人|上诉人)[\u4e00-\u9fa5]{2,3}、[\u4e00-\u9fa5]{2,3}、[\u4e00-\u9fa5]{2,3}|'
                             '(?<=被告人|上诉人)[\u4e00-\u9fa5]{2,3}、[\u4e00-\u9fa5]{2,3}|'
                             '(?<=被告人|上诉人)[\u4e00-\u9fa5]{2,3}')
        accused_person = pattern.findall(text)
        temp = []
        for person in accused_person:
            flag = re.match('[赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严'
                            '华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花'
                            '方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时'
                            '傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明'
                            '臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄'
                            '危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢'
                            '莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢'
                            '滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴'
                            '弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符'
                            '刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲台从鄂索咸籍赖卓蔺屠'
                            '蒙池乔阴胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂'
                            '濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容'
                            '向古易慎戈廖庚终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利'
                            '蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰'
                            '巢关蒯相查后荆红游竺权逯盖益覃]',person, re.M | re.I)
            if flag:
                if len(person) < 4:
                    ex = 0
                    for p in temp:
                        if p == person:
                            ex = 1
                            break
                    if ex == 0:
                        temp.append(person)
                else:
                    person = str(person).split('、')
                    for per in person:
                        ex = 0
                        for p in temp:
                            if p == per:
                                ex = 1
                                break
                        if ex == 0:
                            temp.append(per)
        accused_person = temp
    else:
        accused_person = []
    return accused_person

def get_briber(text, accused_names, name_list):
    my_name_list =''
    for s in name_list:
        my_name_list = my_name_list + str(s) + '|'
    my_name_list = my_name_list[0:my_name_list.__len__()- 1]
    send = re.compile('((?<!退还|退出|返还)(?<!退还所|退出所|返还所|退还其|退出其|返还其))'
                     '(贿送|送给|赠送|给予|拿给|收受|接受|交给|获得|转交|赠予|交付|存入|给|索要|索取|索求|收|收取)')
    send_word = send.findall(text)
    # # left = ['贿送', '送给', '赠送', '给予', '拿给', '交给', '转交', '赠予', '交付', '存入', '给']
    # right = ['收受', '接受', '获得', '索要', '索取', '索求','收','收取']
    if send_word:
        pattern = re.compile('[\u4e00-\u9fa5]某[甲乙丙丁一二三123*]|'
                             '[\u4e00-\u9fa5]某{1,2}|' + my_name_list)
        bribers = pattern.findall(text)
        if bribers == []:
            pattern = re.compile('[\u4e00-\u9fa5]{2,3}(?=为了感谢)')
            bribers = pattern.findall(text)
    else:
        bribers = []
    briber = []
    for name in bribers:
        if name not in accused_names and name not in briber:
            if name.__len__() == 3:
                if re.compile('[\u4e00-\u9fa5]{3}').findall(name):
                    briber.append(name)
            elif name.__len__() == 4:
                if re.compile('[\u4e00-\u9fa5]{4}').findall(name):
                    briber.append(name)
            elif name.__len__() == 2:
                if re.compile('[\u4e00-\u9fa5]{2}').findall(name):
                    briber.append(name)
    return briber

def get_gender(text):

    # pattern = re.compile('，男，|，男。|,男,|，女，|，女。|,女,')
    pattern = re.compile('[男女]')
    gender = pattern.findall(text)
    return gender

def get_born_date(text):
    pattern = re.compile('([\d]{4}年[\d]+月[\d]+日)出生')
    born_date = pattern.findall(text)
    return born_date

def get_birth_place(text):
    pattern = re.compile(r'，([\u4e00-\u9fa5]{2,20})人，|生[于地](.+?)，|住([\u4e00-\u9fa5]{2,20})。、')
    birth_place = pattern.findall(text)
    for (x, y, z) in birth_place:
        return x+y+z

def get_people(text):
    pattern = re.compile('，(汉族|蒙古族|回族|藏族|维吾尔族|苗族|彝族|壮族|布依族'
                                '|朝鲜族|满族|侗族|瑶族|白族|土家族|哈尼族|哈萨克族'
                                '|傣族|黎族|僳僳族|佤族|畲族|高山族|拉祜族|水族|东乡族'
                                '|纳西族|景颇族|柯尔克孜族|土族|达斡尔族|仫佬族|羌族'
                                '|布朗族|撒拉族|毛南族|仡佬族|锡伯族|阿昌族|普米族'
                                '|塔吉克族|怒族|乌孜别克族|俄罗斯族|鄂温克族|德昂族'
                                '|保安族|裕固族|京族|塔塔尔族|独龙族|鄂伦春族|赫哲族'
                                '|门巴族|珞巴族|基诺族)，')

    people = pattern.findall(text)
    return people

def get_edu_level(text):

    pattern = re.compile('，(博士|研究生文化|硕士|大学文化|本科文化|文化程度大学|文化程度本科|'
                            '大学本科|大专文化|文化程度大专|中专文化|文化程度中专|专科文化|'
                            '高中文化|文化程度高中|初中文化|文化程度初中|小学文化|文化程度小学|农民)，')
    edu_level = pattern.findall(text)
    return edu_level

def get_lawyer(text):

    # pattern = re.compile('辩护人.{1,4}，|辩护人.{1,4}、.{0,4}，|辩护人.{1,4}、.{0,4}、.{0,4}，')
    pattern = re.compile('辩护人(.+?)，')

    lawyer = pattern.findall(text)
    return lawyer

def get_law_firm(text):

    pattern = re.compile('[\u4e00-\u9fa5]{1,20}律师事务所|[\u4e00-\u9fa5]{1,20}援助中心律师')
    law_firm = pattern.findall(text)

    return law_firm

# 庭审程序说明
def get_Court_proceedings_time(text):
    pattern =  re.compile('于(.+?)[作向以]')
    Court_proceedings_time = pattern.findall(text)
    return Court_proceedings_time

# 庭审过程
def get_date(text):
    # pattern = re.compile('\d{4}年\d{1,2}月至\d{4}年\d{1,2}月|\d{4}年\d{1,2}月|\d{4}年\d{1,2}、\d{1,2}月|\d{4}年')
    pattern = re.compile(
    '''
    [0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{1,2}月、{0,1}[0-9零一二三四五六七八九元]{0,2}月{0,1}至[0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{1,2}月、{0,1}[0-9零一二三四五六七八九元]{0,2}月{0,1}|
    [0-9零一二三四五六七八九元]{4}年、[0-9零一二三四五六七八九元]{4}年|
    [0-9零一二三四五六七八九元]{4}年至[0-9零一二三四五六七八九元]{4}年|
    [0-9零一二三四五六七八九元]{4}年、[0-9零一二三四五六七八九元]{4}年、[0-9零一二三四五六七八九元]{4}年|
    [0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{1,2}月至[0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{1,2}月|  # year-month
    [0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{0,2}月{0,1}至[0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{0,2}月{0,1}|                    # year
    [0-9零一二三四五六七八九元]{4}年[0-9零一二三四五六七八九元]{0,2}月{0,1}[0-9零一二三四五六七八九元]{0,2}[号日]{0,1}
 
    ''',
    re.VERBOSE)
    '''
    pattern = re.compile(
     ([0-9零一二三四五六七八九元]+年)?([0-9零一二三四五六七八九元]+月)?([0-9零一二三四五六七八九元]+[号日])?|
     ([0-9零一二三四五六七八九元]+年)?([0-9零一二三四五六七八九元]+月)?([0-9零一二三四五六七八九元]+[号日])?至
     ([0-9零一二三四五六七八九元]+年)?([0-9零一二三四五六七八九元]+月)?([0-9零一二三四五六七八九元]+[号日])?
    )
    '''
    result = pattern.findall(text)
    return result

def get_money_number(text):
    pattern = re.compile('\d{1,20}.{0,1}\d{0,5}万{0,1}元(?![\u4e00-\u9fa5]{0,20}退还|[\u4e00-\u9fa5]{0,20}还给|[\u4e00-\u9fa5]{0,20}返还|[\u4e00-\u9fa5]{0,20}退给)')
    result = pattern.findall(text)
    return result

# 判决结果
def get_judgment_result(text):

    pattern = re.compile('判决如下.+|裁定如下:.+|判处如下.+|判决:.+|'
                                        '如下判决:.+|判决书如下:.+|判决意见如下:.+|决定如下:.+')

    judgment_result = pattern.findall(text)

    return  judgment_result

def get_legal_basis(text):

    pattern = re.compile(r'依照(.+?)[之的]规定')

    legal_basis = pattern.findall(text)

    return legal_basis

def get_is_surrendere(text):

    pattern = re.compile('认定自首|处理自首')

    legal_basis = pattern.findall(text)

    return legal_basis

def get_accusation(text):

    pattern = re.compile('贪污罪|挪用公款罪|受贿罪|单位受贿罪|行贿罪|对单位行贿罪|介绍贿赂罪|单位行贿罪|巨额财产来源不明罪|隐瞒境外存款罪|私分国有资产罪|私分罚没财物罪')
    accusation = pattern.findall(text)
    return accusation

def get_court_opinion(text):
    pattern = re.compile('原判决{0,1}(.+?)。')
    court_opinion = pattern.findall(text)
    return court_opinion

def exit(text):
    pattern = re.compile('触犯')
    exit = pattern.findall(text)
    return exit

def get_industry(text, industry):
    pattern = re.compile('粮食|豆类|蔬菜|水果|坚果|杂果|干果|咖啡|可可|棉类|麻类|油|果仁|籽|食用菌|烟草|花木|竹木|干草|木炭|植物提取物|动物提取物|动植物油|动植物种苗|家禽|牲畜|养殖动物|蚕茧|蚕丝|羽毛|羽绒|羊绒|生皮|毛皮|动物|肠衣|禽蛋|饲料|肥料|农药|园艺用具|农用品|农用机械|林业设备及用具|畜牧养殖|渔业|粮油|屠宰|农副产品|木材|家具')
    if pattern.findall(text) and '农林牧渔' not in industry:
        industry.append('农林牧渔')

    pattern = re.compile('保健用品|减肥增重|保养|药|康复|制药设备|医疗器械|计生|医保|医|治疗')
    if pattern.findall(text) and '医药卫生' not in industry:
        industry.append('医药卫生')

    pattern = re.compile('国土|房地产|市政工程|市政道路建设|市政公用设施|自来水|供暖|供热|供气|文教|卫生|体育|音乐|建筑设施|建筑工程|木材|石材|石料|水泥|石灰|石膏|混凝土|建筑玻璃|陶瓷|搪瓷|塑料建材|金属建材|防水|防潮材料|耐火|防火材料|隔热|吸声材料|绝缘材料|特种建材|施工材料|砖|瓦及砌块|墙体材料|天花板|地板|门窗|壁纸|锁具|建筑装饰|五金|管件管材|厨房设施|卫浴设施|涂料|'
                        '胶粘剂|作业保护|活动房|堆垛搬运机械|建筑|木工机械设备|加工机械|工程承包|建筑装璜设计|城建')
    if pattern.findall(text) and '建筑建材' not in industry:
        industry.append('建筑建材')

    pattern = re.compile('金属矿产|有色金属|有色金属制品|有色金属合金|有色金属合金制品|稀土及稀土制品|黑色金属及制品|铁合金及制品|钢铁及制品|铸锻件|金属丝网|粉末冶金|磁性材料|废金属|非金属矿产|非金属矿物制品|石墨及碳素产品|矿业设备 |冶金设备|金属线|金属管|金属板|冶炼加工')
    if pattern.findall(text) and '冶金矿产' not in industry:
        industry.append('冶金矿产')

    pattern = re.compile('石油及制品|煤矿|天然气|煤气|矿业|石油|化工|有机|无机|树脂|聚合物|化学纤维|食品添加剂|饲料添加剂|化学试剂|催化剂|化学助剂|日用化学品|香料|香精|染料|颜料|涂料|胶粘剂|火工产品|油墨|塑料及制品|橡胶及制品|玻璃及制品|实验室用品|仪器|仪表|塑料生产加工机械|橡胶生产加工机械|玻璃生产加工机械|化工设备|化工废料|化工产品设计加工')
    if pattern.findall(text) and '石油化工' not in industry:
        industry.append('石油化工')

    pattern = re.compile('水利|火力|发电|防洪|河道|疏浚|大坝|水库|闸门|泻洪工程|农田水利工程|江河|湖泊|治理工程|电力工程|电力|太阳能|再生能源|其他水利水电设备|其他水利水电设施 ')
    if pattern.findall(text) and '水力水电' not in industry:
        industry.append('水力水电')

    pattern = re.compile('软件|数字|科技|计算机|消耗品|插卡类|主机|电脑外设|机箱|UPS|电源|网络设备|配件|电脑|电子|笔记本电脑|服务器|工作站|电池|磁卡|IP卡|IC卡|来电显示器|拨号器|充电器|天线|控制和调整设备|电话机|可视电话|移动电话|集团电话|交换机|传真机|寻呼机|对讲机|网络通信产品|通讯|声讯系统|GPS系统|通信电缆|雷达及无线导航|广电|电信设备|系统工程|网络工程')
    if pattern.findall(text) and '信息产业' not in industry:
        industry.append('信息产业')

    pattern = re.compile('机械|仪器|仪表|磨具|磨料|零部件|焊接|切割|五金|气动|电动|减速机|变速机|泵|真空|液压机|风机|排风设备|压缩|分离设备|工控设备|换热|制冷|空调|发电机|发电机组|内燃机|节能装置|电线电缆|机械设计加工|家电制造设备|量器量具')
    if pattern.findall(text) and '机械机电' not in industry:
        industry.append('机械机电')

    pattern = re.compile('饮料|酒类|茶叶及制品|咖啡|可可及制品|水产及制品|禽畜肉及制品|罐头食品|速冻食品|方便食品|休闲食品|豆制品|蛋制品|蜜制品|乳制品|糖类|淀粉|食用油|调味品|糕饼面包|面条|粉丝|香烟|食品添加剂|食品饮料加工|食品饮料原料')
    if pattern.findall(text) and '轻工食品' not in industry:
        industry.append('轻工食品')

    pattern = re.compile('服饰|服装辅料|帽子|领带|围巾|头巾|手套|袜子|鞋及鞋材|针织服装|梭织服装|品牌服装|男装|女装|婴儿服装|儿童服装|内衣|睡衣|浴衣|T恤|衬衣|毛衣|西服|夹克|外衣|外套|大衣|风衣|裤子|休闲服装|运动服装|民族服装|婚纱|礼服|工作服|制服|特制服装|牛仔服装|丝绸服装|皮革|毛皮服装|羊毛|羊绒衫|羽绒服装|防寒服|服装加工设备|整熨洗涤设备|鞋加工及修理设备|服饰鞋帽设计加工|皮革加工机械|纺织废料|皮革废料|纺织品设计加工|皮革及制品设计加工|皮革原料|纱线|线|纺织辅料|棉织物|麻织物|丝织物|毛织物|化纤织物|混纺织物|坯布|色织|扎染|印花布|针织布|工业用布|无纺布|面料|抽纱|及其他工艺纺织|地毯|毛巾|浴巾|床上用品|家用纺织|皮革及人造皮革|皮革制品')
    if pattern.findall(text) and '服装纺织' not in industry:
        industry.append('服装纺织')

    pattern = re.compile('不干胶制品|广告材料|印刷出版物|音像制品及电子读物|广播|电视节目|排版|制版设备|印刷设备|二手印刷设备|印刷出版服|媒体和传播|专业咨询|信息技术|信息管理软件开发设计|维修|保险|租赁|会议|培训|物业管理')
    if pattern.findall(text) and '专业服务' not in industry:
        industry.append('专业服务')

    pattern = re.compile('锁具|保险柜|门铃|可视门铃|防盗|报警装置|监视|监控设备|避雷产品|防弹器材|防暴器材|防身用具|军需用品|救生器材|消防器材|作业保护器材|交通安全|运动护具|保安设备|警用设备|及紧急服务')
    if pattern.findall(text) and '安全防护' not in industry:
        industry.append('安全防护')

    pattern = re.compile('环境|废金属处理|纺织废料处理|皮革废料及处理|化工废料及处理|废气处理|水|污水处理|废料回收再利用|降噪音设备|公共环卫|公共环卫机械|园林绿化用品及机械|园林绿化|垃圾处理|荒山绿化|天然林保护|防沙')
    if pattern.findall(text) and '环保绿化' not in industry:
        industry.append('环保绿化')

    pattern = re.compile('旅游|宾馆|酒店|宠物|纪念品|扑克|棋类|乐器|钓鱼|健身|游艺设施|旅行')
    if pattern.findall(text) and '旅游休闲' not in industry:
        industry.append('旅游休闲')

    pattern = re.compile('图书资料|光学及照相器材|耗材|文具|计算器|办公纸张|簿|本|册|信封|档案夹|软盘|硒鼓|墨盒|墨粉|色带|教学模型|教学设施|实验室用品|电话机|可视电话|集团电话|传真机|复印机|打印机|打字机|投影机|碎纸机|考勤机|绘图机|晒图机|视讯会议系统|文艺设备|舞台|音响设备|摄影器材|录像设备|艺术')
    if pattern.findall(text) and '办公文教' not in industry:
        industry.append('办公文教')

    pattern = re.compile('磁性|半导体|绝缘|电工陶瓷|电子元器件、组件|电池|照明与灯具|插头|插座|充电器|电动机|电动工具|光电子|激光仪器 仪器|仪表|光仪|电线电缆|配电装置|开关柜|照明箱|输电设备及|显示设备|电热设备|工业自动化装置|地震设备|天线|雷达及无线导航|广电|电信设备|电子电工产品制造设备|电子电工产品设计加工')
    if pattern.findall(text) and '电子电工' not in industry:
        industry.append('电子电工')

    pattern = re.compile('木制玩具|塑料玩具|填充|绒毛玩具|电子玩具|电动玩具|玩具珠|球|娃娃|玩具车|玩具枪|模型玩具|益智玩具|童车及配件|玩具配件|工美礼品玩具设计加工|其他抽纱及其他工艺纺织|木制|植物编织|石料|宝石玉石|陶瓷工艺品|金属工艺品|玻璃工艺品|水晶工艺品|塑料工艺品|树脂工艺品|泥塑工艺品|纸制工艺品|天然|针钩及编结|雕刻|仿古|仿生|宗教|民间|雕塑|字画|古董和收藏品|珠宝首饰|金银器|时尚饰品|打火机|烟具|钟表|相框|画框|蜡烛及烛台|熏香及熏香炉|装饰盒|钥匙扣|链|盆景|玩具|工艺礼品|纪念品|广告礼品|节日用品|殡葬用品|工美礼品、玩具设计加工')
    if pattern.findall(text) and '玩具礼品' not in industry:
        industry.append('玩具礼品')

    pattern = re.compile('家用电器|家用电脑|家用空调|家用电视机|净水器|饮水机|榨汁机|搅拌机|咖啡机|豆浆机|电热壶|电热杯|电炒锅|电饭煲|微波炉|洗碗机|消毒柜|抽油烟机|冰箱|冷柜|湿度调节器|空气净化器|取暖电器|热水器|电吹风|吸尘器|电扇|排气扇|电熨斗|洗衣机|干衣设备|干手机|给皂液机|氧气机|电驱虫器|视听器材|遥控器|家用纸品|家用塑料制品|家用玻璃制品|家用陶瓷|搪瓷制品|家用金属制品|时尚饰品|珠宝首饰|金银器|打火机|烟具|钟表|相框|画框|熏香及熏香炉|个人保养、日用化学品|餐具|炊具厨具|保温容器|厨房设施|卫浴设施|清洁用具|园艺用具|家具|童车及配件|箱|包|袋|伞|雨具|太阳伞|刀|剪|刷|缝纫编织|婴儿用品|定时器|宠物及用品|门铃|可视门铃|照明与灯具')
    if pattern.findall(text) and '家居用品' not in industry:
        industry.append('家居用品')

    pattern = re.compile('救灾物资|防汛物资|抗旱物资|农用专用物资|储备物资|燃料|锅炉|供热设备|殡仪火化设备|其他物资；劳保用品|兽医用品')
    if pattern.findall(text) and '物资专才' not in industry:
        industry.append('物资专材')

    pattern = re.compile('体育器材|体育场馆专用材料|体育场馆建设|康复器械|比赛服装|体育设施')
    if pattern.findall(text) and '体育用品' not in industry:
        industry.append('体育用品')

    return industry
if __name__ == '__main__':
    print('This is regex fuctions for openlaw!')

