// https://zetcode.com/gui/gtk2/introduction/

#include <gtk/gtk.h>
#include <cjson/cJSON.h>
#include "download_temp.c"

// int main(int argc, char *argv[]) {

//     gtk_init(&argc, &argv);

//     g_printf("GTK+ version: %d.%d.%d\n", gtk_major_version, 
//         gtk_minor_version, gtk_micro_version);
//     g_printf("Glib version: %d.%d.%d\n", glib_major_version,
//         glib_minor_version, glib_micro_version);    
        
//     return 0;
// }

// int main() {
//   int temp = download_temp();
//   printf("temp: %d\n", temp);
// }

void alert(GtkWindow *main_application_window, gchar *message) {
    GtkWidget *dialog;
    dialog = gtk_message_dialog_new(main_application_window,
                                    GTK_DIALOG_DESTROY_WITH_PARENT,
                                    GTK_MESSAGE_INFO,
                                    GTK_BUTTONS_CLOSE,
                                    message
                                    );
    gtk_dialog_run(GTK_DIALOG (dialog));
    gtk_widget_destroy(dialog);
}

// #include <gtk/gtk.h>
// #include <cjson/cJSON.h>
// #include "read_file.c"
// #include "write_file.c"
// #include "json_create.c"

GtkWidget *window;
GtkWidget *label;
GtkWidget *view;
GtkWidget *vbox;
GtkWidget *btn;

void button_clicked(GtkWidget *widget, gpointer data) {    
  // g_print("clicked\n");
  // alert(window, "clicked");
  // char* new_json = json_create();
  // write_file(new_json);
  // alert(window, "clicked");
  int temp = download_temp();
  // printf("temp: %d\n", temp);
  // char *out;
  // sprintf(&out, "temp: = %d", temp);
  // gchar *out;
  // g_sprintf
  // alert(window, *out);
  GString *s;
  s = g_string_new("");
  g_string_append_printf(s, "temp: = %d", temp);
  alert(window, s->str );
  // printf("%s", s->str);
}

char* get_time() {
  GTimeVal curTime;
	g_get_current_time(&curTime);
  GDateTime* gdt = g_date_time_new_from_timeval_local(&curTime);
  char *formatted = g_date_time_format(gdt,
                    "%Y-%m-%dT%H:%M:%S.%f");
  
  return formatted;
}

int main(int argc, char *argv[]) {
  get_time();
    
  // GtkWidget *window;
  // GtkWidget *view;
  // GtkWidget *vbox;
  // GtkWidget *btn;
  
  GtkTextBuffer *buffer;

  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title(GTK_WINDOW(window), "JSON");
  gtk_window_set_default_size(GTK_WINDOW(window), 500, 500);
  gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);

  label = gtk_label_new("Json read from in-json.yml:");
  vbox = gtk_vbox_new(FALSE, 0);
  view = gtk_text_view_new();
  btn = gtk_button_new_with_label("Gen json and Write it to out-json.yml");
  g_signal_connect(G_OBJECT(btn), "clicked", 
      G_CALLBACK(button_clicked), NULL);

  gtk_widget_set_size_request(btn, 70, 30);
  gtk_box_pack_start(GTK_BOX(vbox), label, TRUE, TRUE, 0);
  gtk_box_pack_start(GTK_BOX(vbox), view, TRUE, TRUE, 0);
  gtk_box_pack_start(GTK_BOX(vbox), btn, TRUE, TRUE, 0);
  buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(view));
  // gtk_text_buffer_set_text (buffer, "Hello, this is some text", -1);
  // char *monitor = create_monitor();
  // printf("\"%s\"", monitor);
  // gtk_text_buffer_set_text (buffer, monitor, -1);

  // // printf("supports_full_hd: %d", supports_full_hd("12345"));
  // gchar *maps;
  // if (read_file(&maps)) {
  //   // GString s = g_string_new(&maps);
  //   // printf(&maps);
  //   // gtk_text_buffer_set_text (buffer, maps, -1);
  //   cJSON *parsed_json = cJSON_Parse(maps);
  //   char *printed_json = cJSON_Print(parsed_json);
  //   // gtk_text_buffer_set_text (buffer, printed_json, -1);
  // }
  // // printf(&maps);
  

  gtk_container_add(GTK_CONTAINER(window), vbox);
  

  // alert(window, "message");

  // gtk_widget_show(window);
  gtk_widget_show_all(window);

  g_signal_connect(G_OBJECT(window), "destroy",
      G_CALLBACK(gtk_main_quit), NULL);

  gtk_main();

  return 0;
}
