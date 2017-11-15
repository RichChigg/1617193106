>>> y ='123 @ qq.comaaa @ 163.combbb @ 126.comasdfasfs33333 @ adfcom'
>>>导入重
>>> re.findall（'\ w + @（qq | 163 | 126）.com“之间，y）的
[ 'QQ'， '163'， '126']
>>> re.findall（'\ w + @（?: | qq | 163 | 126）.com“之间，y）的
[ '123@qq.com'， 'aaa@163.com'， 'bbb@126.com']
>>> 
>>> 
>>> y ='tel：010-12345678 address：changanRoad'
>>> re.findall（'\ d'，y）
[0,1,0,1,2,3,4,5,6,7,8]
>>> re.findall（'\ d +'，y）
[ '010'， '12345678']
>>> re.findall（'\ d +  - '，y）
['010-']
>>> re.findall（'\ d +  -  \ d +'，y）
['010-12345678']
>>> 
>>> 
>>> string =“abcdefg acbdgef abcdgfe cadbgfe”
>>>字符串
'abcdefg acbdgef abcdgfe cadbgfe'
>>> re.findall（'\ w'，string）
a，b，c，d，e，f，g，a，c，b，d，g，e'，'f'，'a'，'b'，'c'，'d' ，'f'，'e'，'c'，'a'，'d'，'b'，'g'，'f'，'e']
>>> re.findall（'\ w +'，string）
[ 'ABCDEFG'， 'acbdgef'， 'abcdgfe'， 'cadbgfe']
>>> 
>>> y ='123 @ qq.comaaa @ 163.combbb @ 126.comasdfasfs33333 @ adf.com'
>>> test_list = ['first'，'seconde']
>>> test_list
[ '第一'， 'Seconde系列']
>>> test_list [1]
'Seconde系列系列'
>>> test_list [0]
'第一'
>>>
>>>
>>> y ='localpath C：\ code \ cnkiCrawl'
>>>导入重
>>> re.findall（'[a-zA-Z]：\ S +'，y）
['C：\\代码\\ cnkiCrawl']
>>>
>>>
>>> y ='Hello Kitty Hello Hello Hello Kitty Hello Kitty'
>>> re.findall（'（？：Hello）{2}（？：Kitty）{2}'，y）
['Hello Hello Kitty Kitty'] 
>>>
>>>
>>> y ='aabaaabaaaab'
>>> re.findall（'a {，2} b'，y）
[ 'AAB'， 'AAB'， 'AAB']
>>> 