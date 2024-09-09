# Network Security: ARP MitM

## Introduction
### ARP Protocol
ARP acronym stands for Address Resolution Protocol, it’s a protocol that enables network communications between devices. ARP used to translate Internet Protocol (IP) addresses (IPv4) to a physical machine address, also known as a Media Access Control (MAC) address, in a local-area network. Usually, ARP used in devices to communicate the router that enables those devices to connect to the Internet.
The host is maintaining an ARP cache and use it to connect to websites and other destinations on the network. However, if host doesn’t have the MAC address for an IP address, it will ask other machines on the network for a matching MAC address by sending an ARP request packet
The ARP protocol is not good in security aspect. That’s why IPv6 comes with newer protocol named as, Neighbor Discovery Protocol (NDP). The Neighbor Discovery Protocol is very strong in security aspect and uses cryptographic keys to verify host identities.

### ARP Poisoning/Spoofing
ARP Poisoning/Spoofing is a type of Man in the Middle (MitM) attack, that allows hackers to spy on communications between two parties over a Local Area Network (LAN). Because the designers of the ARP protocol never included an authentication system to validate ARP messages, any device on the same network can answer an ARP request, even though the original message is not requested for it.
This project aims to demonstrate the concepts of ARP spoofing and HTTP traffic sniffing using Python and the Scapy library. The tools developed in this project allow for network traffic interception and analysis in a local network. The project provides hands-on experience with network protocols and the practical implementation of security concepts.
### Tools Overview
1.	ARP Spoofing Tool: This tool enables a Man-in-the-Middle (MITM) attack by sending malicious ARP replies to redirect network traffic between a target device and the router through the attacker's machine. It allows the attacker to intercept or manipulate the traffic.
2.	HTTP Sniffer Tool: This tool captures and analyzes HTTP requests in real-time, identifying URLs and potential login credentials such as usernames and passwords from the captured traffic.
### Project Goals
•	Understand and implement ARP spoofing to perform MITM attacks.
•	Develop a network sniffer capable of extracting useful information from HTTP traffic.
•	Gain practical experience with network protocols and security vulnerabilities.
•	Learn how to mitigate these vulnerabilities through a deeper understanding of network security.

## Usage Instructions
### Prerequisites:
- Python 3.x
- Scapy library (usually the library is already included in Kaly Linux)
- Administrator/root privileges to run the script.
- It is recommended to use a Kali Linux virtual machine and a Windows 10 virtual machine with NAT networking settings.
   - Download Kali Linux image: https://www.kali.org/get-kali/#kali-installer-images
   - Download Windows10 iso:   https://www.microsoft.com/software-download/windows10

### Running the ARP spoof tool:
1.	Open a terminal in Kali Linux and navigate to the directory containing the script arp_spoof.py.
2.	Execute the script using the following command:
    ```terminal 
    python3 arp_spoof.py -t <target_ip> -r <gateway_ip>
    ```
    Replace <target_ip> with the IP address of the target machine and <gateway_ip> with the IP address of the 
    router (gateway).

    Example:
     ```terminal 
    python3 arp_spoof.py -t 10.0.2.4 -r 10.0.2.1
    ```
 
3.	The script will begin sending ARP packets and will print the number of packets sent in real-time.
4.	To stop the attack, press CTRL + C. The script will automatically restore the ARP tables of the target and the router to their original state.
### Running the HTTP Sniffer tool:
1.	While the ARP spoofing tool is running, open a new terminal and navigate to the directory containing the script packet_sniffer.py.
2.	Execute the script using the following command:
    ```terminal 
    python3 packet_sniffer.py -t <interface>
    ``` 
    Replace <interface> with the name of the network interface you wish to sniff on (e.g., eth0, wlan0).

    Example:
     ```terminal 
    python3 packet_sniffer.py -i eth0
    ``` 
 
3.	The script will capture and print HTTP requests in real-time, showing the URLs accessed and any potential login credentials found in the traffic.
### Demonstration:
To verify that the script works as intended:
1.	From the Windows virtual machine, open a browser and navigate to [http://testphp.vulnweb.com/login.php](http://testphp.vulnweb.com/login.php)
2.	Enter any login details on the website.
3.	The credentials you entered should appear in the Linux terminal running the sniffer script.

## Project Execution: Challenges and Solutions
### Challenges Faced
1.	Understanding ARP and HTTP Protocols: One of the initial challenges was gaining a deep understanding of how the ARP and HTTP protocols work. ARP, being a low-level protocol, required a good grasp of network fundamentals. HTTP, though simpler, required understanding the structure of requests and responses to effectively extract useful data.
2.	Handling Scapy Warnings and Errors: During the implementation of the ARP spoofing tool, warnings from Scapy were a recurring issue. For instance, warnings related to MAC address resolution were common. These were addressed by ensuring that the get_mac() function reliably fetched MAC addresses and by suppressing non-critical warnings to maintain focus on the core functionality.
3.	Packet Decoding Issues: In the HTTP sniffer, decoding raw packet data posed a challenge, especially when dealing with non-ASCII characters in HTTP requests. This was resolved by carefully handling string encoding and decoding, ensuring that packets were processed without errors.
4.	Ensuring Script Robustness: Another challenge was ensuring that the scripts handled network changes or interruptions gracefully. For example, if a packet was lost or a target went offline, the script needed to handle these situations without crashing. Implementing error handling mechanisms, such as checking for valid MAC addresses and handling exceptions, was crucial.
5.	Balancing Performance and Functionality: Ensuring that the scripts performed well without missing packets while maintaining accuracy in detecting login information required tuning the timing and packet capture logic. This balance was achieved through iterative testing and refinement.
### Solutions and Learning Outcomes
1.	Iterative Testing and Debugging: The project emphasized the importance of iterative testing. By gradually building up the scripts and testing each component, it was easier to identify and fix issues early in development.
2.	Effective Use of Scapy: Mastering Scapy was a significant part of the project. The library’s flexibility allowed for effective packet manipulation and analysis, but it also required careful handling of its functions and options.
3.	Security Awareness: Through this project, the importance of network security became more apparent. Understanding how easy it can be to perform attacks like ARP spoofing and HTTP sniffing underlined the need for robust security measures, such as HTTPS and secure ARP protocols.
4.	Code Structure and Readability: Writing clean, modular code was essential in making the scripts maintainable and understandable. Functions were kept small and focused, making it easier to debug and extend the functionality if needed.

## Conclusion
This project provided valuable insights into network security and the vulnerabilities that can exist within local networks. Through practical implementation, it was possible to see firsthand how attacks like ARP spoofing and HTTP sniffing are conducted and, more importantly, understand how to defend against such attacks. This experience highlighted both the power and responsibility that come with understanding network security at a deep level.

## Future Work
In the future, this project could be expanded to include:
- HTTPS Sniffing (with SSL stripping): Investigate methods to intercept HTTPS traffic, such as SSL stripping.
- Automated Mitigation Tools: Develop scripts or tools to detect and mitigate ARP spoofing attacks in real-time.
- Cross-Platform Compatibility: Ensure the tools work across different operating systems, not just Linux-based environments.

## Legal Disclaimer
This project is intended for educational purposes only. Unauthorized use of these tools on networks you do not own or have explicit permission to test is illegal and unethical. Always ensure you have the proper authorization before conducting any network security tests.





