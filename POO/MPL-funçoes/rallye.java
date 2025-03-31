import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

public class rallye {
    public static void main(String[] args) {
        // formato da lista com os dados
        // {{inscricao, tempo1, tempo2, tempo3, pontos1, pontos2, pontos3, totalPontos}, {inscricao, tempo1, tempo2, tempo3, pontos1, pontos2, pontos3, totalpontos}}

        //chamada das funcoes
        ArrayList<Double> temposPadrao = lerTemposPadrao();
        ArrayList<ArrayList<Double>> equipes = lerDadosEquipes();
        ArrayList<ArrayList<Double>> equipesComPts = calcPts(equipes, temposPadrao);
        int vencedora = calcVencedor(equipesComPts);

        //declarar tabela com tamanho da lista
        int numLinhas = equipesComPts.size()+1;
        int numCol = equipesComPts.get(0).size();
        String[][] tabela = new String[numLinhas][numCol];

        //adicionar legenda na tabela
        tabela[0][0] = "Equipes";
        tabela[0][1] = "Tempo 1";
        tabela[0][2] = "Tempo 2";
        tabela[0][3] = "Tempo 3";
        tabela[0][4] = "Pts 1";
        tabela[0][5] = "Pts 2";
        tabela[0][6] = "Pts 3";
        tabela[0][7] = "Total";

        //adicionar valores na tabela
        for (int i = 1 ; i < numLinhas ; i++) {
            for (int j = 0 ; j < numCol ; j++) {
                tabela[i][j] = String.valueOf(equipesComPts.get(i-1).get(j));
            }
        }

        //print da tabela
        for (int i = 0 ; i<tabela.length ; i++) {
            for (int j = 0 ; j<tabela[i].length ; j++) {
                System.out.printf("%-10s", tabela[i][j]);
            }
            System.out.println();
        } 

        //print da equipe vencedora
        System.out.println("Equipe Vencedora: ");
        ArrayList<Double> equipeVencedora = equipesComPts.get(vencedora);
        for (int i = 0; i < numCol; i++) {
            System.out.printf("%-10s", String.valueOf(equipeVencedora.get(i)));
        }

    }

    public static ArrayList<Double> lerTemposPadrao() {
        ArrayList<Double> lista = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        for (int i = 1 ; i<=3 ; i++) {
            System.out.println("Digite o tempo padrão " + i + ":");
            double tempo = scanner.nextDouble();
            lista.add(tempo);
        }
        return lista;
    }

    public static ArrayList<Double> lerTemposEquipes() {
        ArrayList<Double> lista = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        for (int i = 1; i <= 3; i++) {
            System.out.println("Digite o tempo da volta " + i + ":");
            double tempo = scanner.nextDouble();
            lista.add(tempo);
        }
        return lista;
    }

    //funcao que retorna uma lista de listas
    public static ArrayList<ArrayList<Double>> lerDadosEquipes() {
        Scanner scanner = new Scanner(System.in);

        //lista que sera retornada, cada equipe é uma lista, numero de inscriçao é o index 0 de cada lista, e a volta os 3 consecutivos
        ArrayList<ArrayList<Double>> equipes = new ArrayList<>();
        int index = 1;

        while (true) {
            System.out.println("Digite o número de inscrição da equipe "+index+":");
            double numInscricao = scanner.nextDouble();
            if (numInscricao == 9999) {
                break;
            }

            ArrayList<Double> equipe = new ArrayList<>();

            //adiciona na lista da equipe o numero de inscricao e o tempo da volta
            equipe.add(numInscricao);
            equipe.addAll(lerTemposEquipes());

            //adiciona a equipe na lista de equipes
            equipes.add(equipe);

            index++;
        }
        scanner.close();
        return equipes;
    }

    public static ArrayList<ArrayList<Double>> calcPts(ArrayList<ArrayList<Double>> equipes, ArrayList<Double> tempoPadrao) {
        //nova lista com os pontos
        ArrayList<ArrayList<Double>> equipesComPts = new ArrayList<>();

        for (int i = 0 ; i < equipes.size() ; i++) {
            ArrayList<Double> novaEquipe = new ArrayList<>(equipes.get(i));
            double total = 0;

            for (int j = 1; j < equipes.get(i).size(); j++) {

                double diferenca = Math.abs(tempoPadrao.get(j - 1) - equipes.get(i).get(j));
                double pontos;

                if (diferenca < 3) {
                    pontos = 100;
                } else if (diferenca <= 5) {
                    pontos = 80;
                } else {
                    pontos = 80 - (diferenca - 5) / 5;
                }

                novaEquipe.add(pontos);
                total += pontos;
            }

            novaEquipe.add(total);
            equipesComPts.add(novaEquipe);
        }
        return equipesComPts;
    }

    public static int calcVencedor (ArrayList<ArrayList<Double>> equipesComPts) {
        //a funcao compara os pontos e retorna a posicao da equipe com maior ponto
        double maior = 0;
        int posMaior = 0;
        for (int i = 0 ; i<equipesComPts.size() ; i++) {
            if (equipesComPts.get(i).get(7) > maior) {
                maior = equipesComPts.get(i).get(7);
                posMaior = i;
            }
        }
        return posMaior;
    }
}