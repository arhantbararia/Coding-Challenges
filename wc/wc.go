package main


import (
	"fmt"
	"os"
	"flag"
)




func count_function(filename string , word_count bool , line_count bool , byte_count bool  ) (string ) {
	var outputString string = ""

	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		return ""
	}
	defer file.Close()

	var wordCount int = 0
	var lineCount int = 0
	var byteCount int = 0

	buf := make([]byte, 1024)
	for {
		n, err := file.Read(buf)
		if n == 0 {
			break
		}
		if err != nil {
			fmt.Println(err)
			return ""
		}
		byteCount += n
		if word_count {
			wordCount += len( string(buf) )
		}
		if line_count {
			lineCount += 1
		}
	}

	if word_count {
		outputString += fmt.Sprintf("Word Count: %d\n", wordCount)
	}

	if line_count {
		outputString += fmt.Sprintf("Line Count: %d\n", lineCount)
	}

	if byte_count {
		outputString += fmt.Sprintf("Byte Count: %d\n", byteCount)
	}

	return outputString



	
}



func main () {
	word_count := flag.Bool("w", false, "Word Count")
	line_count := flag.Bool("l", false, "Line Count")
	byte_count := flag.Bool("c", false, "Byte Count")
	flag.Parse()
	args := flag.Args()

	if len(args) == 0 {
		fmt.Println("Please provide a file name")
		return
	}

	if !*word_count && !*line_count && !*byte_count {
		*word_count = true
		*line_count = true
		*byte_count = true
	}

	for _, filename := range args {
		fmt.Println(count_function(filename, *word_count, *line_count, *byte_count))
	}

	
	

	

}


