import sys
from pathlib import Path
import argparse
from PIL import Image

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--src_dir", default=r"E:\Repos\CVLab-license-plate\LP_Swapping\pair_data\02color_same-id", help="Path to the folder containing the images")
    ap.add_argument("--dst_dir", default=r"E:\Repos\SPADE\datasets\02color_same-id", help="Path to the folder where to save the splitted images")
    args = ap.parse_args()

    SRC_DIR = args.src_dir
    DST_DIR = args.dst_dir

    ps = Path(SRC_DIR)
    image_path_list = list(ps.glob("**/*.png"))

    pd = Path(DST_DIR)
    pd_train_real = pd / 'train_img'
    pd_train_cond = pd / 'train_label'
    pd_train_mask = pd / 'train_inst'
    pd_test_real = pd / 'val_img'
    pd_test_cond = pd / 'val_label'
    pd_test_mask = pd / 'val_inst'
    pd_train_real.mkdir(parents=True, exist_ok=True)
    pd_train_cond.mkdir(parents=True, exist_ok=True)
    pd_train_mask.mkdir(parents=True, exist_ok=True)
    pd_test_real.mkdir(parents=True, exist_ok=True)
    pd_test_cond.mkdir(parents=True, exist_ok=True)
    pd_test_mask.mkdir(parents=True, exist_ok=True)

    for i, image_path in enumerate(image_path_list):
        print(i+1,'/',len(image_path_list))
        parent_name = image_path.parent.name # test or train

        img = Image.open(image_path)
        w,h = img.size
        w_step = w // 3
        img_cond = img.crop((w_step * 0, 0, w_step * 1, h))
        img_real = img.crop((w_step * 1, 0, w_step * 2, h))
        img_mask = img.crop((w_step * 2, 0, w_step * 3, h)).convert('L')

        img_cond.save(locals()['pd_' + parent_name + '_cond'] / image_path.name)
        img_real.save(locals()['pd_' + parent_name + '_real'] / image_path.name)
        img_mask.save(locals()['pd_' + parent_name + '_mask'] / image_path.name)

