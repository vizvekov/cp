import sys
import io
import os

class makeTeampl:
        mainConfig = {};
        service_config = {};
        nodes = {};

        def __init__ (self,config):
                self.mainConfig = self.__valid_array(config);

        def init_templ (self,service,config):
    		if service in "apache" and self.__str2bool(self.mainConfig['use_nginx']):
    		    self.service_config.update({'nginx': config});
                self.service_config.update({service: config});

	def init_node (self,node_config):
	    node_config = self.__valid_array(node_config);
	    if self.__str2bool(self.mainConfig['use_nginx']):
		if 'apach_ip' not in node_config:
		    node_config.update({'apach_ip': '127.0.0.1'});
	    else:
		    node_config.update({'apach_ip': node_config['ext_ip']});
	    self.nodes.update({len(self.nodes)+1: node_config});
	
	def print_nodes(self):
	    print self.nodes
    
        def write_config(self):
    	    for key, node_conf in self.nodes.items():
                for key, value in self.service_config.items():
                        templ_file = "%s/%s/vhost.conf" % (self.mainConfig['template_dir'],key);
                        vhost_dir = "%s/%s/%s/%s" % (self.mainConfig['vhosts_dir'],key,node_conf['ext_ip'],self.service_config[key]['user']);
                        vhost_conf = "%s/%s.conf" % (vhost_dir,self.service_config[key]['domain_name']);
                        if not os.path.exists(vhost_dir):
                            os.makedirs(vhost_dir)
                        config = io.open(vhost_conf,'w');
                        self.service_config[key].update(self.mainConfig);
                        self.service_config[key].update(node_conf);
                        for line in io.open(templ_file, 'r'):
                                for var, val in self.service_config[key].items():
                            		if '$' + var in line:
                                    	    line = line.replace('$' + var, val);
                            	config.write(line);
                        config.close()

        def __valid_array (self,arr):
    	    try:
    		del arr["__name__"];
    	    except Exception, e:
    		pass;
	    return arr;

	def __str2bool(self,v):
	    return v.lower() in ("yes", "true", "t", "1")
