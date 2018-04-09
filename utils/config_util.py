from configparser import ConfigParser, ExtendedInterpolation
import json
import os

class Parser(object):
    def __init__(self, config_path):
        assert os.path.exists(config_path), '{} not exists.'.format(config_path)
        self.config = ConfigParser(
            delimiters='=',
            interpolation=ExtendedInterpolation())
        self.config.read(config_path)

    @property
    def num_pre_loss(self):
        return self.config.getint('rl', 'num_pre_loss')

    @property
    def dim_state_rl(self):
        return self.config.getint('rl', 'dim_state_rl')

    @property
    def dim_hidden_rl(self):
        return self.config.getint('rl', 'dim_hidden_rl')

    @property
    def dim_action_rl(self):
        return self.config.getint('rl', 'dim_action_rl')

    @property
    def lr_rl(self):
        return self.config.getfloat('rl', 'lr_rl')

    @property
    def total_episodes(self):
        return self.config.getint('rl', 'total_episodes')

    @property
    def max_training_step(self):
        return self.config.getint('rl', 'max_training_step')

    @property
    def update_frequency(self):
        return self.config.getint('rl', 'update_frequency')

    @property
    def exp_dir(self):
        return os.path.expanduser(self.config.get('env', 'exp_dir'))

    @property
    def data_dir(self):
        return os.path.expanduser(self.config.get('env', 'data_dir'))

    @property
    def model_dir(self):
        return os.path.expanduser(self.config.get('env', 'model_dir'))

    @property
    def student_model_name(self):
        return self.config.getint('model', 'student_model_name')

    @property
    def train_data(self):
        return os.path.expanduser(self.config.get('data', 'train_data'))

    @property
    def valid_data(self):
        return os.path.expanduser(self.config.get('data', 'valid_data'))

    @property
    def test_data(self):
        return os.path.expanduser(self.config.get('data', 'test_data'))

    @property
    def timedelay_num(self):
        return self.config.getint('train', 'timedelay_num')

    @property
    def max_step(self):
        return self.config.getint('train', 'max_step')

    @property
    def summary_steps(self):
        return self.config.getint('train', 'summary_steps')

    @property
    def lr_policy_params(self):
        params = self.config.get('train', 'lr_policy_params', fallback='{}')
        return json.loads(params)


if __name__ == '__main__':
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config_path = os.path.join(root_path, 'config/regression.cfg')
    config = Parser(config_path)
    print(config.exp_dir)
    print(config.model_dir)