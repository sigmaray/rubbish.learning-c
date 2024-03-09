main: main.c
	# -w -- без ворнингов
	# -g -- с дебаг символами
	gcc -g -w -o main main.c `pkg-config --libs --cflags gtk+-2.0` -lcjson

clean:
	@rm main || true
