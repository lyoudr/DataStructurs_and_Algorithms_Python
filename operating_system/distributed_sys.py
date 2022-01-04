# SSDs have the same characteristics as traditional hard disks 

# 10.1.3 Magnetic Tapes
# Magnetic tape
# Tapes are used mainly for backup, for storage of infrequently used information,

# 10.2 Disk Structure
# logical block => smallest unit of transfer.
# => 512 bytes, or 1024 bytes

# By using this mapping, we can - at least in theory -convert a logical block number into an old-style disk address that consists of a 
# (1) cylinder number
# (2) a track number within that cylinder
# (3) sector number within that track

# The farther a track is from the center of the disk, the greater its length, so the more sectors it can hold.
# The drive increases its rotation speed as the haed moves from the outer to the inner tracks to keep the same rate of data moving under the head.
# Alternatively, the disk rotation speed can stay constant; 
# in this case, 
# the density of bits decreases from inner tracks to outer tracks to keep the data rate constant.
# This method is used in hard disks and is known as "constant angular velocity (CAV)"

### 10.3 Disk Attachment

# 10.3.1 Host-Attached Storage
# (1) I/O ports (or host-attached storage): IDE, ATA, SATA
# The typical desktop PC uses an I/O bus architecture called IDE or ATA.
# This architecture supports a maximum of two drives per I/O bus. 
# High-end workstations and servers generally use more sophisticated I/O architectures such as fibre channel(FC)
    # (1) storage-area networks(SANs): large address space and the switched nature of the communication, multiple hosts and storage devices can attach to the fabric, allowing great flexibility in I/O communication.
    # (2) arbitrated loop(FC-AL): 126 devices

# 10.3.2 Network-attached storage (NAS)
# A network-attached storage (NAS) device is special-purpose storage system that is accessed remotely over a data network.
# Clientes access netowrk-attached storage via a remote-procedure-call (RPC) interface 
    # (1) NFS for UNIX systems
    # (2) CIFS for Windows machine
# Remote Procudure Call (RPC) => carried via TCP or UDP over an IP network - usually the same local area network (LAN) that carries all data traffic to the clients.
# The network-attached storage unit is usually implemented as a "RAID" array with software that implements the RPC interface.


# 10.3.3 Sotrage-Area Network (SAN)
# One drawback of network-attached storage systems is that the storage I/O operations consume bandwidth on the data network, thereby increasing the latency of network communication
# the communication between servers and clients competes for bandwidth with communication among servers and storage devices.
# A storage-area network (SAN) is a private network (using storage protocols rather than networking protocols) connecting servers and storage units
# The power of a SAN lies in its flexibility.
# Multiple hosts and multiple storage arrays can attach to the sam SAN, and storage can by dynamically allocated to hosts.


### 10.4 Disk Scheduling
# 1. seek time => disk arm to move the heads to the cylinder containing the desired sector.
# 2. rotation latency => is the additional time for the disk to rotate the desired sector to the disk head.
# 3. bandwidth => is the total number of bytes transfered, divided by the total time between the first request for service and the completion of the last transfer.
    # = number of bytes transfered / total service time (end - start)

# 4. Whenever a process needs I/O to or from the dis, it issues a system call to the operating system.
    # (1) Whether this operation is input or output
    # (2) What the disk address for the transfer is
    # (3) What the memory address for the transfer is
    # (4) What the number of sectors to be trasferred is

# 10.4.1 FCFS Scheduling
# the first-come, first-served (FCFs) algorithm

# 10.4.2 SSTF Scheduling
# service all the requests close to the current head position before moving the head far away to service other request.
# => "shortest-seek-time-first (SSTF) algorithm"
# SSTF chooses the pending request closest to the current head position.
# SSTF scheduling is essentially a form of shortest-job-first (SJF) scheduling; 
# it may cause starvation of some requests (request that is far away from current head will be pending by the coming requests near current head)

# 10.4.3 SCAN Scheduling
# the disk arm starts at one end of the disk and moves toward the other end, servicing requests as it reaches each cynlinder, until it gets to the other end of the disk.


