/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rpc_server;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import org.apache.xmlrpc.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author GustavoAdolfo
 */
public class RPC_Server {

    /**
     * @param op1
     * @param op2
     * 
     * @return 
     */
   public Integer resta(int op1, int op2){
       String op1_1 = Integer.toString(op1);
       String op2_1 = Integer.toString(op2);
       System.out.println("Resta " + op1_1 + " - "+ op2_1);
      return op1-op2;
   }
     

   public static void main (String [] args){
   
      try {        
         
         WebServer server = new WebServer(10000);
         server.addHandler("resta", new RPC_Server());
         server.start();
        
         accepting thread =new accepting();
         thread.start();
         
         
      } catch (Exception exception){
          System.out.println("client disconnect");
      }
   }
}

