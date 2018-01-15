import os
import re
from subprocess import PIPE, run
import matplotlib.pyplot as plt
import numpy as np

filenames = ['jelinek_mercer', 'dirichlet_prior', 'absolute_discounting']

files = sorted([f for f in os.listdir('results_run') if re.match('|'.join(filenames), f)])

# measures = ["ndcg_cut_10\s", "map_cut_1000"]
measures = ["ndcg_cut_10\s"]

for measure in measures:
	d = {}

	print('\n')
	for file in files:
		result = run('./../trec_eval/trec_eval -m all_trec ap_88_89/qrel_validation results_run/' + file + ' -q | grep -E "' + measure + '"', shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		scores = [float(line.split('\t')[2]) for line in result.stdout.split('\n') if len(line.split('\t')) == 3]
		# score = float(result.stdout.strip().split('\t')[2])
		
		print(scores)

		plt.hist(scores)
		plt.show() 
		
		score = sum(scores)/len(scores)
		param = re.search(re.compile('\d.\d*'), file).group()
		lm = re.search(re.compile('[a-z_a-z]*'), file).group()
		# print(lm, score, param)
		if lm not in scores:
			d[lm] = {'best_param': param, 'score': score}
			continue
		if score > d[lm]['score']:
			d[lm]['best_param'] = param
			d[lm]['score'] = score

	print(measure)
	for lm in d:
		print(lm, d[lm])

