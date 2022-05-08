package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func aname(folan string){
	println("hello",folan)
}

func main(){
	fmt.Println("mahmoud");
	fmt.Println("anas")
	var num = 10.9;
	var number = 9;
	fmt.Println(int(num));
	for i:=7;i<number;i++{
		fmt.Println(num);
	}
	m:="mahmoud"; o:=0
	println(m)

	println("ali","hasan") //println = "space between"

	type Names struct{
		name1 string
		name2 string
		age1 int16
		age2 int16
	}

	fmt.Printf("%T %v %s",m,10,m) //captial p and fmt addedN
	name := bufio.NewScanner(os.Stdin)
	name2 := bufio.NewScanner(os.Stdin)
	urnum := bufio.NewScanner(os.Stdin)
	print("\nenter ur name: ")
	name.Scan()
	print("enter ur name: ")
	name2.Scan()
	entered:= name.Text()
	entered2:= name2.Text()
	print("enter ur num: ")
	urnum.Scan()
	converted,_:=strconv.ParseInt(urnum.Text(),10,64)
	println("hello ",entered , "......",entered2)
	fmt.Printf("ur num is: %d",converted)

	var mynum1 = 10
	var mynum2 = 9.5
	var ans    = float64(mynum1) - mynum2
	fmt.Printf("\n %.2f",ans)
	//! && ||
	if name2 == name{
		println("hello bro")
	}else{
		println("who r u man?")
	}
	for ans <10 {
		println("hello bro")
		ans++;ans+=5
	}
	switch{
	case o>0:
		println("positive")
	case o<0:
		println("negative")
	default:
		println("just zero")
	}

	myarr:=[]string{"mahmoud","anas","yusuf"}
	fmt.Println(myarr[0:3])

	for i,e := range myarr{
		fmt.Printf("%d: %s\n",i,e)
	}

	var p map[string]int = map[string]int{
		"orange":2,
		"kiwi" : 5,
	}
	fmt.Println(p)
	aname("ali")
}