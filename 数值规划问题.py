# 整数规划
# import cvxpy as cp
# from numpy import array
# c=array([40,90])
# a=array([[9,7],[-7,-20]])
# b=array([56,-70])
# x=cp.Variable(2,integer=True)
# obj=cp.Minimize(c@x)# @是* 是用于矩阵的乘法符号
# cons=[a@x<=b,x>=0]
# prob=cp.Problem(obj,cons)
# prob.solve(solver='GLPK_MI',verbose=True)
# print("最优值为：",prob.value)
# print("最优解为：\n",x.value)

# 指派问题
# import cvxpy as cp
# import numpy as np
# c=np.array([[4,8,7,15,12],
#             [7,9,17,14,10],
#             [6,9,12,8,7],
#             [6,7,14,6,10],
#             [6,9,12,10,6]])
# x=cp.Variable((5,5),integer=True)
# obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
# con=[0<=x,x<=1,cp.sum(x,axis=0,keepdims=True)==1,
#      cp.sum(x,axis=1,keepdims=True)==1]
# prob=cp.Problem(obj,con)
# prob.solve(solver='GLPK_MI')
# print("最优值为：",prob.value)
# print("最优解为：",x.value)

# 指派问题 二元规划
# import pulp
#
#
# InvestLP = pulp.LpProblem("Invest decision problem", sense=pulp.LpMaximize)
# x1 = pulp.LpVariable('x1', cat='Binary')
# x2 = pulp.LpVariable('x2', cat='Binary')
# x3 = pulp.LpVariable('x3', cat='Binary')
# x4 = pulp.LpVariable('x4', cat='Binary')
# x5 = pulp.LpVariable('x5', cat='Binary')
#
# InvestLP += (150 * x1 + 210 * x2 + 60 * x3 + 80 * x4 + 180 * x5)
# InvestLP += (x1 + x2 + x3 == 1)
# InvestLP += (x3 + x4 == 1)
# InvestLP += (x5 - x1 <= 0)
# InvestLP.solve()
# print(InvestLP.name)
# print("Status youcans:", pulp.LpStatus[InvestLP.status])
# for v in InvestLP.variables():
#     print(v.name, "=", v.varValue)
# print("Max f(x) =", pulp.value(InvestLP.objective))