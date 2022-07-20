hello:
	echo 'hello world'
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C,W0613,W0611 project/co2_app/views.py \
		project/co2_app/models.py

all:	hello install lint
