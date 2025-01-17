
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # experiment
    parser.add_argument("--exp_name", type=str, default="default",
                        help="exp name")
    parser.add_argument("--checkpoint", type=str, default=None,
                        help="checkpoint path")
    
    # versioning parameter
    parser.add_argument("--opt_param", type=str, default="sgd",
                        help="set a optimizer algorithm")
    parser.add_argument("--loss_param", type=str, default="cl",
                        help="set the loss to use")
    parser.add_argument("--pool_param", type=str, default=None,
                        help="set the pooling layer")
    parser.add_argument("--miner_param", type=str, default=None,
                        help="set the miner to use")
    parser.add_argument("--p_param", type=float, default=2.5,
                        help="set the parameter of the GeM pooling")
    parser.add_argument("--alpha_param", type=float, default=40,
                        help="set the parameter of the Angular loss")
    # Training parameters
    parser.add_argument("--batch_size", type=int, default=64,
                        help="The number of places to use per iteration (one place is N images)")
    parser.add_argument("--img_per_place", type=int, default=4,
                        help="The effective batch size is (batch_size * img_per_place)")
    parser.add_argument("--min_img_per_place", type=int, default=4,
                        help="places with less than min_img_per_place are removed")
    parser.add_argument("--max_epochs", type=int, default=1,
                        help="stop when training reaches max_epochs")
    parser.add_argument("--num_workers", type=int, default=8,
                        help="number of processes to use for data loading / preprocessing")

    # Architecture parameters
    parser.add_argument("--descriptors_dim", type=int, default=512,
                        help="dimensionality of the output descriptors")
    
    # Visualizations parameters
    parser.add_argument("--num_preds_to_save", type=int, default=0,
                        help="At the end of training, save N preds for each query. "
                        "Try with a small number like 3")
    parser.add_argument("--save_only_wrong_preds", action="store_true",
                        help="When saving preds (if num_preds_to_save != 0) save only "
                        "preds for difficult queries, i.e. with uncorrect first prediction")

    # Paths parameters
    parser.add_argument("--train_path", type=str, default="data/gsv_xs/train",
                        help="path to train set")
    parser.add_argument("--val_path", type=str, default="data/sf_xs/val",
                        help="path to val set (must contain database and queries)")
    parser.add_argument("--test_path", type=str, default="data/sf_xs/test",
                        help="path to test set (must contain database and queries)")
    
    args = parser.parse_args()
    return args

