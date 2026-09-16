package com.rays.basic;

import java.util.Iterator;

public class ContinueEx {
	public static void main(String[] args) {
		for (int i = 0; i <= 10; i++) {
			if (i % 2 == 0) {
				continue;

			}
			System.out.println("Odd Number :- " + i);
		}
	}

}
