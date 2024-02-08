import { ConnectedSocket ,OnConnect, SocketController } from 'socket-controllers';

@SocketController()

class MainController {
    @OnConnect()
    public connection(@ConnectedSocket() socket: any) {
        console.log('Client connected: ' + socket.id);
    }
}}