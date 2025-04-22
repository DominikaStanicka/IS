using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

class DeserializeJson
{
    public List<Dictionary<string, object>> Data { get; private set; }

    public DeserializeJson(string filename)
    {
        Console.WriteLine("Deserializowanie JSON...");
        string jsonText = File.ReadAllText(filename);
        Data = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(jsonText);
    }

    public void ShowStats()
    {
        int count = 0;
        foreach (var item in Data)
        {
            if (item.ContainsKey("typ_JST") && item["typ_JST"].ToString() == "GM" &&
                item.ContainsKey("Województwo") && item["Województwo"].ToString() == "dolnośląskie")
            {
                count++;
            }
        }
        Console.WriteLine($"Liczba urzędów miejskich w województwie dolnośląskim: {count}");
    }
}
