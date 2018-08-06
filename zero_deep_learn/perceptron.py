#!/usr/bin/env python
# -*- conding: utf-8 -*-

class Perceptron(object):
    def __init__(self, input_num, activator):
        self.activator = activator
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0

    def __str__(self):
        return "weights:{0}\nbias:{1}\n".format(self.weights, self.bias)

    def predict(self, input_vec):
        first = map(lambda (x, w): x * w, zip(input_vec, self.weights))
        # print "first={}".format(first)
        second = reduce(lambda a, b: a + b, first, 0.0)
        # print "second={}".format(second)
        return self.activator(second + self.bias)

    def train(self, input_vecs, labels, iteration, rate):
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        samples = zip(input_vecs, labels)
        for input_vec, label in samples:
            output = self.predict(input_vec)
            self._update_weigths(input_vec, output, label, rate)

    def _update_weigths(self, input_vec, output, label, rate):
        delta = label - output
        self.weights = map(lambda (x, w): w + rate * delta * x, zip(input_vec, self.weights))
        self.bias += rate * delta


def f(x):
    return 1 if x > 0 else 0


def get_training_dataset():
    input_vecs = [[0, 0], [1, 0], [0, 1], [1, 1]]
    labels = [0, 0, 0, 1]
    return input_vecs, labels


def train_and_perception():
    p = Perceptron(2, f)
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    return p


if __name__ == '__main__':
    and_preception = train_and_perception()
    print and_preception
    # print "1 and 1 = %d" % and_preception.predict([1, 1])
    # print "1 and 0 = %d" % and_preception.predict([1, 0])
    # print "0 and 1 = %d" % and_preception.predict([0, 1])
    # print "0 and 0 = %d" % and_preception.predict([0, 0])
