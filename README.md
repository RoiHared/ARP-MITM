# ARP-MITM

## Introduction
**ARP Protocol -**
ARP acronym stands for Address Resolution Protocol, it’s a protocol that enables
network communications between devices. ARP used to translate Internet Protocol (IP)
addresses (IPv4) to a physical machine address, also known as a Media Access Control
(MAC) address, in a local-area network. Usually, ARP used in devices to communicate
the router that enables those devices to connect to the Internet.

**ARP Poisoning/Spoofing -**
ARP Poisoning/Spoofing is a type of Man in the Middle (MitM) attack, that allows
hackers to spy on communications between two parties over a Local Area Network
(LAN). Because the designers of the ARP protocol never included an authentication
system to validate ARP messages, any device on the same network can answer an ARP
request, even though the original message is not requested for it.

## Requirements
- Kaly Linux virtual machine
- Windows virtual machine


## Installation

To complit

## Usage

To run the program, you will need to run it as root. You can use the following command:
```bash
python3 arp_spoof.py
python3 packet_sniffer.py
