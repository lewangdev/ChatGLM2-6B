import os
os.system('apt install -y aria2c')
os.system('mkdir -p ./ChatGLM2-6B-Models')

model_file_names = [
	'MODEL_LICENSE',
	'README.md',
	'config.json',
	'configuration_chatglm.py',
	'modeling_chatglm.py',
	'pytorch_model.bin.index.json',
	'quantization.py',
	'tokenization_chatglm.py',
	'tokenizer_config.json',
	'pytorch_model-00001-of-00007.bin',
	'pytorch_model-00002-of-00007.bin',
	'pytorch_model-00003-of-00007.bin',
	'pytorch_model-00004-of-00007.bin',
	'pytorch_model-00005-of-00007.bin',
	'pytorch_model-00006-of-00007.bin',
	'pytorch_model-00007-of-00007.bin',
	'tokenizer.model'
]

for fname in model_file_names:
  cmd = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/THUDM/chatglm2-6b/resolve/main/{fname} -d ./ChatGLM2-6B-Models -o {fname}"
  os.system(cmd)
