import Week1
import Week2
import Week3
import Week4
import PerformanceTesting


performance_results = PerformanceTesting.TestComputations.performance_evaluator(subj_fun=Week3.QuickSort.quick_sort,
                                                                                gen_fun=Week3.QuickSort.int_list_generator,
                                                                                n_samples=10, min_n=1000, max_n=10**5)


PerformanceTesting.TestComputations.performance_plotter(performance_results=performance_results,
                                                        theoretical_order_fun=Week3.QuickSort.n_log_n_order)
