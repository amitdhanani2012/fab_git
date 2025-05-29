#!/usr/bin/python2.7
from fabric import Connection
import csv
j=[]
for i in open("server1.txt","r"):
    j.append(i.strip())
print(j)
vmh=None
vm_data_center=None
vmh=input("Enter Virtual Host Name: ")
vm_data_center=input("Enter Data Center Name: ")

#if (vmh==None or vm_data_center==None):
#    exit

wr1=open('alc_test_latest.csv','w')
writer1=csv.writer(wr1)
writer1.writerow(('name','Organization->Name','Status','Business criticality','CPU','IP','RAM','VM Datacenter Location','OS family->Name','OS version->Name','OS version->Full name','Organization->Full name','Virtual host->Name'))
for k in j:
   result=None
   name=None
   organization="xyzorg"
   status="production"   
   bussiness_criticality="High" 
   processor=None
   ip=k
   ram=None
   vm_data_center_location=vm_data_center
   os_family="Linux"
   os_version=None
   os_version_fullname=None
   organization_fullname="xyzorg"
   virtual_host=vmh
   print(k) 
   o=str(k)
   c = Connection(o,user="user",connect_kwargs={"password":"passwrod"})
 
   result=c.run("hostname")
   name=result.stdout.split("\r\n")


   result=c.run('grep -i processor /proc/cpuinfo|wc -l')
   processor=result.stdout.split("\r\n")
   
   result=c.run('dx=$(echo `grep -i memtotal /proc/meminfo`|cut -f2 -d" " ) && xyz=$[ $(echo $dx)/1024 ] && echo $xyz')
   ram=result.stdout.split("\r\n")

   try: 
        result=c.run('cat /etc/redhat-release')
   except:
        os_version="not redhat"
        os_version_fullname="not redhat"
   else:
   	os_version=result.stdout.split("\r\n")
        os_version_fullname=result.stdout.split("\r\n")
     
#   print"testing 123 "+(name[0])
#   writer1.writerow(()) 
   writer1.writerow((name[0].strip('\n').strip('"'),organization.strip('\n').strip('"'),status.strip('\n').strip('"'),bussiness_criticality.strip('\n').strip('"'),processor[0].strip('\n').strip('"'),ip.strip('\n').strip('"'),ram[0].strip('\n').strip('"'),vm_data_center_location.strip('\n').strip('"'),os_family.strip('\n').strip('"'),os_version[0].strip('\n').strip('"'),os_version_fullname[0].strip('\n').strip('"'),organization_fullname.strip('\n').strip('"'),virtual_host.strip('\n').strip('"'),vm_data_center_location.strip('\n').strip('"')))

wr1.close()

