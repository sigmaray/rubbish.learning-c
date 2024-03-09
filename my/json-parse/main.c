// https://zetcode.com/gui/gtk2/firstprograms/

#include <gtk/gtk.h>
#include <cjson/cJSON.h>
#include "read_file.c"
#include "write_file.c"
#include "json_create.c"

GtkWidget *window;
GtkWidget *label;
GtkWidget *view;
GtkWidget *vbox;
GtkWidget *btn;

void button_clicked(GtkWidget *widget, gpointer data) {    
  // g_print("clicked\n");
  // alert(window, "clicked");
  char* new_json = json_create();
  write_file(new_json);
  alert(window, "clicked");
}

int main(int argc, char *argv[]) {
    
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

  // printf("supports_full_hd: %d", supports_full_hd("12345"));
  gchar *maps;
  if (read_file(&maps)) {
    // GString s = g_string_new(&maps);
    // printf(&maps);
    // gtk_text_buffer_set_text (buffer, maps, -1);
    cJSON *parsed_json = cJSON_Parse(maps);
    char *printed_json = cJSON_Print(parsed_json);
    // gtk_text_buffer_set_text (buffer, printed_json, -1);
  }
  // printf(&maps);
  

  gtk_container_add(GTK_CONTAINER(window), vbox);
  

  // alert(window, "message");

  // gtk_widget_show(window);
  gtk_widget_show_all(window);

  g_signal_connect(G_OBJECT(window), "destroy",
      G_CALLBACK(gtk_main_quit), NULL);

  gtk_main();

  return 0;
}
