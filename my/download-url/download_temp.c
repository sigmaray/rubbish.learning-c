int download_temp() {
  //   const gchar *url = "http://cdsweb.u-strasbg.fr/cgi-bin/nph-sesame/-oI/A?M45";
  const gchar *url = "https://api.openweathermap.org/data/2.5/weather?q=Berlin&lang=ru&units=metric&appid=5a043a1bd95bf3ee500eb89de107b41e";
  GFile *file = g_file_new_for_uri(url);
  GError *error = NULL;
  gchar *content = NULL;

  if (!g_file_load_contents(file, NULL, &content, NULL, NULL, &error)) {
    g_error("%s\n", error->message);
    g_clear_error(&error);
  }
  g_object_unref(file);
	
  // g_printf("%s\n", content);
  cJSON *parsed_json = cJSON_Parse(content);
  char *printed_json = cJSON_Print(parsed_json);
  g_printf("%s\n", printed_json);

  const cJSON *main = NULL;
  main = cJSON_GetObjectItemCaseSensitive(parsed_json, "main");
  cJSON *temp = cJSON_GetObjectItemCaseSensitive(main, "temp");
  int tempVal = temp->valueint;
  return tempVal;
}