# 10.4.4 C-SCAN Scheduling
# Circular SCAN (C-SCAN) scheduling is a variant of SCAN designed to provide a more uniform wait time.
# Like SCAN, C-SCAN moves the head from one end of the disk to the other, servicing request along the way.
# When the head reaches the other end, however, it immediately returns to the begining of the disk without servicing any requests on the return trip.


# 10.4.5 LOOK Scheduling
# In practice, neither algorithm is often implemented this way.
# More commonly, the arm goes only as far as the final request in each direction
# Then, it reverses direction immediately, without going all the way to the end of the disk.

# 10.4.5 Selection of a Disk-Scheduling Algorithm
# Requests for disk service can be greatly influenced by the file-allocation method.
# A program reading a contiguously allocated file will generate several requests tath are close together on the disk, resulting in limited head movement.
# The location of directories and index blocks is also important.
# Since every file must be op

# the rotational latency can be nearly as large as the average seek time.
# It is difficult for the operating system to schedule for imporved rotational latency,

### 10.5.1 Disk FOrmatting
# low-level formatting, physical formatting
# Before a s can store data, it must be divided into sectors that the disk controller can read and write.

# The data structure for a sector typically consists of a 
    # (1) header, (2) data area, (3) trailer.

    # header and trailer 有 
        # (1) sectior number and (2)"error-correcting code (ECC)"
    
    # When the controller writes a sector number during normal I/O, the ECC is updated with a value calculated from all the bytes in the data area.
    # When the sector is read, the ECC is recalculated and compared with the stored value. 
    # If the stored and calculated numbers are different, this mismatch indicates that the data area of the sector has become corrupted.
    # It then reports a recoverable "soft error".

# When the disk controller is instructed to low-level-format the disk, it can also be told how many bytes of data space to leave between the header and trailer of all sectors

# (1) Partition 
# partition the disk into one or more groups of cylinders.
# one store operating system's executable code
# one store user files

    # (2) Clusters => most file systems group logical blocks together into larger chunks, frequently called "clusters"
    # Disk I/O is done via blocks,
    # file system I/O is done via clusters effectively assuring that I/O has more sequential-access and fewer random-access characteristics.

# (3) Logical Formatting
# the operating system stores the initial file-system data structures onto the disk.

# Some operating systems give special programs the ability to use a disk partition as a large sequential array of logical blocks, without any file-system data structures.
# This array is sometimes called the raw disk, and I/O to this array is termed "raw I/O". 
# For example, some database systems prefer raw I/O because it enables them to control the exact disk location where each database record is stored.
# Raw I/O bypasses all the file-system services, such as the buffer cache, file locking, prefetching, space allocation, file names, and directories.
# We can make certain applications more efficiently by allowing them to implement their own special-purpose storage services on a raw partition.

# 10.5.2 Boot Block
# This initial "bootstrap" program tends to be simple
# To do its job, the bootstrap program finds the operating-system kernel on disk, loads that kernel into memory, and jumps to initial 
# the bootstrap is stored in "read-only memory" (ROM).
# And, since ROM is read only, it cannot be infected by a computer virus.
# The problem is that changing this bootstrap code requires changing the ROM hardwares

# Windows =>
# identified as boot aprtition - contains the operating system (作業系統) and device driver (裝置驅動程式)
# the windows system places its boot code in the first sector on the hard disk, which it terms the master boot record, MBR

# Note taht such a redirection by the controller could invalidate any opti
# logical block 17 becomes defective and the first available spare follows sector 202,
# 


### 10.6 Swap-Space Management
# swapping was first presented in Section 8.2, where we discussed moving entire processes between disk and main memory
# In practice, very few modern operating systems implement swapping in this fashion.
# Rather, systems now combine swapping with virtual memory 
# Swap-space management is another low-level task of the operating system.
# Virtual memory uses disk space as an extension of main memory.

# Note that it may be safer to overestimate than to underestimate the amount of swap space required, because if a system runs
# Overestimation wastes disk space that could otherwise be used for files, but it does no other harm
# Some operating systems - including Linux - allow the use of multiple swap spaces, including

