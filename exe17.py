from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"
print(f"Copying from {from_file} to {to_file}.")
indata = open(from_file).read()
print(f"The input file is {len(indata)} bytes long.")
print(f"Does the output file exist? {exists(to_file)}")
print("READY. Hit RETURN to continue and CTRL_C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright. All done!")
out_file.close()


#### use only one line to do above
#open(to_file,"w").write(open(from_file).read())



