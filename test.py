from templ import makeTeampl
import ConfigParser


config = ConfigParser.ConfigParser();
config.read('/home/subadmin/cluster_panel/develop/config/config.ini');
test = makeTeampl(config._sections['GLOBAL']);

vhost_arr = {'domain_name': 'test.ru', 'user': 'admin', 'group': 'wheel', 'domain_alias': 'www.test.ru test2.ru www.test2.ru'};

test.init_templ("apache",vhost_arr);

test.init_node(config._sections['server_1']);
test.init_node(config._sections['server_2']);
test.init_node(config._sections['server_3']);

test.write_config();