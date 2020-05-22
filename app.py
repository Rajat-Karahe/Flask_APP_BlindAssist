import os
from flask import Flask, render_template,request
from commons import MobileNet

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

model = MobileNet()

# from inference import get_denomination_name

@app.route('/',methods=['GET','POST'])
def hello_world():
		return render_template('index.html')

		

@app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method=='POST':
		f = request.files['file']
		saveLocation = f.filename
		f.save(saveLocation)
		denomination_name = model.infer(saveLocation)
		os.remove(saveLocation)

		return render_template('result.html',denomination=denomination_name)

			
		



@app.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('about.html')
 

if __name__ == '__main__':
	app.run(debug=True,port=os.getenv('PORT',5000))
	




				
		    
		    
		    