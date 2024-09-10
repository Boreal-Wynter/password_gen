
# Password Generator Application

When I was using my iPhone to create a new account, I made the observation of how most of passwords generated by apple have a similar structure. this observation has led me to create my own simple password generator!



## Deployment

To run this project just click this button here! [Click to See Application!](https://github.com/Boreal-Wynter/password_gen/blob/1ae82839611a72b203ad1503547f7d7ae576af5b/generate_password.exe)

<a href="generate_password.exe" download>Download Program!</a>


## Lessons Learned

1. Creating the Password

The overall structure of a Apple Password. Each password contains: 

 * One Number
 * One Upper-Case Letter
 * Sixteen Lower-Case Letters
 * Two Hyphens

#### Why?

The reason why Apple generates passwords this way is becasue it has high `entropy`. Entropy is the measure of a password strength against different forms of password cracking. This is important because as we continue along in our life, coputers and their computing increase resulting in less time needed to guess a large amount of passwords.

Given that the possible number of symbols for a password is 64 and the length of any password created is 20,

entropy = log<sub>2</sub>(64<sup>20</sup>)

resulting in the bits of entropy being around 120 bits which is very strong.

2. Tkinter

Tkinter is a pre-installed GUI library included with Python that is simple to use for a beginner like me! Applications using tkinter are also cross-platform compatable and are easy to understand! Somthing I like about tkinter is how it handled the layout and sizing the widgets I created with ease. All in all, it was a great library to use that help me build this small application.

3. pyinstaller

Using pyinstaller was a breeze to use and help me turn my program into an executable file that anyone can use! This application removes the need of having python and any dependencies to run the program, reducing time and hassle on other users part! 
## Screenshots

![App Screenshot](https://github.com/Boreal-Wynter/password_gen/blob/902caabe2acb2c1a0402007305d3dc93004c74a3/Application.png)


## Acknowledgements

 - Thank you dafarry and Python.org for creating great documentation for Tkinter so I can create this simple application! 
   - [dafarry](https://dafarry.github.io/tkinterbook/)
   - [python docs](https://docs.python.org/3/library/tk.html)

 - Thank you Katherine Oelsner for creating a wonderful website to cleanly write good README.md files!
   - [readme.so](https://readme.so/)

 - Thanks Apple for creating a short blog on how your passwords are created.
   - [Apple Support](https://support.apple.com/guide/security/automatic-strong-passwords-secc84c811c4/web)
