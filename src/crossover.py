import copy
import random
import numpy as np

from src.config import crossover_probability


def perform_crossover(population):  # Select for crossover
    species_nc = []
    crossover_list = []
    for n_chrom in population:
        rnd = random.uniform(0, 1)
        if rnd < crossover_probability:
            crossover_list.append(n_chrom)
        else:
            species_nc.append(n_chrom)
    crossover_tuples = []
    # Create crossover buddies
    cr_iterate = list(enumerate(crossover_list))
    while cr_iterate:
        cch_idx, c_chrom = cr_iterate.pop()
        if not cr_iterate:
            species_nc.append(c_chrom)
            break
        cb_idx, cross_buddy = random.choice(cr_iterate)
        cr_iterate = [(x_k, x_v) for x_k, x_v in cr_iterate if x_k != cb_idx]
        crossover_tuples.append((c_chrom, cross_buddy))
        # Crossover to list
    after_cover = []
    for cr_tup in crossover_tuples:
        cr_o, cr_t = crossover_chromosomes(
            cr_tup[0], cr_tup[1],
            point_of_crossover=random.randint(0, len(cr_tup) - 1)
        )
        after_cover.append(cr_o)
        after_cover.append(cr_t)
    # New population
    population = after_cover + species_nc
    return population


def crossover_chromosomes(chromosome_o, chromosome_s, point_of_crossover):
    # Random point to crossover
    chr_o, chr_s = copy.copy(chromosome_o), copy.copy(chromosome_s)
    # Change chromosome
    for ch_idx in range(0, point_of_crossover):  # values on ind
        fac_o = chr_o[ch_idx]
        fac_s = chr_s[ch_idx]
        # Values for swap
        fac_os_idx = chr_o.index(fac_s)
        fac_so_idx = chr_s.index(fac_o)
        # Save values
        chr_o[fac_os_idx] = fac_o
        chr_s[fac_so_idx] = fac_s
        # Change values
        chr_o[ch_idx] = fac_s
        chr_s[ch_idx] = fac_o
    return chr_o, chr_s
