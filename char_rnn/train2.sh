set -x

python main.py --cuda \
	--data trump_data \
	--model LSTM \
	--emsize 32 \
	--nhid 512 \
	--nlayers 2 \
	--batch_size 64 \
	--bptt 141 \
	--lr 20 \
	--clip 0.25 \
	--epochs 400 \
	--save model${1}.pt # 2>&1 | tee -a train${1}.log

python generate.py --cuda \
	--data data \
	--checkpoint ./model${1}.pt \
	--outf generated${1}.txt \
	--words 1000 # 2>&1 | tee -a train${1}.log
