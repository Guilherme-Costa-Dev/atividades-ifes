package com.mycompany.projeto_completo.dao;

import com.mycompany.projeto_completo.models.Cliente;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 *
 * @author guilh
 */
public class ClienteDAO {
    
    static String URL = "jdbc:mysql://localhost:3306/projetopoo";
    static String login = "root";
    static String senha = "serra12345";
    
    public static boolean salvar(Cliente obj){
        
        Connection conexao = null;
        boolean retorno = false;
        
        try {
            //carregar o driver mysql
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            //conectar com o banco 
            conexao = DriverManager.getConnection(URL, login, senha); 
            
            //comando SQL
            PreparedStatement instrucaoSQL = conexao.prepareStatement(
                    "INSERT INTO cliente (nomeCliente, cpf, emailCliente) VALUES (?,?,?)"
            );
            
            instrucaoSQL.setString(1, obj.getNomeCliente());
            instrucaoSQL.setString(2, obj.getCPF());
            instrucaoSQL.setString(3, obj.getEmailCliente());
            
            //executar SQL
            int linhasAfetadas = instrucaoSQL.executeUpdate();
            
            if(linhasAfetadas>0){
                retorno = true;
            }
            
            
        } catch (ClassNotFoundException e){
            System.out.println("Driver nao encontrado");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            if(conexao!=null){
                try {
                    conexao.close();
                } catch (SQLException ex) {
                    System.getLogger(ClienteDAO.class.getName()).log(System.Logger.Level.ERROR, (String) null, ex);
                }
            }
        }
        
        return retorno;
    }
    
}
