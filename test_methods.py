from scipy import stats

lines = [[line.split('\t')[0],[float(score) for score in line.split('\t')[1:]]] for line in open('trec_eval_results/map_cut_1000.txt').readlines()]

for i in range(len(lines)):
	for e in range(i+1, len(lines)):
		t = stats.ttest_rel(lines[i][1], lines[e][1])
		print(lines[i][0], lines[e][0], t.pvalue)
