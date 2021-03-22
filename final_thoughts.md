# Final Thoughts

Overall the course was really inciteful. Nickolai Zeldovich and James Mickens are great lecturers, while most of the labs really interesting. Learning about how software can be abused to behave in unexpected ways, and defending against such attacks, has to be one of my most interesting learning experiences so far. I would highly recommend this course to anyone as an introduction to security concepts, but only after they have some exposure to operatings systems, networks(for lectures only), and web JavaScript. Knowledge on compilers helps a bit for security mechanisms as well.

## Labs
Labs 1, 4(skipped), and 5 focus on attacks, while 2, 3, and 6 focus on defense. These labs don't involve a lot of coding, but still requires deep understanding of the systems and concepts.

### Lab1 - Buffer Overflows
Easily my favorite lab. I got to inspect native code through GDB and had to be creative in coming up with different buffer overflow exploits.

### Lab2 - Privilege Separation
Introduces security mechanisms Unix-like kernels provide, using system calls like chroot, chown, setuid, and setgid. Lots of knowledge that should be applied to any security-sensitive application.

### Lab3 - Symbolic Execution
Least interesting lab that I could have skipped. Introduces symbolic execution, which although is a very interesting and useful problem, is probably too complicated to be introduced through a single lab/lecture.

### Lab4(skipped) - Attacking the Server
This labs focuses on theoretical attacks on a partner server. I skipped cause it sounds like a bust.

### Lab5 - Browser Security
Second most interesting after lab1 since it also focuses on attacks. Brings lights to all the potential vulnerabilities that exists on the web. These exploits were a lot easier to write than those in lab1 because its much easier to read/write JavaScript than assembly.

### Lab6 (JavaScript Sandboxing)
Interesting problem in sandboxing user provided JavaScript code such that it is only able to alter the JavaScript state within the sandbox. Very interesting problem, but I think it should be avoided in practice since there are so many ways a user might try to escape the sandbox. Best approach is to never let your users run any JavaScript.
