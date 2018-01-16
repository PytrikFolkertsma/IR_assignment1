import os
import re
from subprocess import PIPE, run
import matplotlib.pyplot as plt
import numpy as np

files = sorted([f for f in os.listdir('clean_results')])

measures = ["ndcg_cut_10\s", "map_cut_1000", "^P_5\s", "recall_1000"]

for measure in measures:
	d = {}

	print('\nMeasure:', measure)
	for file in files:
		result = run('./../trec_eval/trec_eval -m all_trec ap_88_89/qrel_test results_run/' + file + ' -q | grep -E "' + measure + '"', shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		scores = [float(line.split('\t')[2]) for line in result.stdout.split('\n') if len(line.split('\t')) == 3] 
		score = sum(scores)/len(scores)
		# score = float(result.stdout.strip().split('\t')[2])
		print(file, score)		


		# param = re.search(re.compile('\d.\d*'), file).group()
		# lm = re.search(re.compile('[a-z_a-z]*'), file).group()
		# # print(lm, score, param)
		# if lm not in scores:
		# 	d[lm] = {'best_param': param, 'score': score}
		# 	continue
		# if score > d[lm]['score']:
		# 	d[lm]['best_param'] = param
		# 	d[lm]['score'] = score
