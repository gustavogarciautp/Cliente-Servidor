/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_client_ports;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.Scanner;

/**
 *
 * @author GustavoAdolfo
 */
public class RPC_client_ports {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        System.out.println("Ingrese el puerto");
        Scanner teclado = new Scanner(System.in);
        String port = teclado.nextLine();

        Socket sock = new Socket("192.168.0.13", Integer.parseInt(port));
        DataOutputStream output_server = new DataOutputStream(sock.getOutputStream());
        DataInputStream input_server = new DataInputStream(sock.getInputStream()); 
        String data, message;
        while (true){
            try{
                teclado = new Scanner(System.in);
                System.out.print("Mensaje: ");
                message = teclado.nextLine();
                System.out.println("sending "+ message);
                output_server.writeUTF(message);
                data = input_server.readUTF(); 
                //Se muestra por pantalla el mensaje recibido
                System.out.println(data);
                
            }
            catch (Exception exception){
                sock.close();
            }
                     
        }
    }
    
}
