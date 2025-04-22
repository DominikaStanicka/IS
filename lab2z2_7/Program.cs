using System;
using System.IO;
using Newtonsoft.Json;
using YamlDotNet.Serialization;
using YamlDotNet.Serialization.NamingConventions;

class Program
{
    static void Main()
    {
        // Wczytanie pliku YAML bez dodatkowej klasy
        Console.WriteLine("Wczytywanie konfiguracji YAML...");
        var deserializer = new DeserializerBuilder()
            .WithNamingConvention(CamelCaseNamingConvention.Instance)
            .Build();
        
        string yamlText = File.ReadAllText("Assets/config.yaml");
        var config = deserializer.Deserialize<dynamic>(yamlText);

        // Pobranie ścieżek z YAML
        string jsonSource = "Assets/" + config["paths"]["json_source_file"];
        string jsonDest = "Assets/" + config["paths"]["json_destination_file"];
        string yamlDest = "Assets/" + config["paths"]["yaml_destination_file"];

        // Deserializacja JSON
        var deserializerJson = new DeserializeJson(jsonSource);
        deserializerJson.ShowStats();

        // Serializacja do nowego JSON
        SerializeJson.Run(deserializerJson, jsonDest);

        // Konwersja do YAML
        ConvertJsonToYaml.Run(deserializerJson, yamlDest);

        Console.WriteLine("Operacje zakończone pomyślnie!");
    }
}
