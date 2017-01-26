import os

def get_dir_size(dn):
	result = 0
	for sub_dn, _, fn_list in os.walk(dn):
		for fn in fn_list:
			try:
				result += os.path.getsize(os.path.join(sub_dn, fn))
			except Exception:
				pass
	return result

base_dn = '/nfs/dust/cms/user/'
for dn in os.listdir(base_dn):
	print dn, get_dir_size(os.path.join(base_dn, dn))
