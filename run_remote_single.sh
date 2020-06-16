filename=`basename "$1"`
# encode the image name
filenamebase64=$(echo $filename | base64)
filenamebase64=$(echo ${filenamebase64:0:8})
demoindir='/u/jshi31/project/T2ONet/output/FiveK_trial_1/demo_input'
demooutdir='/u/jshi31/project/T2ONeet/output/FiveK_trial_1/demo_output'
input_path=$demoindir/$filenamebase64
output_path="$demooutdir/$filenamebase64.jpg"
# upload the image
cp $1 $input_path
# call model
bash /u/jshi31/project/T2ONet/demo/run_demo_FiveK.sh $input_path 0 $2
# download the image
cp $output_path $3
