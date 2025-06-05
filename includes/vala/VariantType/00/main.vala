int main () {
  Variant message_var = new Variant.string ("Hello, World\n");
  stdout.printf(message_var.get_string());
  return 0;
}
