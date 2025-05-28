package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Olá do GS PING em Docker (Exercício 6)!")
	})

	fmt.Println("Servidor GS PING rodando na porta 8080...")
	http.ListenAndServe(":8080", nil)
}