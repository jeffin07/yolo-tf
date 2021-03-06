import numpy as np
import os
from data.utils import Bbox
import data.utils as utils

class Loader:

	def __init__(self, data_path, config, label_format):
		self.batch_ptr = 0
		self.data_path = data_path
		self.config = config
		self.label_format = label_format
		self.anchors = [Bbox(0, 0, config["ANCHORS"][2*i], config["ANCHORS"][2*i + 1]) for i in range(int(len(config["ANCHORS"])/2))]
		
	def next_batch(self, batch_size):
		x_batch = np.zeros([batch_size, self.config["IMAGE_W"], self.config["IMAGE_H"], 3], np.float32)
		y_batch = np.zeros([batch_size, self.config["GRID_W"], self.config["GRID_H"], self.config["BOX"], 4+1+self.config["CLASS"]], np.float32)
		max_iou = -1
		best_prior = -1
		instance_count = 0
		ptr = self.batch_ptr*batch_size
		image_files = open(os.path.join(self.data_path,"train.txt"), "r").readlines()[ptr:ptr+batch_size]

		for img in image_files:
			name = img.split("/")[-1][:-4]
			# print (name)
			cat = img.split("/")[-2]
			lbl = open(os.path.join(self.data_path,"labels"+self.label_format,cat,name+"txt"),"r").readlines()
			#needs to be changed accroding to the standard format
			lbl_all = [l+lbl[i-1] for i, l in enumerate(lbl) if i % 2 == 0]
			objs = utils.convert_to_bbox(lbl_all)
			image, objs = utils.manip_image_and_label(img.strip("\n"), objs, self.config)

			for obj in objs:						
				class_vector = np.zeros(self.config["CLASS"])
				class_vector[obj.cat] = 1

				center_x = .5 * (obj.xmin + obj.xmax)
				center_x = center_x / (self.config["IMAGE_W"]/self.config["GRID_W"])
				center_y = .5 * (obj.ymin + obj.ymax)
				center_y = center_y / (self.config["IMAGE_H"]/self.config["GRID_H"])

				center_w = (obj.xmax - obj.xmin) / (self.config["IMAGE_W"]/self.config["GRID_W"])
				center_h = (obj.ymax - obj.ymin) / (self.config["IMAGE_H"]/self.config["GRID_H"])

				grid_x = int(np.floor(center_x))
				grid_y = int(np.floor(center_y))
				# print ("grid_x is {} grid_y is {}".format(grid_x, grid_y))

				bbox = [center_x, center_y, center_w, center_h]
				box = Bbox(0, 0, center_w, center_h)

				for i in range(len(self.anchors)):
					iou = utils.compute_iou(self.anchors[i], box)
					# print ("iou is : {}".format(iou))

					if iou > max_iou:
						max_iou = iou
						best_prior = i
						# print ("best iou is : {}".format(max_iou))

				y_batch[instance_count, grid_x, grid_y, best_prior, 0:4] = bbox
				y_batch[instance_count, grid_x, grid_y, best_prior, 4] = 1
				y_batch[instance_count, grid_x, grid_y, best_prior, 5:5+self.config["CLASS"]] = class_vector
				x_batch[instance_count] = image

			instance_count += 1
		self.batch_ptr += 1

		return x_batch, y_batch

	def prev_batch():
		print ("to do")
