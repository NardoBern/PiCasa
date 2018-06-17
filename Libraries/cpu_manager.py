from subprocess import * 

##cmd_ip = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
##cmd_cpu = "mpstat | awk '$11 ~ /[0-9.]+/ { print 100 - $11}'"
##cmd_dfh = "df -h | grep /dev/root | awk '{ print $2 }'"
##cmd_dfh_p = "df -h | grep /dev/root | awk '{ print $5 }'"
##cmd_ps = "ps -ef | wc -l"
##
##def run_cmd(cmd):
##        p = Popen(cmd, shell=True, stdout=PIPE)
##        output = p.communicate()[0]
##        return output

class CPU(object):
    
    cmd_ip = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
    cmd_cpu = "mpstat | awk '$11 ~ /[0-9.]+/ { print 100 - $11}'"
    cmd_dfh = "df -h | grep /dev/root | awk '{ print $2 }'"
    cmd_dfh_p = "df -h | grep /dev/root | awk '{ print $5 }'"
    cmd_ps = "ps -ef | wc -l"

    def run_cmd(self,cmd):
            p = Popen(cmd, shell=True, stdout=PIPE)
            output = p.communicate()[0]
            return output
    def __init__(self):
      """Init a CPU status object"""
      stat_fd = open('/proc/stat')
      stat_buf = stat_fd.readlines()[0].split()

      self.prev_total = float(stat_buf[1]) + float(stat_buf[2]) + float(stat_buf[3]) + float(stat_buf[4]) + float(stat_buf[5]) + float(stat_buf[6]) + float(stat_buf[7])
      self.prev_idle = float(stat_buf[4])
      stat_fd.close()

    def usage(self):
      """return the actual usage of cpu (in %)"""	
      stat_fd = open('/proc/stat')
      stat_buf = stat_fd.readlines()[0].split()
      total = float(stat_buf[1]) + float(stat_buf[2]) + float(stat_buf[3]) + float(stat_buf[4]) + float(stat_buf[5]) + float(stat_buf[6]) + float(stat_buf[7])
      idle = float(stat_buf[4])
      stat_fd.close()
      diff_idle = idle - self.prev_idle
      diff_total = total - self.prev_total
      usage = 1000.0 * (diff_total - diff_idle) / diff_total
      usage = usage / 10
      usage = round(usage, 1)
      self.prev_total = total
      self.prev_idle = idle
      return usage


    def memUsage():
      free_fd = os.popen('free -b')
      free_buf = free_fd.readlines()[1].split()
      usage = (float(free_buf[2]) / (float(free_buf[1]))) * 100
      usage = round(usage, 1)
      return usage
