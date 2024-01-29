import socket


def deactivate_screensaver(ip_adr):
    # create an udp broadcast socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # send the message "PIR raised", 12-bytes long
    message = "504952207261697365640d0a"
    message_bytes = bytes.fromhex(message)
    udp_socket.sendto(message_bytes, (ip_adr, 2311))

    # print and close
    print("screensaver deactivated...")
    udp_socket.close()


if __name__ == "__main__":
    broadcast_ip = "192.168.178.255"
    deactivate_screensaver(broadcast_ip)
