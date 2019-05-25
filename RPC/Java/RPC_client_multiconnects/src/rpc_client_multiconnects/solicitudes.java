/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_client_multiconnects;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Vector;
import org.apache.xmlrpc.XmlRpcClient;

/**
 *
 * @author GustavoAdolfo
 */
public class solicitudes extends Thread{
    XmlRpcClient client;
    PrintWriter writer1=null,writer2 = null;

    public void run() 
        {
            try { 
         Vector params = new Vector();
         
         
         for (int i=0; i<20; i++){
             int a = (int) (Math.random() * 1000) + 1;
             int b = (int) (Math.random() * 1000) + 1;
             params.addElement(a);
             params.addElement(b);
         
            Object result = client.execute("resta.resta", params);
            writer1.println(a+" - "+b);

         
            int sum = ((Integer) result);
            System.out.println(sum);
            
            writer2.println(sum);
            params.clear();
         }

      } catch (Exception exception) {
         System.err.println("JavaClient: " + exception);
      }
    }
}


