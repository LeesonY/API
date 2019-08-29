# def add(a,b,c,d,e):
#     s=a+b+c+d+e
#     return s
# print(add(1,2,3,4,5))

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 a=k*100+j*10+i
#                 print(a)

# def judge_len(*args):
#     for arg in args:
#         if isinstance(arg,str):
#             if len(arg)>5:
#                 print('参数:{},长度大于5'.format(arg))
#             else:
#                 print('参数:{},长度小于5'.format(arg))
#         elif isinstance(arg,list):
#             if len(arg)>5:
#                 print('参数:{},长度大于5'.format(arg))
#             else:
#                 print('参数:{},长度小于5'.format(arg))
#         elif isinstance(arg,tuple):
#             if len(arg)>5:
#                 print('参数:{},长度大于5'.format(arg))
#             else:
#                 print('参数:{},长度小于5'.format(arg))
#         else:
#             print('该函数不支持该{}类型的判断'.format(type(arg)))
# judge_len(1)



















