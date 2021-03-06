import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_epochs', type=int, default=20, help='Number of training epochs')
    parser.add_argument('--n_folds', type=int, default=5, help='Number of training epochs')
    parser.add_argument('--fold', type=int, default=-1, help='Fold to train. -1 means train all folds in a row')
    parser.add_argument('--dataset_root', type=str, default='workdir/data/')
    parser.add_argument('--meta_root', type=str, default='workdir/data')
    parser.add_argument('--train_set', type=str, default='oai', choices=['most', 'oai'],
                        help='Dataset to be used for testing.')

    parser.add_argument('--siamese', type=bool, default=False, help='Whether to use Siamese model')
    parser.add_argument('--siamese_bb', type=str, choices=['lext', 'resnet-18', 'se_resnext50_32x4d'],
                        default='lext',
                        help='Backbone for Siamese model')

    parser.add_argument('--backbone_depth', type=int, default=18, help='Width of Resnet')
    parser.add_argument('--se', type=bool, default=False, help='Use a SE-ResNet instead of plain resent50')
    parser.add_argument('--dw', type=bool, default=False, help='D-parameter of ResNeXt blocks')
    parser.add_argument('--pretrained', type=bool, default=False, help='Whether to use ImageNet weights')
    parser.add_argument('--dropout_rate', type=float, default=0.5, help='Dropout')
    parser.add_argument('--use_bnorm', type=bool, default=False, help='whether to use batchnorm in the classifier')
    parser.add_argument('--use_gwap', type=bool, default=False, help='whether to use task-specific gwap')
    parser.add_argument('--use_gwap_hidden', type=bool, default=False, help='whether to use hidden layer for pooling')
    parser.add_argument('--no_kl', type=bool, default=False, help='Whether to train with KL grade or without')

    parser.add_argument('--weighted_sampling', type=bool, default=False, help='Weighted sampling')
    parser.add_argument('--mtw', type=bool, default=False, help='Maximum task-weighing')

    parser.add_argument('--imsize', type=int, default=700)
    parser.add_argument('--inp_size', type=int, default=310)
    parser.add_argument('--crop_size', type=int, default=300)

    parser.add_argument('--lr_drop', nargs='+', type=int, default=[1, 2])
    parser.add_argument('--lr_drop_gamma', type=list, default=0.1)
    parser.add_argument('--optimizer', type=str, choices=['sgd', 'adam'], default='adam')
    parser.add_argument('--lr', type=float, default=1e-2, help='Learning rate')
    parser.add_argument('--wd', type=float, default=1e-4, help='Weight decay')
    parser.add_argument('--bs', type=int, default=32, help='Batch size')
    parser.add_argument('--val_bs', type=int, default=128, help='Validation batch size')

    parser.add_argument('--snapshot_on', type=str, choices=['val_loss', ], default='val_loss')
    parser.add_argument('--snapshot_comparator', type=str, choices=['lt', 'gt'], default='lt')
    parser.add_argument('--keep_snapshots', type=bool, default=False)
    parser.add_argument('--unfreeze_epoch', type=int, default=1,
                        help='Epoch at which to unfreeze the layers of the backbone')

    parser.add_argument('--snapshots', default='workdir/snapshots/',
                        help='Folder for saving snapshots')
    parser.add_argument('--n_threads', default=16, type=int, help='Number of parallel threads for Data Loader')
    parser.add_argument('--seed', type=int, default=42, help='Random Seed')
    args = parser.parse_args()

    return args
