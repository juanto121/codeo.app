import java.io.*;
import java.util.Stack;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(bfr.readLine());
		BufferedWriter bfw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int c = 1; c <= cases; c++) {
			int n = Integer.parseInt(bfr.readLine());
			
			int buildings[] = new int[n];
			int result[] = new int[n];
			String buildingString[] = bfr.readLine().split(" ");
			Stack<Integer> stack = new Stack<Integer>();

			for (int i = 0; i < n; i++) {
				buildings[i] = Integer.parseInt(buildingString[i]);
			}

			for (int i = n - 1; i >= 0; i--) {
				int building = buildings[i];
				while (!stack.empty() && building >= stack.peek()) {
					stack.pop();
				}
				
				if(!stack.empty() && building < stack.peek()) {
					result[i] = stack.peek();
				}

				if(stack.empty()) {
					result[i] = -1;
				}

				stack.push(building);
			}

			StringBuilder sb = new StringBuilder();
			
			for (int building : result){
				sb.append(building).append(" ");
			}

			bfw.write("Case #" + c + ": " + sb.toString() + "\n");
		}
		bfw.flush();
	}
}
