import tensorflow as tf

sess = tf.Session()

#Verify we can print string

hello = tf.constant("Test")
print(sess.run(hello))

#Perform simple maths 
a = tf.constant(20)
b = tf.constant(22)
print('a+b = {0}'.format(sess.run(a+b)))
