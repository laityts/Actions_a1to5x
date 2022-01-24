import os

DTB_NAME = "dtb_tmp"
DTS_NAME = "dtsi"

os.system("./mkdtimg dump dtbo.img -b " + DTB_NAME)

for i in range(20):
    fi  = DTB_NAME + "." + str(i)
    fo  = DTS_NAME + "." + str(i)
    cmd = "./dtc -q -I dtb -O dts " + fi + " -o " + fo
    if os.path.isfile(fi):
        print(cmd)
        os.system(cmd)
        os.remove(fi)
    else:
        break