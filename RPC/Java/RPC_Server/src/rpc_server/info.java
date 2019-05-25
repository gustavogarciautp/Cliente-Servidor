/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_server;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author GustavoAdolfo
 */
public class info extends Thread{
    
    public Socket connection;
    
    @Override
    public void run(){
        try {
            String data,res;
            DataOutputStream output_server, output_client;
            output_client = new DataOutputStream(connection.getOutputStream());
            DataInputStream input_client = new DataInputStream(connection.getInputStream()); 
            
            System.out.println("Informacion");
            while (true){
                    data = input_client.readUTF();
                    //Se muestra por pantalla el mensaje recibido
                    System.out.println(data);
                    if ("Sv?".equals(data))
                        res = "Serv|-|10000|resta";
                    else
                        res= "Solicitud incorrecta";
                    //Se le envía un mensaje al cliente usando su flujo de salida
                    output_client.writeUTF(res);
            }
        } catch (IOException ex) {
            System.out.println("No more data from "+ connection.toString());
            
        }
    }
}
