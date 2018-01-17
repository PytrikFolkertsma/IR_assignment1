import os
import re
from subprocess import PIPE, run
import matplotlib.pyplot as plt
import numpy as np

files = sorted([f for f in os.listdir('clean_results')])

measures = ["ndcg_cut_10", "map_cut_1000", "P_5", "recall_1000"]
# measures = ["ndcg_cut_10"]

for measure in measures:
	results = []
	d = {}
	c = 0
	output = open('trec_eval_results/' + measure + '.txt', 'w')
	print('\nMeasure:', measure)
	for file in files:
		result = run('./../trec_eval/trec_eval -m all_trec ap_88_89/qrel_test results_run/' + file + ' -q | grep -E "^' + measure + '\s"', shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		scores = [float(line.split('\t')[2]) for line in result.stdout.split('\n')[:-2]] #last element is empty, second last element is score for all
		score = sum(scores)/len(scores)
		if c == 0:
			queries = [line.split('\t')[1] for line in result.stdout.split('\n')[:-2]]
			output.write(measure + '\t' + '\t'.join(queries) + '\n')
			c += 1

		print(file, score)
		output.write(file + '\t' + '\t'.join(str(x) for x in scores) + '\n')
	output.close()



		# score = float(result.stdout.strip().split('\t')[2])
		# print(file, scores)
		# results.append([file, scores])
	# print('\nPvalue <', 0.05/5, '\n')

	# for i in range(len(results)):
	# 	for e in range(i+1, len(results)):
	# 		# print(i, e)
	# 		t = stats.ttest_rel(results[i][1], results[e][1])
	# 		if t.pvalue < 0.01:
	# 			print('Significant:', results[i][0], results[e][0], t.pvalue)
	# 		else:
	# 			print('Unsignificant:', results[i][0], results[e][0], t.pvalue)





		# param = re.search(re.compile('\d.\d*'), file).group()
		# lm = re.search(re.compile('[a-z_a-z]*'), file).group()
		# # print(lm, score, param)
		# if lm not in scores:
		# 	d[lm] = {'best_param': param, 'score': score}
		# 	continue
		# if score > d[lm]['score']:
		# 	d[lm]['best_param'] = param
		# 	d[lm]['score'] = score
