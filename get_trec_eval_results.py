import os
import re
from subprocess import PIPE, run
import matplotlib.pyplot as plt
import numpy as np


files = [f for f in os.listdir('results_run')]

measures = ["ndcg_cut_10\s", "map_cut_1000", "^P_5\s", "recall_1000"]

for measure in measures:
	d = {}
	print('\nMeasure:', measure)
	for file in files:
		result = run('./../trec_eval/trec_eval -m all_trec ap_88_89/qrel_test results_run/' + file + ' | grep -E "' + measure + '"', shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		score = float(result.stdout.split('\t')[2].strip())
		print(file, score)

	

