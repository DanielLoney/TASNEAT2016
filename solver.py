""" 2-input solver example """
from __future__ import print_function
from neat import nn, population, statistics, visualize
from preprocessing import Preprocessing

path = 'Data Sets\student-mat.csv'

print("Please set the 'output nodes' in the config file to the appropriate value\nInput output method. 0 is integer, 1 is binary, 2 is tally:\n ")
method = int(raw_input())

solver_inputs = Preprocessing.preprocess_inputs(path)
solver_outputs = Preprocessing.preprocess_outputs_1(path, method)


def eval_fitness(genomes):

    for g in genomes:
        net = nn.create_feed_forward_phenotype(g)
        error = 0.0

        if method == 0:
            for inputs, expected in zip(solver_inputs, solver_outputs):
                # Serial activation propagates the inputs through the entire network.
                output = net.serial_activate(inputs)
                error += abs(output[0] - expected[0])
            # integer fitness
        elif method == 1:
            for inputs, expected in zip(solver_inputs, solver_outputs):
                # Serial activation propagates the inputs through the entire network.
                output = net.serial_activate(inputs)
                outputs_sum = 0.0
                expected_sum = 0.0
                for index, digit in enumerate(output):
                    outputs_sum += (2**(len(output)-1-index))*digit
                for index, digit in enumerate(expected):
                    expected_sum += (2**(len(expected)-1-index))*digit  # base 2 to base 10
                error += abs(outputs_sum - expected_sum)
            # binary fitness
        elif method == 2:
            for inputs, expected in zip(solver_inputs, solver_outputs):
                # Serial activation propagates the inputs through the entire network.
                output = net.serial_activate(inputs)
                outputs_sum = 0.0
                expected_sum = 0.0
                for tally in output:
                    outputs_sum += tally
                for tally in expected:
                    expected_sum += tally
                error += abs(outputs_sum - expected_sum)
            # tally fitness
        g.fitness = 1 - error
        # When the output matches expected for all inputs, fitness will reach
        # its maximum value of 1.0.

generation = -1
if method == 0:
    generation = 10  # integer output
elif method == 1:
    generation = 30  # binary output
elif method == 2:
    generation = 50  # tally output


pop = population.Population('solver_config')
pop.epoch(eval_fitness, generation)  # max generations

print('Number of evaluations: {0}'.format(pop.total_evaluations))

# Display the most fit genome.
print('\nBest genome:')
winner = pop.most_fit_genomes[-1]
print(winner)

# Verify network output against training data.
print('\nOutput:')
winner_net = nn.create_feed_forward_phenotype(winner)
'''for inputs, expected in zip(solver_inputs, solver_outputs):
    output = winner_net.serial_activate(inputs)
    print("expected {0:1.5f} got {1:1.5f}".format(expected, output[0]))'''

# Visualize the winner network and plot/log statistics.
visualize.plot_stats(pop)
visualize.plot_species(pop)
visualize.draw_net(winner, view=True, filename="solver_1-all.gv")
visualize.draw_net(winner, view=True, filename="solver_1-enabled.gv", show_disabled=False)
visualize.draw_net(winner, view=True, filename="solver_1-enabled-pruned.gv", show_disabled=False, prune_unused=True)
statistics.save_stats(pop)
statistics.save_species_count(pop)
statistics.save_species_fitness(pop)
