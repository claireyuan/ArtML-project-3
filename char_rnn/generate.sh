set -x

python generate.py --cuda \
	--data data \
	--checkpoint ./model${1}.pt \
	--outf generated${1}.txt \
	--words 100000 # 2>&1 | tee -a train${1}.log
