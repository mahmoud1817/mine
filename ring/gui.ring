load "guilib.ring"

thing = new qApp{
    win = new qWidget(){
        setWindowTitle("hey bro")
        setGeometry(200,200,500,500)
	lbl   = new QLabel(win) {
	setText("write=> ")
	move(10,60)
}
//qPushButton setClickEvent
	entry = new qLineEdit(win){
	setGeometry(60,50,200,50)
	setAlignment(Qt_AlignHCenter)
	setText("hey man")
	setFont(new qFont("impact",10,1,0))
	setWinIcon(win,'../res/images/correct.png')
	setStylesheet("color:orangered")
}
        show()
    }
    exec()
}
