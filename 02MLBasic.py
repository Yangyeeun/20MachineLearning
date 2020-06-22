import tensorflow as tf
tf.enable_eager_execution()
# Data
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]
# W, b initialize
W = tf.Variable(2.9)
b = tf.Variable(0.5)

# learning_rate initialize
## grad값을 얼만큼 반영할것인지 결정
learning_rate = 0.01

for i in range(100+1): # W, b update
 # Gradient descent## tape에 변수기록, 호출해 미분값 구하기
 with tf.GradientTape() as tape:
 hypothesis = W * x_data + b
 
 cost = tf.reduce_mean(tf.square(hypothesis - y_data))
 W_grad, b_grad = tape.gradient(cost, [W, b])
 W.assign_sub(learning_rate * W_grad)
 b.assign_sub(learning_rate * b_grad)
 
 if i % 10 == 0:
 print("{:5}|{:10.4f}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))
