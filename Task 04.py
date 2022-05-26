import numpy as np

# a = np.array([[1, 2, 3, 4], [1, 2, 3, 4, 5]])
# a = np.array([[[1, 2, 3], [4, 5, 6]],[['a', 'b', 'c'], ['d', 'e', 'f']]])
# print(a.ndim)
# print(a)
# print("\n",a[0,0:2,1:2])
# print(a[0,1:2])
# print(type(a),"\n")
# print(a.dtype)

# for i in a:
# 	for j in i:
# 		for k in j:
# 			print(k)


# l1 = [[1,2.3,5],[4.6,8.4,7.9]]
# b = np.array(l1)
# print(b)
# print(b.dtype)
# c = np.array(l1,dtype="i")
# print(c)
# print(c.dtype)

# l2 = [ "22-06-03","3-07-07","4-08-10"]
# d = np.array(l2,dtype="M")
# print(d)
# print(d.dtype)


# l3 = [1,2,3,4,5,6]
# e = np.array(l3)
# print(e)
# view_e = e.view()
# copy_e = e.copy()

# view_e[2] = 10
# copy_e[0] = 25
# print("\n",e)
# print(view_e)
# print(copy_e,"\n\n")


# print(view_e.base)
# print(copy_e.base)


# f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(f.shape)
# f_new = f.reshape(2, 2,3)
# print(f_new)
# print(f_new.ndim)

# g = np.array([[[1, 2, 3], [4, 5, 6]],[['a', 'b', 'c'], ['d', 'e', 'f']]])

# for i in np.nditer(g[:,::2,::2]):
# 	print(i)

# h = np.array([[[1,2,3],[4,5,6]]])

# for i in np.ndenumerate(h):
# 	print(i)

# i = np.array([[[1,2],[3,4]]])
# j = np.array([[['a','b','ab'],['c','d','cd']]])
# print(i.shape)
# print(j.shape)

# join_i_j = np.concatenate((i,j),axis=3)
# print(join_i_j)
# print(join_i_j.shape)

# k = np.array([[1,2],[3,4]])
# l = np.array([['a','b'],['c','d']])
# print(k.shape)
# print(l.shape)

# join_k_l = np.stack((k,l),axis=1)
# print(np.concatenate((k,l),axis=1))
# print(join_k_l)
# print(join_k_l.shape)

# m = np.array([[[1,2,3,4],[4,5,6,8]],[[7,8,9,15],[10,11,12,38]]])
# split_m = np.array_split(m,3,axis=2)
# print(split_m)


# n = np.array([1,3,5,8,10,1])
# search_n = np.where(n%3==0)
# print(search_n)

# searchsorted_n = np.searchsorted(n,[2,7],side='right')
# print(searchsorted_n)

# o = np.array([[[9,0,5,4,8],[7,1,0,3,6]],[['a','z','d','e','q'],['q','z','y','j','x']]])
# sort_o = np.sort(o)
# print(sort_o)

p = np.array([1,2,3,4,5,6,7,8,9,10])
filter_p = p % 3 ==0
print(p[filter_p])