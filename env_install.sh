# Check if the Conda environment exists
if conda env list | grep 'yolo_test'; then
    # If it exists, activate it
    conda activate yolo_test
    echo "Environment 'yolo_test' activated."
else
    echo "Environment 'yolo_test' does not exist. Creating it from env.yml..."
    # Create the environment from the environment file
    conda env create -f env.yml
    conda activate yolo_test
    echo "Environment 'yolo_test' created and activated."
fi
