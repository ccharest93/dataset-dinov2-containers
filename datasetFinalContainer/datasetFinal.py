from dinov2.data.datasets import ImageNet

for split in ImageNet.Split:
    dataset = ImageNet(split=split, root="/efs-shared", extra="/efs-shared")
    dataset.dump_extra()