# 10.6.2 Swap-Space Location
# A swap space reside in one of two places:it can be carved out of the normal file system, or it can be in a separate disk partition
# (1) file system
    # If the swap space is simply a large file within the file system, normal file-system routines can be used to create it, name it, and allocate its space.
    # Navigating the directory structure and the disk-allocation data structures takes time and extra disk accesses.
    # External fragmentation can greatly increase swapping times by forcing multiple seeks during reading and writing.
    # We can improve performance by caching the "block location information" in physical memory and by using special tools to allocate 
    # "physically contiguous blocks" for the swap file, but the cost of traversing the file-system data structures remains.

# (2) Separate Disk Partition
    # Alternatively, swap space can be created in a separate "raw partition".
    # No file system or directory structure is placed in this space.
    # Rather, a separate swap-space storage manager is used to allocate and deallocate the blocks from the raw partitions.
    # This manager uses algorithms optimized for speed rather than for storage efficiency, because swap space is accessed much more frequently than file systems
    # Since swap space is reinitialized at boot time, any fragmentation is short-lived.
    # The raw-partition approach creates a fixed amount of swap space during disk partitioning.
    # Adding more swap space requires either repartitioning the disk or adding another swap space elsewhere.
    # Some operating systems are flexible and can swap both in raw partitions and in file-system space.


# 10.6.3 Swap-Space Management: An Example
    # We can illustrate how swap space is used by following the evolution of swapping and paging in various UNIX systems.
    # The traditional UNIX kernel started with an implementation of swapping that copied entire processes between contiguous disk regions and 
    # UNIX later evolved to a combination of swapping and paging as paging hardware became available.
    
    # (1) Solaris
        # In Soalris 1 (SunOS), the desingers changed standard UNIX methods to improve efficiency and reflect technological developments.
        # When a process executes, text-segment pages containing code are brought in from the file system, accessed in main memory, and thrown away if selected for pageout.
        # It is more efficient to reread a page from the file system than to write it to swap space and then reread it from there.
        # Swap space is only used as a backing store for pages of anonymous memory, which includes memory allocated for the stack, heap, and uninitialized data of a process.
        # (for 動態產生的 stack, heap)

        # The biggest change is that Solaris now allocates swap space only when a page is forced out of physical memory, 
        # rather than when the virtual memory page is first created.

    # (2) Linux
        # Linux is similar to Solaris in that swap space is used only for "anonymous memory" - that is, memory not backed  by and file.
        # A swap area may be in either a swap file on a regular file system or a dedicated swap partition.
        # Each swap area consists of a series of 4-KB "page slots", which are used to hold swapped pages.
        # Associated with each swap area is a "swap map" - an array of integer counters, each corresponding to a page slot in the swap area.
        # If the value of a counter is 0, the corresponding page slot is available
        # Values greater than 0 indicate that the page slot is occupied by a swapped page.
        # For example, a value of 3 indicates that the swapped page is mapped to three different processes


### 10.7 RAID Structure
    # Having a large number of disks in a system presents opportunities for improving the rate at which data can be read or written, if the disks are operated in parallel.
    # Furthermore, this setup offers the potential for improving the reliability of data storage, because redundant information can be stored on multiple disks.
    # Thus, failure of one disk does not lead to loss of data.
    # A variety of disk-organization techniques, collectively called "redundant arrays of independent disks (RAID)"


### 10.7.1 Improvement of Reliability via Redundancy (Mirroring)
# The solution to the problem of reliability is to introduce "redundancy"; 
# we store extra information that is not normally needed but that can be used in the event of failure of a disk to rebuild the lost information.
# Thus, even if a disk fails, data are not lost.

# The simplest (but most expensive) approach to introducing redundancy is to duplicate every disk
# This technique is called mirroring
# With mirroring, a logical disk consists of two physical disks, and every write is carried out on both disks.
# The result is called a mirrored volume
# If one of the disks in the volume fails, the data can be read from the other

