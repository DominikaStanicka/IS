using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

class SerializeJson
{
    public static void Run(DeserializeJson deserializedData, string fileLocation)
    {
        Console.WriteLine("Serializowanie JSON...");
        List<Dictionary<string, object>> processedData = new List<Dictionary<string, object>>();

        foreach (var item in deserializedData.Data)
        {
            processedData.Add(new Dictionary<string, object>
            {
                { "Kod_TERYT", item["Kod_TERYT"] },
                { "Województwo", item["Województwo"] },
                { "Powiat", item.ContainsKey("Powiat") ? item["Powiat"] : "Brak danych" },
                { "typ_JST", item["typ_JST"] },
                { "nazwa_urzędu_JST", item["nazwa_urzędu_JST"] },
                { "miejscowość", item["miejscowość"] },
                { "telefon_z_numerem_kierunkowym", item.ContainsKey("telefon_z_numerem_kierunkowym") ? item["telefon_z_numerem_kierunkowym"] : "Brak danych" }
            });
        }

        string jsonOutput = JsonConvert.SerializeObject(new { departaments = processedData }, Formatting.Indented);
        File.WriteAllText(fileLocation, jsonOutput);
        Console.WriteLine("Zapisano plik JSON!");
    }
}
