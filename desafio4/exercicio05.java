package exercicios;

import java.util.Scanner;

public class exercicio05 {
	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		String texto;
		
		System.out.printf("Digite um texto => ");
		texto = teclado.nextLine();
		
		System.out.println(texto.toUpperCase());
	}

}
