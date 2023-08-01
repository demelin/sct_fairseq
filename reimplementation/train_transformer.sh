#!/bin/sh

# Variables
data_dir=$1
model_dir=$2

mkdir $model_dir
mkdir $model_dir/checkpoints
mkdir $model_dir/tensorboard_logs

# Train / finetune model
# For hyper-parameter choices, see https://github.com/pytorch/fairseq/issues/346
# NOTE: PARAMETERS ASSUME TRAINING ON TWO GPUS!
fairseq-train $data_dir \
    --arch transformer \
    --task translation \
    --max-tokens 3072 \
    --update-freq 4 \
    --share-all-embeddings \
    --max_len_b_mt 400 \
    --dropout 0.1 \
    --attention-dropout 0.1 \
    --activation-dropout 0.1 \
    --optimizer adam \
    --adam-betas '(0.9, 0.98)'\
    --lr-scheduler inverse_sqrt \
    --warmup-init-lr 1e-07 \
    --warmup-updates 8000 \
    --lr 2e-4 \
    --label-smoothing 0.1 \
    --weight-decay 0.0 \
    --clip-norm 0.0 \
    --validate-interval-updates 4000 \
    --log-format json \
    --log-interval 100 \
    --save-interval-updates 4000 \
    --save-dir $model_dir/checkpoints \
    --tensorboard-logdir $model_dir/tensorboard_logs \
    --max-update 1000000 \
    --patience 3
