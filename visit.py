import urllib2
import random
import threading
import sys
import time
class Connect:
   req = urllib2.Request('http://google.com')
   con_sucess, con_failed, con_total=0,0,0
   url_total, proxy_total= 0,0
   url_list =[]
   proxy_list= []
   agent_list =[]

   def __init__(self):
      pF = open('proxy.txt','r')
      pR = pF.read()
      self.proxy_list = pR.split('\n')

      uF = open('url.txt','r')
      uR = uF.read()
      self.url_list = uR.split('\n')

      aF = open('agent.txt','r')
      aR = aF.read()
      self.agent_list = aR.split('\n')

   def prep_con(self):
     rURL = random.randint(0,(len(self.url_list))-1)
     self.req = urllib2.Request(self.url_list[rURL])
     rAGENT = random.randint(0,(len(self.agent_list))-1)
     self.req.add_header('User-agent',self.agent_list[rAGENT])

   def make_con(self):
      count, time_stamp =0,0
      for proxy in self.proxy_list:
       self.req.set_proxy(proxy,'http')
       if count%4==0:
         if self.con_total > 2*count:
            time_stamp = 1
         else:
            time_stamp = 1
       threading.Thread(target=self.visitURL).start()
       time.sleep(time_stamp)
       count += 1

   def visit(self):
      try:
       f = urllib2.urlopen(self.req)
       self.con_sucess += 1
      except:
       self.con_failed += 1
      self.con_total += 1
      print "\033[1;32mNo.",self.con_total,"\n\033[1;34m+ ",self.con_sucess,"\033[1;33mViewers\n\033[1;31mGagal = ",self.con_failed

   def visitURL(self):
      self.prep_con()
      self.visit()

if __name__ == "__main__":
   cnct = Connect()
   cnct.make_con()
