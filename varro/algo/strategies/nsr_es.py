"""
This module contains the class for Simple Genetic Algorithm strategy
"""

import os
import numpy as np
import random
from deap import base, creator, tools
from collections import namedtuple

from varro.algo.strategies.strategy import Strategy
from varro.algo.strategies.ns_es import StrategyNSES


class StrategyNSRES(StrategyNSES):

    #############
    # VARIABLES #
    #############
    @property
    def novelty_metric(self):
        """The distance metric to be used to measure an Individual's novelty"""
        return self._novelty_metric

    #############
    # FUNCTIONS #
    #############
    def init_fitness_and_inds(self):
        """Initializes the fitness and definition of individuals"""

        class Scores(list):
            def __init__(self, fitness_score=None, novelty_score=None):
                super().__init__([fitness_score, novelty_score,])
                self.fitness_score, self.novelty_score = fitness_score, novelty_score

            @property
            def fitness_score(self):
                return self.__fitness_score

            @fitness_score.setter
            def fitness_score(self, fitness_score):
                self.__fitness_score = fitness_score
                super().__setitem__(0, fitness_score)

            @property
            def novelty_score(self):
                return self.__novelty_score

            @novelty_score.setter
            def novelty_score(self, novelty_score):
                self.__novelty_score = novelty_score
                super().__setitem__(1, novelty_score)

            def __setitem__(self, key, value):
                if key == 0:
                    self.fitness_score = value
                else:
                    self.novelty_score = value

        Fitness = type('Fitness', (base.Fitness,), dict(values=Scores()))
        creator.create("FitnessMulti", Fitness, weights=(-1.0, 1.0,)) # Both Fitness and Novelty
        creator.create("Individual", np.ndarray, fitness=creator.FitnessMulti)


    def init_toolbox(self):
        """Initializes the toolbox according to strategy"""
        # Define specific Fitness and Individual for Novelty Search and Reward (Fitness)
        self.init_fitness_and_inds()

        # Configure the rest of the toolbox that is independent
        # of which evolutionary strategy
        super().config_toolbox()


    def load_es_vars(self):
        """Loads the evolutionary strategy variables from checkpoint given after
        creating the fitness and individual templates for DEAP evolution or initializes them
        """
        super().load_es_vars()

        # If we have a multiobjective strategy,
        # we also need to keep the Pareto Fronts
        self.paretofront = cp["paretofront"] if self.ckpt else tools.ParetoFront(similar=np.array_equal)


    def save_ckpt(self, exp_ckpt_dir):
        """Saves the checkpoint of the current generation of Population
        and some other information

        Args:
            exp_ckpt_dir (str): The experiment's checkpointing directory
        """
        # Fill the dictionary using the dict(key=value[, ...]) constructor
        cp = dict(pop=self.pop,
                  curr_gen=self.curr_gen,
                  halloffame=self.halloffame,
                  paretofront=self.paretofront,
                  logbook=self.logbook,
                  rndstate=self.rndstate)

        with open(os.path.join(exp_ckpt_dir, 'checkpoint_gen{}.pkl'.format(self.curr_gen)), "wb") as cp_file:
            pickle.dump(cp, cp_file)


    def evaluate(self, pop):
        """Evaluates an entire population on a dataset on the neural net / fpga
        architecture specified by the model, and calculates the fitness scores for
        each individual, sorting the entire population by fitness scores in-place

        Args:
            pop (list): An iterable of np.ndarrays that represent the individuals

        Returns:
            Average fitness score of population

        """
        # Re-generates the training set for the problem (if possible) to prevent overfitting
        self.problem.reset_train_set()

        # Compute all fitness for population
        num_invalid_inds = super(StrategyNSES, self).compute_fitness(pop)

        # Calculate the Novelty scores for population
        super().compute_novelty(pop)

        # The population is entirely replaced by the
        # evaluated offspring
        self.pop[:] = pop

        # Update population statistics
        self.halloffame.update(self.pop)
        self.paretofront.update(self.pop)
        # record = self.stats.compile(self.pop)
        # self.logbook.record(gen=self.curr_gen, evals=num_invalid_inds, **record)

        return np.mean([ind.fitness.values.fitness_score for ind in pop])


    def generate_offspring(self):
        """Generates new offspring using a combination of the selection methods
        specified to choose fittest individuals and custom preference

        Returns:
            A Tuple of (Non-alterable offspring, Alterable offspring)

        """
        return super().generate_offspring()


    ########
    # INIT #
    ########
    def __init__(self, novelty_metric, **kwargs):

        # Call Strategy constructor
        Strategy.__init__(self, name='nsr-es', **kwargs)

        # Set Novelty metric
        # Supported novelty metrics:
        # https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html#sklearn.neighbors.DistanceMetric
        self._novelty_metric = novelty_metric
