/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testmarkov;

import Jama.Matrix;
import java.io.PrintWriter;
import java.util.Arrays;

/**
 *
 * @author remy
 */
public class TestMarkov {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Test des chaines des Markov");
        
        double[][] probaMatrix = new double[4][4];
        probaMatrix[0][0] = 0;
        probaMatrix[0][1] = 1;
        probaMatrix[0][2] = 0;
        probaMatrix[0][3] = 0;
        
        probaMatrix[1][0] = 0;
        probaMatrix[1][1] = 0;
        probaMatrix[1][2] = 0.1;
        probaMatrix[1][3] = 0.9;
        
        probaMatrix[2][0] = 0;
        probaMatrix[2][1] = 1;
        probaMatrix[2][2] = 0;
        probaMatrix[2][3] = 0;
        
        probaMatrix[3][0] = 1;
        probaMatrix[3][1] = 0;
        probaMatrix[3][2] = 0;
        probaMatrix[3][3] = 0;
        double[] res = calculateLimitBehaviour(probaMatrix);
        
        System.out.println("Résultat: " + Arrays.toString(res));
    }
    
    
    public static double[] calculateLimitBehaviour(double[][] probabilityMatrix) {
        // On crée une nouvelle matrice de la taille+1 avec la ligne suplémentaire remplie de 1
        int ligne = probabilityMatrix.length;
        int colonne = probabilityMatrix[0].length+1;
        PrintWriter out = new PrintWriter(System.out, true);
        
        Matrix lhs = new Matrix(ligne, colonne, 1);
        
        // On remplit la matrice que l'on vient de créé par la matrice passé en pramètre
        lhs.setMatrix(0, ligne-1, 0, colonne-2, new Matrix(probabilityMatrix));
        
        // On retire la matrice identitée à notre matrice (formule du cours de simulation)
        // (la nouvelle ligne n'est pas impactée vue que la marice n'est plus carré après son insertion)
        lhs.minusEquals(Matrix.identity(ligne, colonne));
        
        lhs.print(out, colonne-1, 1);
        
        // On transpose pour pouvoir utiliser après la décomposition LU dessus
        lhs = lhs.transpose();
        
        // RHS seras nos réponses sous forme d'un vecteur (matrice de largeur 1) remplie de 0,
        // sauf à la dernière ligne ou c'est 1 (pour répondre à la formule x+y+... = 1
        Matrix rhs = new Matrix(colonne, 1);
        rhs.set(colonne-1, 0, 1);
        
        // On lance la résolution (qui utilise une décomposition LU)
        Matrix ans = lhs.solve(rhs);
        ans = ans.transpose();
        
        System.out.println(" * ");
        ans.print(out, ans.getColumnDimension()-1, 4);
        
        System.out.println(" = ");
        rhs.print(out, colonne-1, 1);
        
        return  ans.getArray()[0];
    }
    
}
