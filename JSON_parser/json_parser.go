package main

import (
	"fmt"
	"log"
	"os"
)



func verify_JSON(file_path string ) (bool) {

	data , err := os.ReadFile(file_path)
	if(err != nil ){
		log.Fatalln("Error in Reading file")
	}

	fmt.Println(string(data))
	
	//start reading the file
	//check if the file starts with '{' and ends with '}'

	if data[0] != '{' || data[len(data)-1] != '}' {
		return false
	}

	//check if the file has a key value pair

	



	
}






func main() {
	// read file
	// verify
	// return result 0 for valid file, 1 otherwise
	// print result



	

	







}