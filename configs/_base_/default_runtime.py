checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])

# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]
checkpoint_config = dict(create_symlink=False)
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None  #'/media/public/disk4/lyw/mmdetection/work_dirs/mask_rcnn_r50_fpn_1x_coco/epoch_12.pth'
workflow = [('train', 1)]
