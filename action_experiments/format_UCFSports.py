import os, sys, glob, shutil

data_dir = '/workspace/data/ucf_sports_actions/UCFsports/data/'
videos = [l.split() for l in file(os.path.join(data_dir,'videos.txt'))]

for v in videos:
    new_dir = os.path.join(data_dir, v[0], 'jpeg')
    old_dir = os.path.join(data_dir, '..', '/'.join(v[-1].split('/')[:2]))
    images = sorted(glob.glob(old_dir + '/*.jpg'))
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    if len(images) == 0:
        images = sorted(glob.glob(old_dir + '/jpeg/*.jpg'))

    for i in range(len(images)):
        shutil.copyfile(images[i], new_dir + '/' + str(i+1).zfill(6) + '.jpg')

    shutil.copyfile('/workspace/action-faster-rcnn/ucfsports-anno/' + v[0] + '.txt', os.path.join(data_dir, v[0], 'humans.txt'))