# The mean time to failure of a mirrored volume - where failure is the loss of data - depends on two factors
# (1) the mean time to failure of the individual disks
# (2) mean time to repair

# Even with mirroring of disks, if writes are in progress to the same block in both disks, and power fails before both blocks are fully written, the two blocks can be in an inconsistent state.
# One solution to this problem is to write one copy first, then the next.


### 10.7.2 Improvement in Performance via Parallelism (Striping)
# data striping consists of splitting the bits of each byte across multiple disks; such striping is called "bit-level striping."
# For example, if we have an array of eight disks, we write bit i of each byte to disk i.
# The array of eight disks can be treated as a single disk with sectors 

# One solution to this problem is to write one copy first, then the next.
# Another is to add a "solid-state nonvolatile RAM (NVRAM)" cache to RAID array.
# In "block-level striping", for instance, blocks of a file are striped across multiple disks; with n disks, block i of a file goes to disk (i % n) + 1
# Parallelism in a disk system, has two main goals:
    # (1) Increase the throughput of multiple small access (that is, page accesses) by load balancing
    # (2) Reduce the response time of large access.


### 10.7.3 RAID Levels
# Mirroring (Redundancy) provides high reliability, but it is expensive.
# Striping (Parallelism) provides high data-transfer rates, but it does not improve reliability. 
# Numerours schemes to provide redundancy at lower cost by using disk striping combined with "parity" bits (which we describe shortly) have been proposed.
# These schemes have different cost-performance trade-offs and are classified according to levels called "RAID levels."

# We describe the various levels here;

# (1) RAID Level 0: RAID level 0 refers to disk arrays with striping at the level of blocks but without any redundancy (such as mirroring of parity bits)
# (2) RAID Level 1: RAID level 1 refiers to disk mirroring.
# (3) RAID Level 2: RAID level 2 is also known as memory-style error-correcting-code (ECC) organization. Each byte in a memory system may have a parity bit associated with it 
    # that records whether the number of the bits in the byte is damaged, the parity of the byte changes and thus does not match the stored parity.
    # Similarly, if the stored parity bit is damaged, it does not match the computed parity.
    # Thus, all single-bit errors are detected by the memory system.
    # Error-correcting schemes store two or more extra bits and can reconstruct the data if a single bit is damaged.

# (4) RAID Level 3: Bit-Interleaved parity
    # If one of the sectors is damaged, we know exactly which sector it is, and we can figure out whether any bit in the sector is a 1 or a 0 
    # by computing the parity of the remaining bits is equal to the stored parity,
    # If the parity of the remaining bits is equal to the stored parity, the missing bit is 0; otherwise, it is 1.
    # RAID level 3 has two advantages over level 1.

    # First, the storage overhead is reduced because only one parity disk is needed for several regular disks, whereas one mirror disk is needed for every disk in level 1.
    # Second, since reads and writes of a byte are spread out over multiple disks with N-way striping of data, 
    # the transfer rate for reading or writing a single block is N times as afst as RAID level 1.
    
    # A further performance problem with RAID 3 - and with all parity - based RAID levels - is the expense of computing and writing the parity.
    # To moderate this performance penalty, many "RAID storage arrays" include a "hardware controller" with dedicated "parity hardware".
    # This controller offloads the parity computation from the CPU to the array.
    # The array has an "NVRAM cache" as well, to store the blocks while the parity is computed and to buffer the writes from the controller to the spindles.
    # In fact, a caching array doing parity RAID can outperform a non-caching non-parity RAID.
    # On the negative side, RAID level 3 supports fewer I/Os per second, since every disk has to participate in ever I/O request.

# (5) RAID Level 4: block-level striping , and in addition keeps a parity block on a separate disk for corresponding blocks from N other disks.
    # If one of the disks fails, the parity block can be used with the corresponding blocks from the other disks to restore the blocks of the failed disk.
    # A block read access only one disk, allowing other requests to be processed by the other disks.
    # Thus, the data-transfer rate for each access is slower, but multiple read accesses can proceed in parallel, leading to a higher overall I/O rate.
    # The transfer rates for large reads are high, since all the disks can be read in parallel.
    # Large writes also have high transfer rates.

    # Small independent writes cannot be performed in parallel. An operating-system write of data smaller than a block requires that the block be read, 
    # modified with the new data, and written back.
    # The parity block has to be updated as well.

