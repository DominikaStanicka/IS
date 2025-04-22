using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using System.Linq;

class DeserializeJson
{
    public List<Dictionary<string, object>> Data { get; private set; } = new();

    public DeserializeJson(string filename)
    {
        Console.WriteLine("Deserializowanie JSON...");
        string jsonText = File.ReadAllText(filename);
        Data = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(jsonText);
    }

    public void ShowStats()
    {
        // Słownik do przechowywania liczby JST w każdym województwie
        Dictionary<string, int> wojewodztwaStats = new Dictionary<string, int>();

        foreach (var item in Data)
        {
            if (item.ContainsKey("typ_JST") && item["typ_JST"].ToString() == "GM" &&
                item.ContainsKey("Województwo"))
            {
                string wojewodztwo = item["Województwo"].ToString();
                
                // Jeśli województwo już jest w słowniku, zwiększamy licznik
                if (wojewodztwaStats.ContainsKey(wojewodztwo))
                {
                    wojewodztwaStats[wojewodztwo]++;
                }
                else
                {
                    // Jeśli nie, dodajemy je do słownika i ustawiamy licznik na 1
                    wojewodztwaStats[wojewodztwo] = 1;
                }
            }
        }

        // Wyświetlenie wyników
        Console.WriteLine("\nLiczba urzędów miejskich (GM) w każdym województwie:");
        foreach (var entry in wojewodztwaStats.OrderByDescending(x => x.Value))
        {
            Console.WriteLine($"- {entry.Key}: {entry.Value}");
        }
    }
}
