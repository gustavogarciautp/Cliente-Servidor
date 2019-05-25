/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_client_multiconnects;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.util.Vector;
import org.apache.xmlrpc.XmlRpcClient;

/**
 *
 * @author GustavoAdolfo
 */
public class RPC_client_multiconnects {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws MalformedURLException, IOException, InterruptedException {
        // TODO code application logic here
            FileWriter file1= new FileWriter("log_client_send.txt");
            FileWriter file2 = new FileWriter("log_client_recv.txt");
            PrintWriter writer1=new PrintWriter(file1);
            PrintWriter writer2 = new PrintWriter(file2);
            Vector threads = new Vector();
        for (int i=0; i<40; i++){
            XmlRpcClient client = new XmlRpcClient("http://192.168.0.13:10000"); 
            solicitudes thread = new solicitudes();
            threads.addElement(thread);
            thread.client = client;
            thread.writer1 = writer1;
            thread.writer2 = writer2;
            thread.start();
            
        }
        solicitudes thread = new solicitudes();
        for (int i=0; i< threads.size();i++){
            thread=(solicitudes) threads.elementAt(i);
            thread.join();
        }
           if (null != file1)
              file1.close();
           if (null != file2)
              file2.close();
           } 
    
        
    }
    

