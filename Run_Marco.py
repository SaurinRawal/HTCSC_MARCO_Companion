from Automated_Marco import *
from file_chem_converter import set_up_cockail_csv
from args import set_args

HWI_NUM_WELLS = 1536

def main():
    args = set_args()

    images_path = args['PATH']
    model_path = args['MODEL_PATH']
    csv_path = args['CSV_PATH']
    hit_path = args['HITS_PATH']
    cocktail_path = args['COCKTAIL_PATH']
    print(images_path)
    #loud = args['LOUD']

    test_write_locations(csv_path, hit_path)

    crystal_images = get_images(images_path)
    size = len(crystal_images)

    iterator = load_images(crystal_images)
    cocktail_dict = set_up_cockail_csv(cocktail_path=cocktail_path)

    csv_data = run_model(tf.contrib.predictor.from_saved_model(model_path),
                         size,
                         cocktail_dict,
                         iterator)
    write_csv(csv_data, csv_path)

    get_crystal_predictions(csv_path, hit_path)

    #if loud: play_sound()
if __name__ == '__main__':
    main()