# (6) RAID Level 5: Block-interleaved distributed parity
    # differs from level 4 in that it spreads data and parity among all N + 1 disks, rather than storing data in N disks and parity in one disk.
    # For each block, one of the disks stores the parity and the others sotre data.
    # For example, with an array of five disks, the parity fot then th block is sotre, the parity for the nth block is stored in disk (n mod 5)+1. The nth blocks of the other four disks store actual data for that block.

# (7) RAID Level 6: P + Q redundancy scheme, stores extra redundant information to guard against multiple disk failures
    # Instead of parity, error-correcting codes such as "Reed-Solomon codes" are used. 2 bits of redundant data are stored for every 4 bits of data - compared with 1 parity bit in level 5

# (8) RAID Level 0 + 1 and 1 + 0:
    # refers to a combination of RAID levels 0 and 1
    # RAID 0 provides the performance
    # RAID 1 provides the reliability
    # In RAID 0 + 1, a set of disks are striped, and then the stripe is mirrored to another, equivalent stripe.

    # Another RAID option that is becoming available commercially is RAID level 1 + 0, in which disks are mirrored in pairs and then the resulting mirrored pairs are striped.

# Volume-management software can implement RAID within the kernel or at the system software layer.
# In this case, the storage hardware can provide minimal features and still be part of a full RAID solution.
# Parity RAID is fairly slow when implemented in software, 
# Arrays can have multiple connections available or can be 

# Other features, such as snapshots and replication, can be implemented at each of these levels as well.

# A "snapshot" is a view of the file system before the last update took place.
# A Replication involves the automatic duplication of writes between separate sites for redundancy and disaster recovery.
    # (1) synchronous : each block must be written locally and remotely before the write is considered complete
    # (2) asynchronous : the writes are grouped together and written periodically

# if RAID is implemented in software, then each host may need to carry out and manage its own replication.
# If replication is implemented in the storage array or in the SAN interconnect layer

# One other aspect of most RAID implementation is a hot spare disk or disks.
# A hot spare is not used for data but is configured to be used as replacement in case of disk failure.
# For instance, a hot spare can be used to rebuild a mirrored pair should one of the disks in the pair fail.
# In this way, the RAID level can be reestablished automatically, without waiting for the failed disk to be replaced.

### 10.7.4 
# How do system designers choose a RAID level?
# One consideration is rebuild performance.
# If a disk fails, the time needed to rebuild its data can be significant.
# RAID level 0 is used in high-performance applications where data loss is not critical.
# RAID level 1 is popular for applications that require high reliability with fast recovery.
# RAID level 0 + 1 and 1 + 0 are used where both performance and reliability are important - for example - for small database.

# How many disks should be in a given RAID set ?
# How many bits should be protected by each parity bit ?
# If more disks are in an array, data-transfer rates are higher


### 10.7.5 Extensions
# The concepts of RAID have been generalized to other storage devices, including 
# Commonly, tape-drive robots containing multiple tape drives will stripe data across all the drives to increase throughput and decrease backup time

# A pointer to a file could be wrong, for example, or pointers within the file structure could be wrong
# Incomplete writes, if not properly recovered, could result in corrupt data.
# Some other process could accidentally write over a file system's structures, too.
# RAID protects against physical media errors, but not other hardware and software errors.

# The Solaris ZFS file system takes an innovative approach to solving these problems through the use of "checksums" - a technique used to verify the integrity of data
# These checksums are not kept with the block that is being checksummed.
# Rather, they are stored with the pointer to that block.

# If such factors are known ahead of time, then the disks and volumes can be properly allocated
# Some volume managers allow size changes, but some file systems do not allow for file-system growth or shrinkage.

