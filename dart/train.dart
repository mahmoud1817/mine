void main() {
  String name = "mahmoud", anothername = "anas", space = " ";
  var some = "1";
  some ??="hey";

  String? name2 = "ans"; print(name2!);
  print(name + "$space" + anothername);

// string + int || int + string = error

  if (name == "mahmoud" && anothername == "anas") {
    print(int.parse(some) + int.parse(some));
  } else if (name == "mahmoud") {
    print("-_-");
  } else {
    print("whatever");
  }

  print(17 ~/ 6); //home folder
  
  switch (name2){
    case "folan":{
      print("hey folan");
      break;
    }
    case "ans":{
      print("hey bro");
      break;
    }
    default:{
      print("anyway");
    }
  }
  for(int i=0;i<3;i++){
    print('brooo');
  }
}
