from templ import MakeTeampl
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('/home/subadmin/PycharmProjects/cp/config/config.ini')
test = MakeTeampl(config._sections['GLOBAL'])

test.init_node(config._sections['server_1'])
test.init_node(config._sections['server_2'])
test.init_node(config._sections['server_3'])

vhost_arr = {'domain_name': 'test.ru', 'user': 'admin', 'group': 'wheel',
             'domain_alias': 'www.test.ru test2.ru www.test2.ru', 'owner': '123'}

test.init_templ(vhost_arr)

test.write_config("apache", 'test.ru')

vhost_arr = {'domain_name': 'test5.ru', 'user': 'admin', 'group': 'wheel',
             'domain_alias': 'www.test5.ru', 'owner': '123'}

test.init_templ(vhost_arr)

test.write_config("apache", 'test5.ru')

