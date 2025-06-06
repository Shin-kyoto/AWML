# 1. Train and deploy TransFusion

# Test to create data for T4dataset
python tools/detection3d/create_data_t4dataset.py --root_path ./data/t4dataset --config pipelines/test_integration/configs/dataset/test.py --version xx1 --max_sweeps 2 --out_dir ./data/t4dataset/info/test_name && \
# Test to train TransFusion model
python tools/detection3d/train.py pipelines/test_integration/configs/TransFusion/transfusion_test.py && \
# Test to evaluation TransFusion model
python tools/detection3d/test.py pipelines/test_integration/configs/TransFusion/transfusion_test.py work_dirs/pretrain/transfusion/epoch_50.pth
