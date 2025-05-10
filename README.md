# Simple Echo Server

- Simple echo server is a basic server that echoes back the message it receives from the client.

- Analyze network traffic  between server and client using tcpdump

## How to run

```bash
python3 echo_server.py
```

## How to run client
open new terminal and run
```bash
python3 echo_client.py
```

## Capture Data
Open new terminal and run
Install tcpdump package in Linux System if not installed
```bash
sudo apt install tcpdump    
```
Capture data on part 6542 and save to file name capture.pcap
```bash
sudo tcpdump -i any port 6542 -s 0 -vA -w capture.pcap
```
### Analyze Data
At the same terminal where you run the capture command, In current directory,to read the capture.pcap file
```bash
tcpdump -nn -r capture.pcap -A
```

Output will be like this
```bash
shot length 262144
Warning: interface names might be incorrect
11:11:02.375885 lo    In  IP 127.0.0.1.60990 > 127.0.0.1.6542: Flags [S], seq 3700300803, win 65495, options [mss 65495,sackOK,TS val 3623601823 ecr 0,nop,wscale 7], length 0
E..<c.@.@............>...............0.........
............
11:11:02.375917 lo    In  IP 127.0.0.1.6542 > 127.0.0.1.60990: Flags [S.], seq 381104031, ack 3700300804, win 65483, options [mss 65495,sackOK,TS val 3623601823 ecr 3623601823,nop,wscale 7], length 0
E..<..@.@.<............>../..........0.........
............
11:11:02.375940 lo    In  IP 127.0.0.1.60990 > 127.0.0.1.6542: Flags [.], ack 1, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 0
E..4c.@.@............>......../......(.....
........
11:11:02.375985 lo    In  IP 127.0.0.1.60990 > 127.0.0.1.6542: Flags [P.], seq 1:13, ack 1, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 12
E..@c.@.@............>......../......4.....
........Hello, world
11:11:02.375994 lo    In  IP 127.0.0.1.6542 > 127.0.0.1.60990: Flags [.], ack 13, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 0
E..4..@.@.i............>../..........(.....
........
11:11:02.376141 lo    In  IP 127.0.0.1.6542 > 127.0.0.1.60990: Flags [P.], seq 1:13, ack 13, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 12
E..@..@.@.i............>../..........4.....
........Hello, world
11:11:02.376159 lo    In  IP 127.0.0.1.60990 > 127.0.0.1.6542: Flags [.], ack 13, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 0
E..4c.@.@............>......../......(.....
........
11:11:02.376232 lo    In  IP 127.0.0.1.60990 > 127.0.0.1.6542: Flags [F.], seq 13, ack 13, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 0
E..4c.@.@............>......../......(.....
........
11:11:02.376264 lo    In  IP 127.0.0.1.6542 > 127.0.0.1.60990: Flags [F.], seq 13, ack 14, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 0
E..4..@.@.i............>../..........(.....
........
11:11:02.376285 lo    In  IP 127.0.0.1.60990 > 127.0.0.1.6542: Flags [.], ack 14, win 512, options [nop,nop,TS val 3623601823 ecr 3623601823], length 0
E..4c.@.@............>......../......(.....
........
'''

- How to read tcpdump output
In tcpdump output, each line represents a packet and contains the following information:
(Note: server is served at port 6542 , client is served at port 60990 )

| Step | Description                          | Flags  |
| ---- | ------------------------------------ | ------ |
| 1    | Client sends SYN                     | `[S]`  |
| 2    | Server responds with SYN-ACK         | `[S.]` |
| 3    | Client sends ACK (handshake done)    | `[.]`  |
| 4    | Client sends "Hello, world"          | `[P.]` |
| 5    | Server ACKs receipt                  | `[.]`  |
| 6    | Server sends "Hello, world" back     | `[P.]` |
| 7    | Client ACKs reply                    | `[.]`  |
| 8    | Client sends FIN to close connection | `[F.]` |
| 9    | Server replies with FIN              | `[F.]` |
| 10   | Client ACKs server FIN               | `[.]`  |



