_base_ = "../glip_atss_swin-t_a_fpn_dyhead_pretrain_obj365.py"

model = dict(
    test_cfg=dict(
        max_per_img=300,
        chunked_size=40,
    )
)

dataset_type = "LVISV1Dataset"
data_root = "data/coco/"

val_dataloader = dict(
    dataset=dict(
        data_root=data_root, type=dataset_type, ann_file="annotations/lvis_od_val.json", data_prefix=dict(img="")
    )
)
test_dataloader = val_dataloader

# numpy < 1.24.0
val_evaluator = dict(_delete_=True, type="LVISFixedAPMetric", ann_file=data_root + "annotations/lvis_od_val.json")
test_evaluator = val_evaluator
