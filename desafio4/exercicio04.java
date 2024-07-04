package exercicios;

public class exercicio04 {
	public static void main(String[] args) {
		String texto01 = "Será que são iguais?";
		String texto02 =  "Será que são iguais?";
		
		boolean t1 = texto01.equalsIgnoreCase(texto02);
		
		System.out.println(t1);
	}
}
