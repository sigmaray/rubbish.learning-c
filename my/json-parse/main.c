// https://zetcode.com/gui/gtk2/firstprograms/

#include <gtk/gtk.h>
#include <cjson/cJSON.h>
#include "json_create.c"

int read_file(gchar** contents) {
  // g_file_get_contents("main.c")  
  if (!g_file_get_contents("json.json", contents, NULL, NULL)) {
      // printf("l9\n");
      return FALSE;
  }
  // printf(contents);
  // printf("l13\n");
  return TRUE;
}

/* return 1 if the monitor supports full hd, 0 otherwise */
// int supports_full_hd(const char * const monitor)
// {
//     const cJSON *resolution = NULL;
//     const cJSON *resolutions = NULL;
//     const cJSON *name = NULL;
//     int status = 0;
//     cJSON *monitor_json = cJSON_Parse(monitor);
//     if (monitor_json == NULL)
//     {
//         const char *error_ptr = cJSON_GetErrorPtr();
//         if (error_ptr != NULL)
//         {
//             fprintf(stderr, "Error before: %s\n", error_ptr);
//         }
//         status = 0;
//         goto end;
//     }

//     name = cJSON_GetObjectItemCaseSensitive(monitor_json, "name");
//     if (cJSON_IsString(name) && (name->valuestring != NULL))
//     {
//         printf("Checking monitor \"%s\"\n", name->valuestring);
//     }

//     resolutions = cJSON_GetObjectItemCaseSensitive(monitor_json, "resolutions");
//     cJSON_ArrayForEach(resolution, resolutions)
//     {
//         cJSON *width = cJSON_GetObjectItemCaseSensitive(resolution, "width");
//         cJSON *height = cJSON_GetObjectItemCaseSensitive(resolution, "height");

//         if (!cJSON_IsNumber(width) || !cJSON_IsNumber(height))
//         {
//             status = 0;
//             goto end;
//         }

//         if ((width->valuedouble == 1920) && (height->valuedouble == 1080))
//         {
//             status = 1;
//             goto end;
//         }
//     }

// end:
//     cJSON_Delete(monitor_json);
//     return status;
// }

int main(int argc, char *argv[]) {
    
  GtkWidget *window;
  GtkWidget *view;
  GtkWidget *vbox;
  
  GtkTextBuffer *buffer;

  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title(GTK_WINDOW(window), "JSON");
  gtk_window_set_default_size(GTK_WINDOW(window), 230, 150);
  gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);

  vbox = gtk_vbox_new(FALSE, 0);
  view = gtk_text_view_new();
  gtk_box_pack_start(GTK_BOX(vbox), view, TRUE, TRUE, 0);
  buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(view));
  // gtk_text_buffer_set_text (buffer, "Hello, this is some text", -1);
  // char *monitor = create_monitor();
  // printf("\"%s\"", monitor);
  // gtk_text_buffer_set_text (buffer, monitor, -1);

  // printf("supports_full_hd: %d", supports_full_hd("12345"));
  gchar *maps;
  if (read_file(&maps)) {
    // GString s = g_string_new(&maps);
    printf(&maps);
    gtk_text_buffer_set_text (buffer, maps, -1);
  }
  // printf(&maps);
  

  gtk_container_add(GTK_CONTAINER(window), vbox);

  alert(window, "message");

  // gtk_widget_show(window);
  gtk_widget_show_all(window);

  g_signal_connect(G_OBJECT(window), "destroy",
      G_CALLBACK(gtk_main_quit), NULL);

  gtk_main();

  return 0;
}
