#1
np.zeros_like()

#2
# sort the results, highest prediction first
sorted_index = np.argsort(-y_pu,axis=0).reshape(-1).tolist()  #negate to get largest rating first

#3
#course 3 week 2 lab 2
m_dist = ma.masked_array(dist, mask=np.identity(dist.shape[0]))  # mask the diagonal