# ZFS combines file-system management and volume management into a unit providing greater functionality than the traditional separation of those functions allows.
# Disks, or partitions of disks, are gathered together via RAID sets into pools of storage.
# The entire pool's free space is available to all file systems within that pool.
# ZFS uses the memory model of malloc() free() to allocate and release storage for each file system as blocks are used and freed within the file system.

### 10.8 Stable-Storage Implementation
# By definition, information residing in stable storage is never lost.
# To implement such storage, we need to replicate the required information on multiple storage devices (usually disks) with independent failure modes.
# We also need to coordinate the writing of updates in a way that guarantees that a failure during an update will not leave all the copies in a damaged state and that,
# when we are recovering from a failure, we can force all copies to a 

# (1) Successful completion => The data were written correctly on disk.
# (2) Partial Failure => A failure occurred in the midst of transfer, 
    # so only some of the sectors were written with the new data, 
    # and the sector being written during the failure may have been corrupted.
# (3) Total failure => The failure occured before the disk write started, so the previous data values on the disk remain intact.

# Whenever a failure occurs during writing of a block, the system needs to detect it and invoke a recovery procedure
# During recovery from a failure, each pair of physical blocks is examined.

# If both are the same and no detectable error exists, then no further action is necessary.
# If one block contains a detectable error then we replace its contents with the value of the other block.
# If neither block contains a detectable error, but the blocks differ in content, then we replace the content of the first block with that of the second.

# We can extend this procedure easily to allow the use of an arbitrarily large number of copies of each block of stable storage.
# Although having a large number of copies further reduces 

# Because waiting for disk writes to complete (synchronous I/O) is time consuming, many storage arrays add "NVRAM" as cache.
# Another is to add a solid-state nonvolatile RAM (NARAM) cache to the RAID array.
# Modern disk drives are structured as large one-dimensional arrays of logical disk blocks.

# Generally, these logical blocks are 512 bytes in size.
# Disks may be attached to a computer system in one of two ways 
# Defragmenting a badly fragmented file system can significantly improve performance, but the system may have reduced performance while the defragmentation is in progress.
# Finally, when a block is corrupted, the system must have a way to lock out that block or to replace it logically with a spare.

# Some systems dedicate a raw-disk partition to swap space, and others use a file within the file system instead.
# Still other systems allow the user or system administrator to make the decision

# Because of the amount of storage required on large systems, disks are frequently made reddundant via RAID algorithms.
# and even automatic recovery in the face of a disk failure.
# The operating system abstracts from the physical properties of its storage devices to define a logical storage unit, the file.
# Files are mapped by the operating system onto physical devices.

# From a user's perspective, a file is the smallest allotment of logical secondary storage; that is, data cannot be written to secondary storage unless they are within a file.
# Commonly, files represent programs and data
# Files may be free form, such as text files, or may be formatted rigidly.
# In general, a file is sequence of bits, bytes, lines or records, the meaning of which id defined by the file's creator and user.
# The concept of a file is thus extremely general.

# (1) A text file is a sequence of characters organized into lines (and possibly pages).
# (2) A source file is a sequence of functions, each of which is further organized as declarations followed by executable statements.
# An executable file is a series of code sections
# When a file is named, it becomes independent of the process, the user, and even the system that created it.

# Name => The symbolic file name is the only information kept in human-re
# Size => The current size of the file (in bytes, words, or blocks) and possibly the maximum allowed size are included in this attribute
# Protection => Access-control information determines who can do reading, writing, executing, and so on.
# Time, date, and user identification.

# Some newer file systems also support extend file attributes, including character encoding of the file and security features 
# The information about all files is kept in the directory structure, 

# 11.1.2 File Operations
# A file is an abstract data type.
# To define a file properly, we nned to con
# Let's examine what the operating system must do to perform each of these six basic file operations.

# Creating a file : Two steps are necessary to create a file. First, space in the file system must be found for the file.
# Writing a file : To write a file, we make a system call specifying both the name of the file and the information to be written to
# The system must keep a write pointer to the location in the file where the next write is to take place.

