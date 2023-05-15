"""1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5] """

l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l2=[]
def flatten(l):
  for i in l:
    if isinstance(i,list):
      flatten(i)
    else:
      l2.append(i)
flatten(l)
print(l2)
"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]] """


l=[[1,2],[3,4],[5,6,7]]
l2=[]
def reverse(x):
  for i in l:
    i.reverse()
  l.reverse()
  return l
print(reverse(l))