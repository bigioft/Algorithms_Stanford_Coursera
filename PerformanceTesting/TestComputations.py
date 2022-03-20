# coding=utf-8
import timeit
import numpy as np
import pandas as pd
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


def performance_evaluator(subj_fun, gen_fun, n_samples=10, min_n=10, max_n=10**6):
    random.seed(10)
    n_points = 20
    eval_points = np.linspace(start=min_n, stop=max_n, num=n_points).astype(np.int32)
    all_performances = {}
    for n_i in eval_points:
        performance_times = []
        for k in range(0, n_samples):
            generated_problem = gen_fun(n_i)
            starting_time = timeit.default_timer()
            _ = subj_fun(generated_problem)
            performance_time = timeit.default_timer() - starting_time
            performance_times.append(performance_time)
        all_performances[n_i] = performance_times
    return all_performances


def performance_plotter(performance_results, theoretical_order_fun):
    best_performances = np.array([np.min(performance_results[i]) for i in performance_results.keys()])
    avg_performances = np.array([np.mean(performance_results[i]) for i in performance_results.keys()])
    worst_performances = np.array([np.max(performance_results[i]) for i in performance_results.keys()])

    theoretical_order = theoretical_order_fun(performance_results.keys())
    m, b = np.polyfit(theoretical_order, avg_performances, 1)
    theo_performances = b + m * theoretical_order

    data_performance = pd.DataFrame({
        'n': performance_results.keys(),
        'best': best_performances,
        'avg': avg_performances,
        'worst': worst_performances,
        'theo': theo_performances})

    plt.interactive(False)
    sns.lineplot(x='n', y='value', hue='variable',
                 data=pd.melt(data_performance, ['n']))
    plt.show()
