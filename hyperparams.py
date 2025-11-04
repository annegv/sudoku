class Hyperparams:
    '''Hyper parameters'''
    # data
    # train_fpath = '../v2/data/sudoku.csv'
    # updated train path for the orcd data setup
    train_fpath = '../orcd/scratch/sudoku_data/sudoku.csv'
    # left the test data where it was as given in the cloned repo
    test_fpath = '../v2/data/test.csv'
    
    # model
    num_blocks = 10
    num_filters = 512
    filter_size = 3
    
    # training scheme
    lr = 0.0001
    logdir = "logdir"
    batch_size = 64
    num_epochs = 3
    
