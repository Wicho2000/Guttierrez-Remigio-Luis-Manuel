#!/bin/bash

declare -a urls=("https://www.virustotal.com" "https://www.mercadolibre.com" "https://best.aliexpress.com")

date_str=$(date)
csv_file="urls.csv"
json_file="urls.json"
xml_file="urls.xml"
yml_file="urls.yml"

# Inicializar archivos
printf "%s\n" "$date_str" > "$csv_file"
echo "[" > "$json_file"
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" > "$xml_file"
echo "<urls>" >> "$xml_file"
echo "---" > "$yml_file"

declare -a json_entries

for url in "${urls[@]}"; do 
    status=$(curl -m 10 -s -I "$url" | head -n 1 | awk '{print $2}')
    
    # CSV
    printf "%s,%s\n" "$url" "$status" >> "$csv_file"
    
    # JSON (guardamos en un array para evitar la última coma extra)
    json_entries+=("{ \"url\": \"$url\", \"status\": \"$status\" }")
    
    # XML
    echo "  <url>" >> "$xml_file"
    echo "    <link>$url</link>" >> "$xml_file"
    echo "    <status>$status</status>" >> "$xml_file"
    echo "  </url>" >> "$xml_file"
    
    # YAML
    echo "- url: $url" >> "$yml_file"
    echo "  status: $status" >> "$yml_file"
done

# Escribir JSON correctamente con corchetes
(IFS=","; echo "${json_entries[*]}" >> "$json_file")
echo "]" >> "$json_file"

# Cerrar XML
echo "</urls>" >> "$xml_file"

# Mostrar archivos generados
echo "Archivos generados: $csv_file, $json_file, $xml_file, $yml_file"
echo "================ CSV ================="
cat "$csv_file"
echo "================ JSON ================="
cat "$json_file"
echo "================ XML ================="
cat "$xml_file"
echo "================ YAML ================="
cat "$yml_file"