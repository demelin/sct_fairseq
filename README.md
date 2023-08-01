# sct_fairseq
Re-implementation of the **Shortcut Transformer (SCT)** in fairseq and the accompanying experimental code. This codebase is provided solely for completion, as supplmentary material for the PhD thesis.
Following files had been added to / modified within the fairseq repository and should be integrated into your local fairseq repo in order to replicate the experiments discussed in the thesis:


## SCT reimplementation  
<code>./fairseq/fairseq/models/transformer/__init__.py</code>  
<code>./fairseq/fairseq/models/transformer/transformer_base.py</code>  
<code>./fairseq/fairseq/models/transformer/transformer_decoder.py</code>  
<code>./fairseq/fairseq/models/transformer/transformer_encoder.py</code>  
<code>./fairseq/fairseq/models/transformer/transformer_legacy.py</code>  
  
<code>./fairseq/fairseq/modules/__init__.py</code>  
<code>./fairseq/fairseq/modules/shortcut_multihead_attention.py</code>  
<code>./fairseq/fairseq/modules/shortcut_multihead_attention_with_fusion.py</code>  
<code>./fairseq/fairseq/modules/transformer_layer.py</code>  
  
  
## Supporting experimental code  
<code>./fairseq/fairseq/criterions/label_smoothed_cross_entropy_with_probs.py</code>
