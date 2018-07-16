import tensorflow as tf 
import random


class DiziVerisi():

	def __init__(self,boyut=1000,max_uzunluk=20,min_uzunluk=3,max_deger=1000):
		self.data , self.labels , self.seqlen= [] , [] , []
		for i in range(boyut):
			"""
				1000 tane 3 ile 20 arasında dizi boyutu
				oluşturuldu. Bu boyutlar dizileri tanımlamak
				için kullanılacak
			"""
			len_ = random.randint(min_uzunluk,max_uzunluk)
			self.seqlen.append(len_)
			"""
				oluşturulan random değer %50 den küçük ise linner dizi 
				değilse non-lineer dizi oluştuluyor
				oluşturulan bu dizi sayıları yaklaşık olarak birbirine eşit şekilde 
				ayarlandı

			"""
			if random.random() < 0.5:
				rand_start = random.randint(0 , max_deger-len_)
				#oluşturulan uzunluk kadar lineer bir dizi oluşturuldu sayılar random üretilerek
				s = [[float(i)/max_deger] for i in range(rand_start,rand_start+len_)]
				#oluşturulan dizinin sonuna 0 lar eklenerek max uzunluğa getirildi böylece tüm dizilerin boyut 20 oldu
				s += [[0.] for i in range(max_uzunluk-len_)]
				self.data.append(s)
				self.labels.append([1,0])
			else:
				s = [[float(random.randint(0 , max_deger)) / max_deger] for i in range(len_)]
				s += [[0.] for i in range(max_uzunluk-len_)]
				self.data.append(s)
				self.labels.append([0,1])
		self.batch_id = 0
				


	def next(self , batch_size):
		"""
			next metodu ile modelde besleme yapılacak olan batch değerleri döndürülüyor
			batch_id değeri her metod çağrıldığında güncellenmektedir
			batch_id değerinden başlayarak batch_size kadar ilerleme ile batch değerleri oluşturulmakta
			eğer batch_id ve batch_size değeri data boyunu geçerse data boyu alınarak taşma engellenmektedir
			en sonra batch_id değeri batch_size değeri kadar büyütülmektedir.
			metod girişinde eğer batch_id data boyutuna eşit mi diyekontrol edilerek data boyutu taşması engellenmektedir.
		"""
		if self.batch_id == len(self.data):
			self.batch_id = 0
		batch_data = (self.data[self.batch_id:min(self.batch_id+batch_size,len(self.data))])
		batch_label = (self.labels[self.batch_id:min(self.batch_id+batch_size,len(self.data))])
		batch_seqlen = (self.seqlen[self.batch_id:min(self.batch_id+batch_size,len(self.data))])
		self.batch_id = min(self.batch_id+batch_size,len(self.data))
		return batch_data , batch_label , batch_seqlen

#MODEL

#training parametreleri
learning_rate = 0.04
num_steps = 500
batch_size = 100
display_steps = 100

#network parametreleri
num_input = 20 
hidden = 50
num_classes = 2

train_set = DiziVerisi(boyut=1000)
test_set = DiziVerisi(boyut=500)

#değişkenler için yer tut
tf_x = tf.placeholder('float',[None,num_input,1])
tf_y = tf.placeholder('float',[None,num_classes])
seqlen = tf.placeholder(tf.int32 , [None])

#ağırlık ve bias değerleri tanımlandı
weight = {'w_out':tf.Variable(tf.random_normal([hidden,num_classes]))}
biases = {'b_out':tf.Variable(tf.random_normal([num_classes]))}

def dinamikRNN(x , seqlen , W , B):
	"""
		unstack metodu tensor ü sıralı listeye dönüştürür ve lstm için sıralı liste olmalı
		dönüştürme işlemi 2. değerde verilen sayı kadar tensorü bir dizi olarak döndürüyor
		verilen 2. değer verilen 3. değerle belirtilen sıra elemanı ile aynı olmalı 
		yani verilen tensor boyutu (5,3,2) olsun verilen 3. değer çıkarılacak boyutu gösteriyor
		0 olursa ilk eleman çıkar boyut (3,2) olur ve 2. değer olarak 5 verilmeli 5 tane tensor üretsiz
		1 olursa ikinci eleman çıkar boyut (5,2) olur ve 2. değer olarak 3 verilmelidir. çıktı olarak 3 tensor dizisi üretsin
	"""
	x = tf.unstack(x , num_input , 1)
	lstm_cell = tf.contrib.rnn.BasicLSTMCell(hidden)
	output , states = tf.contrib.rnn.static_rnn(lstm_cell,x,dtype=tf.float32,sequence_length=seqlen)
	"""
		stack metodu tensor dizisini tensor'e çevirir
		Bunu yaparken dizi içindeki tensor sayısını başa ekliyor ve yeni boyut yapıyor
		yani unstack ile 2. elemanı çıkardığımızda stack metodu ile bu başa yazılıyor 
		yeni boyut değişiyor bunun için transpose uygulayarak orjinal boyuta dönüştürüyoruz
	"""
	output = tf.stack(output)
	output = tf.transpose(output , [1 , 0 , 2])

	batch_size = tf.shape(output)[0]
	index = tf.range(0,batch_size)*num_input + (seqlen-1)

	output = tf.gather(tf.reshape(output,[-1,hidden]) , index)
	return tf.matmul(output,W['w_out'])+B['b_out']

logits = dinamikRNN(tf_x , seqlen , weight , biases)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits , labels=tf_y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

correct_pred = tf.equal(tf.argmax(logits,1),tf.argmax(tf_y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)

	for step in range(1,num_steps+1):
		batch_x , batch_y , batch_seqlen = train_set.next(batch_size)
		feed_dict = {tf_x:batch_x , tf_y:batch_y , seqlen:batch_seqlen}
		sess.run(optimizer,feed_dict=feed_dict)

		if step % 100 == 0:
			acc , loss = sess.run([accuracy , cost] , feed_dict=feed_dict)
			print('Step : {}\nAccuracy : {:.4f}\nLoss : {:.4f}\n\n'.format(step , acc , loss))

	print('Optimization Finished...')

	test_data = test_set.data
	test_label = test_set.labels
	test_seqlen = test_set.seqlen

	print('Test Accuracy : {}'.format(sess.run(accuracy , feed_dict={tf_x : test_data , tf_y : test_label , seqlen : test_seqlen})))

