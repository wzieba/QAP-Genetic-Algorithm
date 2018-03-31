# QAP with GA 🐒 [![Build Status](https://travis-ci.org/wzieba/QAP-Genetic-Algorithm.svg?branch=master)](https://travis-ci.org/wzieba/QAP-Genetic-Algorithm) [![codecov](https://codecov.io/gh/wzieba/QAP-Genetic-Algorithm/branch/master/graph/badge.svg)](https://codecov.io/gh/wzieba/QAP-Genetic-Algorithm)

Resolving Quadratic Assignment Problem with Genetic Algorithm

## 🚀 Getting Started

To run clone repo, go to `src` folder and run
```
python main.py
```

## 🔧 Config

In `config.py` you can find following configuration options:
```
INPUT_FILE = "had12.dat"
CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.08
POPULATION_SIZE = 100
NUMBER_OF_GENERATIONS = 100
DRAW_VISUALIZATION = True
DRAW_CHART = True
```
Feel free to experiment with them.

## 📈 Visualization

### Simulation

![Visualization](https://raw.githubusercontent.com/wzieba/QAP-Genetic-Algorithm/master/static/visualization.gif "Visualization")

#### Legend (how to read)

- Red color of line means long distance, green one - short
- Thick line means big value of flow (aka cost), thin one - small

Both values are in context of particular distance and flow matrices

In short: thin green is better than thick red

### Charts

![Chart](https://raw.githubusercontent.com/wzieba/QAP-Genetic-Algorithm/master/static/chart.png "Chart")

## 🚚 Quadratic Assignment Problem

The objective of the Quadratic Assignment Problem (QAP) is to assign n facilities to n locations in such a way as to minimize the assignment cost. The assignment cost is the sum, over all pairs, of the flow between a pair of facilities multiplied by the distance between their assigned locations.

Source and more information: [neos-guide.org](https://neos-guide.org/content/quadratic-assignment-problem)

### Dataset

Dataset available in `res/data` are taken from [http://anjos.mgi.polymtl.ca/qaplib/inst.html#HRW](http://anjos.mgi.polymtl.ca/qaplib/inst.html#HRW)

Authors: S.W. Hadley, F. Rendl and H. Wolkowicz

## Genetic Algorithm

In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection. [More](https://en.wikipedia.org/wiki/Genetic_algorithm)

### Important note

Some fragments of this implementation were inspired by code of mgr Filip Bachura from Wroclaw University of Science and Technology