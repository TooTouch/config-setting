# argparse
python 0.argparse.py ./configs.yaml 2 \
-n=test \
--is_use \
-m resnet18 \
-c a b c

# omegaconf
python 1.omegaconf.py \
config=./configs.yaml \
add_opt1=kkk \
add_opt2.params1=1 add_opt2.params2=test \
add_list=[1,2,3] \
add_dict="{a: 1, b: 2}" 

# fire
python 2.fire.py \
--name=test1 \
--case=[2,3,4] \
--params="{'a':1, 'b':2}" \
--is_use True