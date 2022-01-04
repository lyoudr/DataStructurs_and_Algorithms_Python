# Partitioning is useful for limiting the sizes of individual file systems.
# putting multiple file-system types on the same device, or leaving part of the device available for other uses, such as swap space or 

### Volume
# Any entity containing a file system is generally known as "volume".
# Each volume can be thought of as a virtual disk.
# Volumes can also store multiple operating systems, allowing a system to boot and run more than one operating system.

# Each volume that contains a file system must also contain information about the files in the system.
# 每個含有 file system 的 volume，也必須包含在那個 file system 的 file 的資訊
# 這些資訊通常被儲存在 device directory or volume table of contents.

# 11.3.1 Storage Structure
# objfs - a "virtual" file system (essentially an interface to the kernel that looks like a file system) that gives debuggers access to kernel symbols
# ctfs - a "virtual" file system that maintains "contract" information to manage which processes start when the system boots and must continue to run during operation


# 11.3.3 Single-Level Directory
# All files are contained in the same directory, which is easy to support and understand
# leads to confusion of file names among different users, The standard solution is to create a separate directory for each user.

# 11.3.4 Two-Level Directory
# master file directory (MFD) 
# each user has his own "user file directory (UFD)"

# The program creates a new UFD and adds an entry for it to the MFD
# The execution of this program might be restriceted to system administrators.

# 11.3.5 Tree-Structured Directories
# Once we have seen how to view a two-level directory as a two-level tree, the natural generalization is to extend the directory structure to a tree of arbitrary height
# A tree is the most common directory structure.
# The tree has a root directory, and every file in the system has a unique path name

# A directory (or subdirectory) contains a set of files or subdirectories.
# One bit in each directory entry defines the entry as file (0) or as a subdirectory (1)

# In normal use, each process has a current directory.
# The current directory should contain most of the files that are of current interest to the process.
# When reference is made to a file, the current directory is searched.
# If a file is needed that is not in the current directory, then the user usually must either specify a path name or change the current directory to be the directory holding that file.
# To change directories, a system call is provided that takes a directory name as a parameter and uses it to redefine the current directory

# The initial current directory of a user's login shell is designated when the user job starts or the user logs in.
# The operating system searches the accounting file

# Allowing a user to define her own subdirectories permits her to impose a structure on her files.
# This structure might result in separate directoreis for files associated with different topics or different forms of information

# An interesing policy decision in a tree-structured directory concerns how to handle the deletion of a directory.
# If a directory is empty, its entry in the
# Some systems will not delete a directory unless it is empty.
# Thus, to delete a directory, the user must first delete all the files in that directory.
# This approach can result in a substantial amount of work.
# An alternative approach, such as that taken by the UNIX rm command, is to provide an option: 
# when a request is made to delete a directory, all that directory's files and subdirectories are also to be deleted.

# With a tree-structured directory system, users can be allowed to access, in addition to their files, the files of other users.
# For example, user B can access a file of user A by specifying its path names.
# User B can specify either an absolute or a relative path name.
# Alternatively, user B can change her current directory to be user A's directory and access the file by its file names.

# 11.3.5 Acyclic-Graph Directories
# Consider two programmers who are working on a joint project.
# The files associated with that project can be stored in a subdirectory, separating them from other projects and files of the two programmers.
# But since both programmers are equally responsible for the project, both want the subdirectory to be in their own directories.
# In this situation, the common subdirectory should be "shared".
# A shared directory or file exists in the file system in two places at once.

# It is important to note that a shared file is not the same as two copies of the file 
# With a shared file, only one actual file exists, so any changes made by one person are immediately visible to the other.
# Sharing is particularly important for subdirectories; a new file created by one person will automatically appear in all the shared subdirectories.

# Shared files and subdirectories can be implemented in several ways.
# A common way, exemplified by many of the UNIX systems, is to create a new directory entry called a link.
# A link is effectively a pointer to another file or subdirectory.
# For example, a linke may be implemented as an absolute or a relative path name.
# When a reference to a file is made, we search the directory.
# Links are easily identified by their format in the directory entry

# An acyclic-graph directory structure is more flexible than a simple tree structure,
# but it is also more complex.
# A file may now have multiple absolute path names.
# Consequently, 
# When can the space allocated to a shared file be deallocated and reused?

# One possibility is to remove the file whenever anyone deletes it, but this action may leave dangling pointers to the now-nonexisting file.

# In a system where sharing is implemented by symblic links, this situation is somewhat easier to handle.
# The deletion of a link need not affect the original file; only the link is removed.

# If the file entry itself is deleted, the space for the file is deallocated, leaving the links dangling.

# We can search for these links and remove them as well, but unless a list of the associated links is kept with each file,
# Alternatively, we can leave the links until an attempt is made to use them.
# At that time, we can determine that the file of the name given by the link does not exist and can fail to resolve the link name;

# In the case of UNIX, symbolic links are left when a file is deleted, and it is up to the user to realize that the original file is goen or has been replace.

# Another approach to deletion is to preserve the file until all references to it are deleted.
# To implemented that the last reference to the file has been deleted.

# When a link or a copy of the directory entry is established, a new entry is added to the file-reference list.
# The UNIX operating system uses this approach for nosymbolic links

# 11.3.7 General Graph Directory
# A serious problem with using an 

# 11.3.6 Acyclic-Graph Directories
# A tree structure prohibits the sharing of files or directories.
# An "acyclic-graph" - that is, a graph with nocycles -allows directoreis to share 

### Symbolic links => 
# 1. The deletion of a link need not affect the original file; only the link is removed, leaving the links dangling
# 2. If the file entry itself is deleted, the space for the file is deallocated, leaving the links dangling.
# leave the links until an attempt is made to use them. At that time, we can determine that the file of the name given by the link does not exist and fail to resolve the link name.

