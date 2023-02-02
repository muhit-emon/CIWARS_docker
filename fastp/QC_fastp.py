import os, sys
import subprocess
import argparse
	
class fastp(object):
	
	def __init__(self, input_file1, input_file2):
		
		output_file1_name = os.path.splitext(os.path.basename(input_file1))[0] + "_clean" + os.path.splitext(os.path.basename(input_file1))[1]
		output_file2_name = os.path.splitext(os.path.basename(input_file2))[0] + "_clean" + os.path.splitext(os.path.basename(input_file2))[1]

		output_file1_path = "./output/" + output_file1_name
		output_file2_path = "./output/" + output_file2_name
		
		self.command = ["./fastp", "-i", input_file1, "-I", input_file2, "-o", output_file1_path, "-O", output_file2_path, "--detect_adapter_for_pe", "--trim_poly_g", 
				"--trim_poly_x", "--low_complexity_filter", "--average_qual", "10", "--thread", "8"]
		
	def run(self):
		try:
			
			if sys.version_info >= (3, 5):
				subprocess.run(self.command, stdout=subprocess.DEVNULL)
			else:
				subprocess.call(self.command, stdout=subprocess.DEVNULL)
			
			#subprocess.run(self.command)
			return True 
		
		except Exception as e: 
			print(e)
			return False
	
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-if", "--forward_pe_file", type = str, required = True, help = "Path to forward paired end file (required)")
	parser.add_argument("-ir", "--reverse_pe_file", type = str, required = True, help = "Path to reverse paired end file (required)") 
	
	args = parser.parse_args()
	qc = fastp(input_file1 = args.forward_pe_file, input_file2 = args.reverse_pe_file)
	if not qc.run(): 
		return 0

if __name__ == '__main__':
	main()