fn main(){
    let mut name = "mahmoud";
    const specialname:&str = "something";
    println!("{}",name);
    name = "anas";
    println!("ur name now is {}",name);
    if name == "mahmoud"{
        println!("hey bro")
    } else if name == "anas"{
        println!("also hey bro")
    } else {
        println!("who r u?")
    }

    loop{
        println!("hey bro");
        break
    }

    while name == "anas"{
        println!("hey man");
        break
    }
    let list = vec!["mahmoud","anas","yusef"];
    for (n,i) in list.iter().enumerate() {
        println!("the name {} is {}",n,i)
    }

    let tuple1 = ("mahmoud","ans","yusef");

    println!("{}",tuple1.2);

}