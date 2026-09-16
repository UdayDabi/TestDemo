package com.rays.basic;

public class SwitchEx {
	public static void main(String[] args) {
		String str = "Monday";
		
		 switch (str) {
		case "Monday":
			System.out.println("First day of Week");
			
		case "Tus":
			System.out.println("Sec day of Week");
			break;
		case "Wen":
			System.out.println("Third day of Week");
			break;
		case "Thu":
			System.out.println("Fourth day of Week");
			break;
		case "Fri":
			System.out.println("Fivth day of Week");
			break;
		case "Sat":
			System.out.println("Sixth day of Week");
			break;

		default:
			System.out.println("Wow Chill day Enjoy Sunday");
			break;
		}

	}

}