### A list of all reference to a file (Hard Links or Nonsymbolic links)
# When a link or copy of the directory entry is established , a new entry is added to the file-reference list.
# When a link or directory entry is deleted, we remove its entry on the list. The file is deleted when its file-reference list is empty.
# Deleting a link or entry decrements the count.
# When the count is 0, the file can be deleted; there are no remaining references to it.
# A poorly designed algorithm might result in an infinite loop continually searching through the cycle and never terminating.
# One solution is to limit arbitrarily the number of directories that will be accessed during a search

# when cycles exist, the reference count may not be 0 
# we generally need to use a garbage collection scheme to determine when the last reference has been deleted and the disk space can be reallocated.
# Garbage collection involves traversing the entire file system, marking 

# 11.4 File-System Mounting
# a file system must be mounted before it can be available to processes on the system.
# The directory structure may be built out of multiple volumes

# Mouting Porcess
# (1) mount point - the location within the file structure where the file system is to be attaced.
#  ex : 將一套 file system 放在 (mount) /home (mount point) 底下

# (2) OS 會 verifies that the device contains a valid file system.
# It does so by asking the device driver to read the device directory and verifying that the directory has the expected format.
# a system may disallow a mount over a directory that contains files; or it may make the mounted file 


#### 11.5 File Sharing
### 11.5.1 Multiple Users
# To implement sharing and protection, the system must maintain more file and directory attributes than are needed on a single-user system.
# owner => is the user who can change attributes and grant access and who has the most control over the file
# group => 


### 11.5.2 Remote File Systems 
# With the adment of networks, communication among remote computers became possible.
# ftp: Networking allows the sharing of resources spread across a campus or even around the world
# The second major method uses a "distributed file system (DFS)"

# 11.5.2.1 The Client-Server Model
# Generally, the server declares that a resource is available to clients
# More secure solutions include secure authentication of the client via encrypted keys.
# In the case of UNIX and its network file system (NFS), 
# authentication takes place via the client networking information, 
# by default. In this scheme, the user’s IDs on the client and server must match

# 11.5.2.2 Distributed Information Systems
# To make client-server systems easier to manage, distributed information systems, also known as distributed naming services, provide unified access to the information needed for remote computing.
# "The domain name system" (DNS) provides host-name-to-network-address translations for the entire Internet.

# Other distributed information system provide user name/password/user ID/group ID
# In the case of Microsoft's "common Internet file system (CIFS)", network information is used in conjunction with user authentication (user name and password) to create a network login.

# The industry is moving toward use of the lightweight directory-access protocal (LDAP).
# Conceivably, one distributed LDAP directory could be used by an organization to store all user and resource information for all the organization’s computers.
# The result would be secure single sign-on for users, who would enter their authentication information once for access to all computers within the organization.


# 11.5.2.4 Failure Modes
# Rather, the system can either terminate all operations to the lost server or delay operations until the server is again reachable
# These failure semantics are defined and implemented as part of the remote-file-system protocol.
# most DFS (distributed file system) protocals either enforce or allow delaying of file-system operations to remote hosts, with the hope that the remote host will become available again.

# some kind of state information may be maintained on both the client and the server.
# NFS takes a simple approach
# "stateless DFS" => In essence, it assumes that a client request for a file read or write would not have occurred unless the file system had been remotely mounted and the file had been previously open.
# Simiarly, it does not track 

### 11.5.3 Consistency Semantics
#  These semantics specify how multiple users of a system are to access a shared file simultaneously.
# In particular, they specify when modifications of data by one user will be observable by other users. These semantics are typically implemented as code with the file system.

# 11.5.3.1 UNIX Semantics
# Writes to an open file by a user are visible immediately to other users who have this file open.
# One mode of sharing allow users to share the pointer of current location into the file.
# Thus, the advancing of the pointer by one user affects all sharing users.
# a file is associated with a single physical image that is accessed as an exclusive resource.
# Contention for this single image causes delays in user processes.

# Exclusive 的模式，同時只有一個 user 能寫入此 file
# 且只要一修改 file, 其他 user 都可以馬上看到

# 11.5.3.2 Session Semantics 
# 1. Writes to an open file by a user are not visible immediately to other users that have the same file open
# 2. Once a file is closed, the changes made to it are visible only in sessions starting later. Already open instances of the file do not reflect these changes.
# like version control , one file has multiple image
# . Consequently, multiple users are allowed to perform both read and write accesses concurrently on their images of the file, without delay

# 11.5.3.3 Immutable-Shared-Files Semantics
# Once a file is declared as shared by its creator, it cannot be modified.


#### 11.6 Protection

# Reliablility is generally provided by duplicate copies of files.
# Many computers have systems programs that automatically copy disk files to tape at regular intervals to maintain a copy should a file system be accidentally destroyed.

# 11.6.1 Types of Access
# Read - Read from the file
# Write - Write or rewrite the file
# Execute - Load the file into memory and execute it.
# Append - Write new information at the end of the file.
# Delete - Delete the file and free its space for possible reuse.

# 11.6.2 Access Control
# different users may need different types of access to a file or directory.
# The most general scheme to implement identity-dependent access is to associate with each file and directory an "access-control list (ACL)" specifying user names and the types of access allowed for each user.

# Owner - The user who created the file is the owner
# Solaris gives ACLs precedence.
# This follows the general rule that specificity should have priority.

### 11.6.3 Other Protection Approaches
# Another approach to the protection problem is to associtate a password with each file.
# Similarly, if a path name refers to a file in 