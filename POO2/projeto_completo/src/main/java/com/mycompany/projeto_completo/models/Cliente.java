package com.mycompany.projeto_completo.models;

/**
 *
 * @author guilh
 */
public class Cliente {
    
    //atributos
    private int idCliente;
    private String CPF;
    private String nomeCliente;
    private String emailCliente;
    
    
    //constructors
    public Cliente(int idCliente, String CPF, String nomeCliente, String emailCliente) {
        this.idCliente = idCliente;
        this.CPF = CPF;
        this.nomeCliente = nomeCliente;
        this.emailCliente = emailCliente;
    }

    public Cliente(String CPF, String nomeCliente, String emailCliente) {
        this.CPF = CPF;
        this.nomeCliente = nomeCliente;
        this.emailCliente = emailCliente;
    }
    
    
    //getters and setters
    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) {
        this.CPF = CPF;
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public String getEmailCliente() {
        return emailCliente;
    }

    public void setEmailCliente(String emailCliente) {
        this.emailCliente = emailCliente;
    }
}
