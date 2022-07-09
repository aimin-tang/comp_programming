s1 = """
<job-template>deploy-license-fmg</job-template><extra-vars>{
    "admin_password": "kwWwed8dRBmc",
    "controllers": {
        "fmg": {
            "mg1": {
                "type": "fortimanager",
                "hostname": "mg1",
                "license": "test1",
                "vm_params": {
                    "interfaces": {
                        "mgmt_int": {
                            "ipv4_addr": "10.10.10.10"
                        }
                    }
                }
            }
        }
    }
}</extra-vars><limit>mg1</limit>
"""

s2 = '<config xmlns="http://tail-f.com/ns/config/1.0">' + s1 + '</config>'

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
from xml.dom import minidom

ns_d = {'ns': "http://tail-f.com/ns/config/1.0"}

root = ET.fromstring(s2)
job_template  = root.find('./ns:job-template', ns_d)
print(job_template.text)

xml_str = tostring(root)
dom = minidom.parseString(xml_str)
lines = dom.toprettyxml(indent='  ').split('\n')
print('\n'.join([line for line in lines if line.strip()]))