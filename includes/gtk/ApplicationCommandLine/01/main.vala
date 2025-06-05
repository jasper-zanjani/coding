public class ApplicationCommandLineExample : Application {
    public ApplicationCommandLineExample () {
        Object (flags: ApplicationFlags.HANDLES_COMMAND_LINE);
    }

    private const OptionEntry[] options = { // (1)
        { "name", 'n', 0, OptionArg.STRING, null, N_("Greet the specified name"), },
        {},
    };

    construct {
        add_main_option_entries(options);
    }

    public override void activate () { }

    public override int command_line (ApplicationCommandLine command_line) { // (2)
        var options = command_line.get_options_dict ();

        if ("name" in options) {
            var name = options.lookup_value("name", VariantType.STRING);
            if (name != null)
                stdout.printf("Hello, %s\n", name.get_string());
        }
        else
            stdout.printf("Hello, World!\n");

        return 0;
    }
}

int main (string[] args) {
    Intl.textdomain ("ApplicationCommandLineExample"); // (3)
    var app = new ApplicationCommandLineExample();
    return app.run (args);
}
