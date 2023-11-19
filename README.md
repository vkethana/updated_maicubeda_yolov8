# YoloV8 Model to Draw Bounding Boxes
This model is being trained using YoloV8. The dataset is from MaiCuBeDa. 
Important: The Python file `make_yolo_readable_dataset.py` does not work currently because I changed the file structure of the GitHub repo. As such, the program is currently referencing nonexistent files. It would not take much work to fix it, though.

I didn't upload the tablet images because of GitHub restrictions on file sizes.

# How to run the model for yourself
The repository does not work out of the box because of the image size restrictions I mentioned earlier. 
1) Download the MaiCuBeDa tablet images. Extract them into `datasets/coco/images`. The link to the original dataset is here: https://heidata.uni-heidelberg.de/dataset.xhtml?persistentId=doi:10.11588/data/QSNIQ2
2) Mass rename the image files so that the txt files in `datasets/coco/annotations` are *exactly* the same as the png files in `datasets/coco/images/`, excluding extensions. In other words, every png file in `images/` needs a corresponding txt image in `annotations/`. The scripts in `dataset_generation_files/misc` can help with this.
3) Run `cd yolov8` and then `yolo detect train data=coco8.yaml model=yolov8n.pt epochs=100 imgsz=640`, adjusting the epoch count as necessary.
4) For more info, see this link: https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format
