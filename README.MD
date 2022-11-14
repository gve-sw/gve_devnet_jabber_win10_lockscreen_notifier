# GVE DevNet Jabber Win10 Lockscreen Notifier

The purpose of this sample code is to show how you can use a Jabber custom tab to obtain incoming call notifications via a Javascript function and invoke a local web server that can relay those notifications across a Windows 10 lock screen which is something that Jabber for Windows cannot do natively. 

## Contacts
* Gerardo Chaves (gchaves@cisco.com)

## Solution Components
* Cisco Jabber for Windows

## Sandbox

You can use any dCloud demo that contains Jabber 12 or later for Windows to test this sample code such as the [Cisco Collaboration 12.5 v1 - Transform Work with Collaboration](https://dcloud2-rtp.cisco.com/content/demo/578984?returnPathTitleKey=content-view) demo. 


## Installation

1. Make sure you have [Python 3.10 or later](https://www.python.org/downloads/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

2. Create and activate a virtual environment for the project ([Instructions](https://docs.python.org/3/tutorial/venv.html)).

3. Access the created virtual environment folder
    ```
    cd [add name of virtual environment here] 
    ```

4. Clone this Github repository:  
  ```git clone [add github link here]```
  * For Github link: 
      In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**  
     
  * Or simply download the repository as zip file using 'Download ZIP' button and extract it

5. Access the downloaded folder:  
    ```cd gve_devnet_jabber_win10_lockscreen_notifier```

6. Install all dependencies:  
  ```pip install -r requirements.txt```

7. Run the flask application 
  ```python3 app.py```

8. Create a new custom tab on the Jabber for Windows client on the machine where you have installed the code and , ssuming you kept the default parameters for starting the Flask application, use the following address on the URL field for the new Tab:  
https://localhost:5500

9. Lock the screen on the Windows 10 client machine and place a call to the extension that the Jabber client has configured and confirm you can see an incoming call notification. 


## Screenshots



### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.