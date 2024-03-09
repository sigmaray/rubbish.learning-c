int write_file(gchar* contents) {
  // g_file_get_contents("main.c")  
  if (!g_file_set_contents ("out-json.json", contents, -1, NULL)) {
      // printf("l9\n");
      return FALSE;
  }
  // printf(contents);
  // printf("l13\n");
  return TRUE;
}
