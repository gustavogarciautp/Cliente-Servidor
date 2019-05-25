/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_server;

/**
 *
 * @author GustavoAdolfo
 */
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;
    public class accepting extends Thread{
    
        @Override
        public void run() 
        {
            try {
                int port=8000;
                ServerSocket sock= new ServerSocket(port);
                Socket connection =new Socket();
                while (true){
                    try{
                    System.out.println("waiting for a connection in port "+ Integer.toString(port));
                    connection= sock.accept();
                    System.out.println("connection from " + connection.toString());
                    
                    info thread = new info();
                    thread.connection = connection;
                    thread.start();
                    }
                    catch (Exception e){
                        System.out.println("Fin de la conexión");
                    
                        sock.close();
                    }
                    }  } catch (IOException ex) {
                Logger.getLogger(accepting.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
       
   }