# Reading a file :
# To read from a file, we use a system call that specifies the name of the file and where (in memory) the next block of the file should be put
# Again, the directory is searched for the associated entry, 

# Most of the file operations mentioned involve searching the directory for the entry associated with the named file.
# To avoid this constant searching, many systems require that an "open()" system call be made before a file is first used.
# The operating system keeps a table, called the "open-file table"

# The "open()" operation :
    # (1) takes a file name
    # (2) searches the directory
    # (3) copying the directory entry into the open-file table.

# The "open()" call also accept access-mode information - create, read-only, read-write, append-only, and so on.
# This mode is checked against the file's permissions. If the request mode is allowed, the file is opened for the process.
# The "open()" system call typically returns a pointer to the entry in the open-file table.

# Typically, the operating system uses two levels of internal tables :
# (1) a per-process table : tracks all files that a process has open. is information regarding the process's use of the file.
# (2) system-wide table : contains process-independent information, such as the location of the file on disk, access dates, and file size.

# Once a file has been opened by one process, the system-wide table includes an entry for the file
# When another process executes an "open()" call, a new entry is simply added to the process's open-file table pointing to the appropriate entry in the system-wide table.


# In summary, several pieces of information are associated with an open file.
    # (1) File pointer : the system must track the last read-write location as a "current-file-position pointer" 代表目前 file 被讀或寫的位置，每個 process 都不一樣
        # This pointer is unique to each process operating on the file and therefore must be kept separate from the on-disk file attributes.
    
    # (2) File-open count : The file-open count tracks the number of opens and closes and reaches zero on the last close. The system can then remove the entry.
    
    # (3) Disk location of the file : Most file operations require the system to modify data within the file. 
        # The information needed to locate the file on disk is kept in memory so that the system does not have to read it from disk for each operation.
    
    # (4) Access rights : Each process opens a file in an access mode. This information is stored on the per-process table so the operating system can allow or deny subsequent I/O requests.

# Some operating system provide facilities for locking an open file .
# File locks allow one process to lock a file and prevent other processes from gaining access to it.
# File locks are useful for files that are shared by several processes 

# (1) Advisory => 
    # shared lock => is akin to a reader lock in that several processes can acquire the lock concurrently
    # it is up to software developers to ensure that locks are appropriately acquired and released.

# (2) Mandatory => 
    # exclusive lock => behaves like a writer lock; only one process at a time can acquire such a lock
    # once a process acquires an exclusive lock, the operating system will prevent any other process from accessing the locked file.
    # For example, assume a process acquires an exclusive lock on the file "system.log". If we attempt to open system.log from another process—for example, a text editor—the operating system will prevent access until the exclusive lock is released

# Furthermore, some measures must be taken to ensure that two or more processes do not become involved in a deadlock while trying to acquire file locks.

### 11.1.3 File Types
# A common technique for implementing file types is to include the type as part of the file name.
# The name is split into two parts - a name and an extension, usually separated by a period.
# Most operating systems allow users to specify a file name as a sequence of characters followed by a period and terminated by an extension made up of additional characters.
# Only a file with a .com, .exe, or .sh extension can be executed.
# Each file also has a creator attribute containing the name of the program that created it.
# This attribute is set by the operating system during the create() call, so its use is enforced and supported by the system.

# The UNIX system uses a crude "magic number" stored at the begining of some files to indicate roughly the type of the file - executable program, shell script, PDF file, and so on.

### 11.1.4 File Structure
# Further, certain files must conform to a required structure that is understood by the operating system.
# For example, the operating system requires that an executable file have a specific structure so that it can determine 
# where in memory to load the file and what the location of the first instruction is.
# If the operating system defines five different file structures, it needs to contain the code to support these file structures.

# text files (composed of ASCII characters separated by a carriage return and line feed)
# executable files

# The encrypted file is not ASCII text lines but rather is random bits.
# Each application program must include its own code to interpret an input file as to the appropriate structure.

# Disk systems typically have a well-defined block size determined by the size of a sector.