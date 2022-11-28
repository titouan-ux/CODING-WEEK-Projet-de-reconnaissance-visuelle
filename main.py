#from carbonai import PowerMeter
#power_meter = PowerMeter(project_name="reconnaissance_image_gr4")
import gui.gui_main

def main():
    gui.gui_main.login_process()

if __name__ == '__main__':
    #power_meter.start_measure(package='tensorflow', algorithm='recon_img')
    main()
    #power_meter.stop_measure()