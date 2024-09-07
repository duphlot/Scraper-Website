
import numpy as np
import pandas as pd

books=pd.read_csv("Books.csv")
users=pd.read_csv("Users.csv")
ratings=pd.read_csv("Ratings.csv")

books.head() #in các dòng đầu

users.head()

ratings.head()

print(books.shape) #đếm số dòng, cột
print(users.shape)
print(ratings.shape)

books.isnull().sum() #kiểm tra ô ko có gtri

users.isnull().sum()

ratings.isnull().sum()

books.duplicated().sum() #kiểm tra trùng lặp

ratings.duplicated().sum()

users.duplicated().sum()

#popularity based recommend system

ratings_with_name=ratings.merge(books,on='ISBN') 
#gộp thông tin chi tiết của books và ratings

ratings_with_name

num_rating_df=ratings_with_name.groupby("Book-Title").count()['Book-Rating'].reset_index()
#gộp books giống nhau rồi đếm lượt ratings

num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace="True")
#đổi tên cột, sửa thẳng vào bảng gốc

num_rating_df

avg_rating_df=ratings_with_name.groupby("Book-Title").mean()['Book-Rating'].reset_index()
##gộp books giống nhau rồi tính avg ratings

avg_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace="True")

avg_rating_df

popular_df=num_rating_df.merge(avg_rating_df,on='Book-Title')
#gộp 2 bảng theo cột Book-Title
popular_df

popular_df=popular_df[popular_df["num_ratings_x"]>=250].sort_values("num_ratings_y",ascending=False).head(50)
#lấy các hàng có numx>=250 rồi sort giảm dần theo numy, in 50 dòng đầu

popular_df

popular_df.merge(books,on='Book-Title')

#collaborative filtering

x=ratings_with_name.groupby("User-ID").count()['Book-Rating']>200
#gộp userid giống nhau rồi xét lượt đếm ratings>200 lưu vào bảng x

userID_true=x[x].index
#lấy cột đầu các gtri true

filtered_ratings=ratings_with_name[ratings_with_name['User-ID'].isin(userID_true)]
#lấy các hàng của bảng ratings_with_name có gtri User-ID nằm trong userID-true lưu vào bảng mới

filtered_ratings

y=filtered_ratings.groupby('Book-Title').count()['Book-Rating']>=50
#gộp Book-Title giống nhau rồi xét lượt đếm ratings>=50 lưu vào bảng y
famous_book=y[y].index

final_ratings=filtered_ratings[filtered_ratings['Book-Title'].isin(famous_book)]
#lấy các hàng của bảng filtered_ratings có gtri User-ID nằm trong userID-true lưu vào bảng mới

pt=final_ratings.pivot_table(index="Book-Title",columns="User-ID",values="Book-Rating")
#biến bảng final_ratings thành dạng pivot_table với cột đầu là Book-Title, cái cột còn lại (hàng) 
#là ratings của từng userid trên mỗi sách (ô gtri) rồi lưu vào bảng pt

pt.fillna(0,inplace=True) #điền 0 vào các ô null trên bảng gốc
pt

from sklearn.metrics.pairwise import cosine_similarity
#trong pt một hàng là một dãy số (một vecto)
similarity_score=cosine_similarity(pt)
#biến bảng pt thành dạng cosin_similarity bằng cách tính độ tương tự giữa từng cặp vecto trong pt 
#(columns,rows=Book-Title, các ô là độ tương tự)
similarity_score.shape

def recommend(book_name):
  book_index=np.where(pt.index==book_name)[0][0]
  #tìm vị trí (có dạng mảng) trong index của pt có gtri==book_name (book_name là biến đầu vào), 
  #lấy ptu [0] của ptu [0] trong mảng vị trí ta được stt của book_name trong index pt, lưu vào book_index
  list_similarity=similarity_score[book_index]
  #stt vị trí trong pt cũng là trong similarity_score (bảng độ tương tự)
  #truy cập vào dòng thứ book_index của similarity_score, lưu các gtri vào list_similarity (dạng list)
  list_added_index=list(enumerate(list_similarity))
  #đánh stt từng ptu trong list được liệt kê ra, sau đó gom lại thành mảng gồm các list có dạng (stt,độ tương tự)
  book_similars=sorted(list_added_index,key=lambda x:x[1],reverse=True)
  #sort lại các list theo thứ tự giảm dần của ptu [1] trong mảng, lưu vào book_similars
  print(book_similars[1:5])
  for book in book_similars[1:5]:
  #bỏ ptu book_similars[0] vì trùng nhau
    print(book[0])
    #(là stt các book trong pt và similarity_score)
    print(pt.index[book[0]])
    #in gtri cột index thứ book[0] của pt 
  return book_similars[1:5]

