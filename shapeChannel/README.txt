解释：
用户划的样本点->sampleTranslation将其平移移动到原点处->
键盘上的几个键的坐标->keyboardTranslation将几个坐标转换为和样本点数目相等的点，并平移到原点处->

=>

shapeNormalizedDistance依据参数L将两组序列最长边变成等长的，然后计算距离

--------------------
main.py中两个序列值，sample为用户划的点，keyboard为某一单词的键盘键位坐标。例如若h<->(5, 2), i<->(4, 3)，则此时单词hi对应的keyboard序列为[[5,2],[4,3]]。
⚠️注意：所有序列值都是非负数！

在main.py中，手动更改两个序列值，与归一化时的共同长度L，命令行输入python main.py，main会调用调试用的getMyDistance函数，即可得到上述过程计算出的距离。
⚠️注意：序列值必须是float类型的。这一版本中，为了方便，在getMyDistance里添加了对序列的强制类型转换。

--------------------

by LiangCong