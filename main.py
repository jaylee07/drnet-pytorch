import argparse

def argument():
    parser = argparse.ArgumentParser(description='DrNet-implementation')
    parser.add_argument('--dataset', required=True, default='facades')
    parser.add_argument('--trainBatchSize', type=int, default=1, help='training batch size')
    parser.add_argument('--testBatchSize', type=int, default=1, help='testing batch size')
    parser.add_argument('--maxepoch', type=int, default=200, help='number of epochs')
    parser.add_argument('--ch_in', type=int, default=3, help='input image channels')
    parser.add_argument('--ch_out', type=int, default=3, help='output image channels')
    parser.add_argument('--width', type=int, default=64, help='width of input figure')
    parser.add_argument('--ngf', type=int, default=64, help='generator filters')
    parser.add_argument('--ndf', type=int, default=64, help='discriminator filters')
    parser.add_argument('--lrD', type=float, default=0.00002, help='Learning Rate D')
    parser.add_argument('--lrG', type=float, default=0.0002, help='Learning Rate G')
    parser.add_argument('--lr_policy', type=str, default='step', help='learning rate schedule')
    parser.add_argument('--lr_decay_iters', type=int, default=30, help='lr decay frequency')
    parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for adam. default=0.5')
    parser.add_argument('--cuda', action='store_true', default=True, help='use cuda?')
    parser.add_argument('--threads', type=int, default=4, help='number of threads for data loader to use')
    parser.add_argument('--seed', type=int, default=123, help='random seed to use. Default=123')
    parser.add_argument('--save_dir', type=str, default='result')
    parser.add_argument('--model', type=str, default='DrNet')
    parser.add_argument('--modelD', type=str, default='n_layer')
    parser.add_argument('--modelG', type=str, default='resnet_9blocks')
    parser.add_argument('--pose_dim', type=str, default='resnet_9blocks')
    parser.add_argument('--content_dim', type=str, default='resnet_9blocks')
    parser.add_argument('--norm_type', type=str, default='batch')
    parser.add_argument('--use_dropout', type=bool, default='False')
    parser.add_argument('--init_type', type=str, default='normal')
    parser.add_argument('--gpu_ids', type=int, nargs='+', help='# of gpu_ids')
    parser.add_argument('--layers', type=int, nargs='+', help='# of resnet_blocks in one layer')

    opt = parser.parse_args()
    return opt