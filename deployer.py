import virtualbox 
vm = virtualbox.VirtualBox().find_machine('ubuntu') 
session = vm.create_session() 
s = virtualbox.Session() 
vm.unlock_machine()
vm.launch_vm_process()
