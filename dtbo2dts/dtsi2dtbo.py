import os

DTB_NAME = "dtb_tmp"
DTS_NAME = "dtsi"

for i in range(20):
    fi  = DTS_NAME + "." + str(i)
    fo  = DTB_NAME + "." + str(i)
    cmd = "./dtc -q -I dts -O dtb " + fi + " -o " + fo
    if os.path.isfile(fi):
        print(cmd)
        os.system(cmd)
        os.remove(fi)
    else:
        break

os.system("./mkdtimg create dtbo_new.img dtb_tmp.*")