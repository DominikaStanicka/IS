using System;
using System.IO;
using YamlDotNet.Serialization;
using YamlDotNet.Serialization.NamingConventions;

class ConvertJsonToYaml
{
    public static void Run(DeserializeJson deserializedData, string destinationFile)
    {
        Console.WriteLine("Konwertowanie JSON do YAML...");
        var serializer = new SerializerBuilder()
            .WithNamingConvention(CamelCaseNamingConvention.Instance)
            .Build();

        string yamlOutput = serializer.Serialize(deserializedData.Data);
        File.WriteAllText(destinationFile, yamlOutput);
        Console.WriteLine("Zapisano plik YAML!");
    }
}
