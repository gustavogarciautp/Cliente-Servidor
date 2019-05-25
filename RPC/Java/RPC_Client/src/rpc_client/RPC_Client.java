/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_client;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Vector;
import org.apache.xmlrpc.XmlRpcClient;
import org.apache.xmlrpc.*;


/**
 *
 * @author GustavoAdolfo
 */
public class RPC_Client {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        FileWriter file1=null,file2 = null;
        PrintWriter writer1=null,writer2 = null;
        try {
         XmlRpcClient client = new XmlRpcClient("http://192.168.0.13:10000"); 
         Vector params = new Vector();
         
            file1 = new FileWriter("log_client_send.txt");
            writer1 = new PrintWriter(file1);
            file2 = new FileWriter("log_client_recv.txt");
            writer2 = new PrintWriter(file2);
         
         for (int i=0; i<2000; i++){
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
      finally {
           try {
           if (null != file1)
              file1.close();
           if (null != file2)
              file2.close();
           } catch (Exception e2) {
              e2.printStackTrace();
           }
    }
    }
    
}
