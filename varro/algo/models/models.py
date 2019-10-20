"""
This module contains classes for defining each type of model.
"""
import numpy as np
from keras.layers import Dense
from keras.models import Sequential

from varro.algo.problems import Problem


class Model:
	def __init__(self):
		"""Wrapper class for different types of models."""
		pass

	def load_weights(self, weights):
		pass

	def predict(self, X):
		pass

class ModelNN(Model):
	def __init__(self, problem):
		"""Neural network architecture wrapper class specific to a problem

		Args:
			problem (str): String specifying the type of problem we're dealing with

		"""
		self.model = Sequential()
		if problem.approx_type == Problem.CLASSIFICATION:
			self.model.add(Dense(128, input_dim=problem.input_dim, activation='relu'))
			self.model.add(Dense(64, activation='relu'))
			self.model.add(Dense(problem.output_dim, activation='softmax'))
		elif problem.approx_type == Problem.REGRESSION:
			self.model.add(Dense(1, input_dim=problem.input_dim, activation='relu'))
			self.model.add(Dense(3, activation='relu'))
			self.model.add(Dense(2, activation='relu'))
			self.model.add(Dense(problem.output_dim, activation='sigmoid'))
		else:
			raise ValueError('Unknown approximation type ' + str(problem.approx_type))
		
		self.num_weights_alterable = np.sum([np.prod(layer.shape) for layer in self.model.get_weights()[::2]])
	
	def load_weights(self, weights):
		"""Loads an array of weights into this model.

		Args:
			weights (np.ndarray of floats): The new values for the weights
				- e.g. [0.93, 0.85, 0.24, ..., 0.19]

		"""
		# Pull out the numbers from the individual and
		# load them as the shape from the model's weights
		ind_idx = 0
		new_weights = []
		for idx, layer in enumerate(self.model.get_weights()):
			# Ignore odd layers with biases
			if idx % 2:
				new_weights.append(layer)
			else: 
				# Number of weights we'll take from the individual for this layer
				num_weights_taken = np.prod(layer.shape)
				new_weights.append(weights[ind_idx:ind_idx+num_weights_taken].reshape(layer.shape))
				ind_idx += num_weights_taken

		# Set Weights using individual
		self.model.set_weights(new_weights)

	def predict(self, X):
		return self.model.predict(X)

