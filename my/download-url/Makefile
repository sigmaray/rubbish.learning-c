main: main.c
	# gcc -w -o main main.c `pkg-config --libs --cflags gtk+-2.0`
	gcc -g -w -o main main.c `pkg-config --libs --cflags gtk+-2.0` -lcjson

clean:
	@rm main || true
