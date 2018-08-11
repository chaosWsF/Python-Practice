import tensorflow as tf

# with tf.name_scope('inputs'):
a = tf.constant(2, name="a")
b = tf.constant(3, name="b")
# with tf.name_scope('add'):
x = tf.add(a, b, name="add")

with tf.Session() as sess:
    # sess.run(x)
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    sess.run(x)
    writer.close()
