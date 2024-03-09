// https://zetcode.com/gui/gtk2/introduction/

#include <gtk/gtk.h>

// int main(int argc, char *argv[]) {

//     gtk_init(&argc, &argv);

//     g_printf("GTK+ version: %d.%d.%d\n", gtk_major_version, 
//         gtk_minor_version, gtk_micro_version);
//     g_printf("Glib version: %d.%d.%d\n", glib_major_version,
//         glib_minor_version, glib_micro_version);    
        
//     return 0;
// }

int main() {
  const gchar *url = "http://cdsweb.u-strasbg.fr/cgi-bin/nph-sesame/-oI/A?M45";
  GFile *file = g_file_new_for_uri(url);
  GError *error = NULL;
  gchar *content = NULL;

  if (!g_file_load_contents(file, NULL, &content, NULL, NULL, &error)) {
    g_error("%s\n", error->message);
    g_clear_error(&error);
  }
  g_object_unref(file);
	
  g_printf("%s\n", content);
}
