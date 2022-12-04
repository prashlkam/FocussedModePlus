# FocusedModePlus
A tool that could help persons with Autism to Focus more only on a certain part of the screen, by reducing unnecessary distractions on the Screen.....

## What is FocusedModePlus
---------------------

Autism spectrum disorder (ASD) is a developmental disability caused by differences in the brain. People with ASD often have problems with social communication and interaction, and restricted or repetitive behaviors or interests. People with ASD may also have different ways of learning, moving, or paying attention.

Technology has helped Autism in many ways...

Video on How to Diagnoze Autism with Computers (and Machine Learning)
[!Youtube Video](https://www.youtube.com/watch?v=YQpTlnWYAqE&t=196s)

Apart from this, there are various software applications available for persons with Autism. Broadly the softwares can be classified into the following Catagories...

 > Autism Diagnosis / Training / Early Intervention (for Parents)
 > Communication / Assistive Aids
 > Early Schooling / Educational Aids
 > Entertainment / Recreational software
 > Other Tools / Utilities
 
For a Curated list of Software Solutions for Autism - you may refer to the following URL...

http://www.mousetrial.com/autism_software.html

Issues faced by Users of Software (with Autism)
---------

Clutter can be a huge stressor for people with autism because it can contribute to sensory overload and overall stress levels. An unorganized and messy space (a cluttered desktop for instance) can also make simple tasks more difficult because a larger amount of time may need to be dedicated to finding needed files / items.

A user posted the following comments on reddit...
"Yes, but I also have ADHD. I simultaneously want a clean space but will treat clutter as invisible.

When I finally "see" clutter, I will start so rapidly and thoroughly cleaning that I get overwhelmed and then I'll be so burnt out that I can't even consider the thought of cleaning for days. When this happens, I usually end up undoing some of the cleaning I did accomplish."

Source: https://www.reddit.com/r/AutismTranslated/comments/vlxhcg/do_anyone_else_get_super_overstimulated_by_visual/

Another issue is Pop-ups / Notifications. When Pop-ups / Notifications appear - users can easily get distracted by them and lose focus on the Activity that they're currently performing. Persons with Autism can also get overwhelmed by these Pop-ups / Notifications - and not be in a position to decide what to do next.

Focus Assist on Windows 10
---------
The Focus Assist feature was originally introduced as ‘Quiet Hours’ in previous versions of Windows 10. This feature enables you to avoid unnecessary notifications while you are carrying out a task that demands your focus. You get flexibility in deciding the degree of suppression of notifications. You may maintain a priority list or completely avoid notifications.

In the Focus Assist section, you will also find a heading named Automatic rules. Here you can make the Windows learn the conditions that should enable the Focus Assist automatically. You get the following four conditions to set.

  - During these times: You can set the desired time during which you don’t want any distraction from notifications.
  - When I’m duplicating my display: Enabling this option suppresses notifications as long as you’re projecting your monitor to an external screen.
  - When I’m playing a game: This option prevents notifications while you play games in full-screen mode.
  - When I’m using an app in full-screen mode: This option also blocks notifications as long as you’re using an app in full-screen mode.

For a full run down on how to use Focus Assist - please visit the following URLs...

  1. https://www.gadgetbridge.com/how-to/what-is-focus-assist-in-windows-10-and-how-to-enable-it/
  2. https://blogs.microsoft.com/accessibility/m365-accessibility-spring-2022/
  3. or just Google for "Focus Assist on Windows 11"...

FocusedModePlus
--------

Consider the following images / screenshots...

<img src="./content/inde6556y77t6x.png", width="800", hight="600">
Img 1 - Cluttered desktop with too many files

<img src="./content/ind555y67ex.jpg", width="800", hight="600">
Img 2 - Cluttered desktop with too many open Apps

<img src="./content/images7yuhgbhju7y78uhy66tyu7uybh.jpg", width="800", hight="600">
Img 3 - Cluttered toolbars with too many buttons (eg. Adobe Photoshop toolbars over various versions)
----------------

Clutter is a Reality in life. Eliminating clutter might be possible in some cases - but more difficult in others.

The way we deal with clutter on the Desktop - needs to be reimagined...

FocusedModePlus is just such an Attempt...

## FocusedModePlus features
 - FocusedModePlus tries to reduce distractions by focusing only on a small part of the screen
 - when FocusedModePlus is run - it places a fullscreen, always-on-top, borderless and blank window over the screen
 - a small part of this blank window is Transparent - through which anything that is in the background can be seen
 - the Transparent area moves wherever the mouse cursor is moved
 - the Transparent area can also be moved - by using the Arrow keys on the keyboard
 - the Transparent area can also be resiized horizontally - use the `-` key to reduce the width and the `=` key to increase width
 - the Transparent area can also be resiized vertically - use the `[` key to reduce the hight and the `]` key to increase hight
 - the whole blank window can be Minimized - by pressing the `m` key

## Setup
-----------
 follow these steps to install FocusedModePlus on your system...
 - install python
 - install pygame using pip
```
pip install pygame
```
 - install pywin32 using pip
```
pip install pywin32
```
 - do a git clone of this project - in a directory of your choice
```
git clone  https://github.com/prashlkam/FocusedModePlus
```
 - open windows cmd prompt and navigate to the directory where you saved the project...
```
cd C:\<where you saved the project>
```
 - now Run the program...
```
python3 .\focussedmodeplus.py
```
