
# filter1 = tf.get_variable(name="filter1",shape=[3, 3, 3, 32], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv1 = tf.layers.conv2d(x, filter1, strides=[1, 1, 1, 1], padding="SAME",name="conv1")
# maxpool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
# filter2 = tf.get_variable(name="filter2",shape=[3, 3, 32, 64], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv2 = tf.layers.conv2d(maxpool1, filter2, strides=[1, 1, 1, 1], padding="SAME")
# maxpool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
# filter3 = tf.get_variable(name="filter3",shape=[3, 3, 64, 128], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv3 = tf.layers.conv2d(maxpool2, filter3, strides=[1, 1, 1, 1], padding="SAME")
# filter4 = tf.get_variable(name="filter4",shape=[1, 1, 128, 64], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv4 = tf.layers.conv2d(conv3, filter4, strides=[1, 1, 1, 1], padding="SAME")
# filter5 = tf.get_variable(name="filter5",shape=[3, 3, 64, 128], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv5 = tf.layers.conv2d(conv4, filter5, strides=[1, 1, 1, 1], padding="SAME")
# maxpool3 = tf.nn.max_pool(conv5, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
# filter6 = tf.get_variable(name="filter6",shape=[3, 3, 128, 256], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv6 = tf.layers.conv2d(maxpool3, filter6, strides=[1, 1, 1, 1], padding="SAME")
# filter7 = tf.get_variable(name="filter7",shape=[1, 1, 256, 128], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv7 = tf.layers.conv2d(conv6, filter7, strides=[1, 1, 1, 1], padding="SAME")
# filter8 = tf.get_variable(name="filter8",shape=[3, 3, 128, 256], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv8 = tf.layers.conv2d(conv7, filter8, strides=[1, 1, 1, 1], padding="SAME")
# maxpool4 = tf.nn.max_pool(conv8, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
# filter9 = tf.get_variable(name="filter9",shape=[3, 3, 256, 512], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv9 = tf.layers.conv2d(maxpool4, filter9, strides=[1, 1, 1, 1], padding="SAME")
# filter10 = tf.get_variable(name="filter10",shape=[1, 1, 512, 256], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv10 = tf.layers.conv2d(conv9, filter10, strides=[1, 1, 1, 1], padding="SAME")
# filter11 = tf.get_variable(name="filter11",shape=[3, 3, 256, 512], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv11 = tf.layers.conv2d(conv10, filter11, strides=[1, 1, 1, 1], padding="SAME")
# filter12 = tf.get_variable(name="filter12",shape=[1, 1, 512, 256], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv12 = tf.layers.conv2d(conv11, filter12, strides=[1, 1, 1, 1], padding="SAME")
# filter13 = tf.get_variable(name="filter13",shape=[3, 3, 256, 512], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv13 = tf.layers.conv2d(conv12, filter13, strides=[1, 1, 1, 1], padding="SAME")
# maxpool5 = tf.nn.max_pool(conv13, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
# filter14 = tf.get_variable(name="filter14",shape=[3, 3, 512, 1024], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv14 = tf.layers.conv2d(maxpool5, filter14, strides=[1, 1, 1, 1], padding="SAME")
# filter15 = tf.get_variable(name="filter15",shape=[1, 1, 1024, 512], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv15 = tf.layers.conv2d(conv14, filter15, strides=[1, 1, 1, 1], padding="SAME")
# filter16 = tf.get_variable(name="filter16",shape=[3, 3, 512, 1024], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv16 = tf.layers.conv2d(conv15, filter16, strides=[1, 1, 1, 1], padding="SAME")
# filter17 = tf.get_variable(name="filter17",shape=[1, 1, 1024, 512], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv17 = tf.layers.conv2d(conv16, filter17, strides=[1, 1, 1, 1], padding="SAME")
# filter18 = tf.get_variable(name="filter18",shape=[3, 3, 512, 1024], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv18 = tf.layers.conv2d(conv17, filter18, strides=[1, 1, 1, 1], padding="SAME")
# filter19 = tf.get_variable(name="filter19",shape=[3, 3, 1024, 1024], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv19 = tf.layers.conv2d(conv18, filter19, strides=[1, 1, 1, 1], padding="SAME")
# filter20 = tf.get_variable(name="filter20",shape=[3, 3, 1024, 1024], initializer=tf.truncated_normal_initializer(stddev=5e-2,dtype=tf.float64),dtype=tf.float64)
# conv20 = tf.layers.conv2d(conv19, filter20, strides=[1, 1, 1, 1], padding="SAME")